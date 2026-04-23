# CI / CD 流程

> 适用范围：Sprint 73+。本文档解释 pyantv 仓库的持续集成与持续部署机制，
> 帮助贡献者理解 PR 触发了哪些校验、为什么失败、如何在本地复现。

## 概览

pyantv 在 GitHub Actions 上维护 **3 个 workflow**：

| Workflow | 文件 | 触发条件 | 作用 |
|---------|------|---------|------|
| **pyantv CI** | `.github/workflows/python-app.yml` | 所有 push / PR | lint + docs 校验 + 多平台构建 + 单元测试 |
| **pyantv Docs Deploy** | `.github/workflows/docs-deploy.yml` | master 分支变更 `docs/**` 或 `mkdocs.yml` | 构建并部署文档站到 GitHub Pages |
| **Release** | `.github/workflows/release.yml` | 推送 `v*` 形式的 git tag | 构建 sdist + wheel 并发布到 PyPI |

## pyantv CI（python-app.yml）

包含 3 个 job，均使用 [`uv`](https://github.com/astral-sh/uv) 作为依赖管理器
（与本地开发完全同构，避免 "本地通过 / CI 失败" 的尴尬）。

### Job 1：`lint`

- **运行环境**：`ubuntu-latest` + Python 3.12
- **执行命令**：`uv run make lint` →
  `flake8 --exclude=build,example,.venv,examples --max-line-length=89`
- **失败条件**：任何 flake8 错误或警告
- **本地复现**：`make lint`

### Job 2：`docs`（Sprint 73+ 新增）

- **运行环境**：`ubuntu-latest` + Python 3.12
- **依赖**：`needs: lint`（lint 通过后才跑，避免浪费 CI minutes）
- **执行命令**：`uv run mkdocs build --strict --site-dir site`
- **失败条件**：在 `--strict` 模式下，以下情况均会让 CI 失败：
  - mkdocs.yml `nav` 中引用了不存在的 `.md` 文件
  - Markdown 内 `[text](other.md)` 链接到不存在的目标
  - `docs/` 目录下存在未在 `nav` 中引用的"孤儿文档"
  - Markdown 解析告警（如代码块语言标识符拼写错误）
- **本地复现**：

  ```shell
  uv sync --group docs       # 推荐
  # 或纯 pip（需要 pip >= 25.1）：
  pip install -e . --group docs
  make docs-build
  ```

> 💡 这个 job 是为了避免之前出现过的 "文档与代码不一致" 问题
> （详见 Sprint 73 修复记录中删除的 `charts/histogram.md` / `charts/facet.md`
> 等死链）。任何 PR 现在都会被 mkdocs strict 校验拦截。

### Job 3：`build`

- **运行环境**：3 个 OS × 6 个 Python 版本 = **18 个并行 job**
  - OS：`ubuntu-latest`、`macos-latest`、`windows-latest`
  - Python：`3.8`、`3.9`、`3.10`、`3.11`、`3.12`、`3.13`
- **依赖**：`needs: lint`
- **执行步骤**：
  1. `uv sync --group dev --group test --extra all` 安装完整开发依赖（dev/test 走 PEP 735 [dependency-groups]）
  2. `uv run python -m build` 构建 sdist + wheel（PEP 517）
  3. `uv run pytest -v --cov-config=.coveragerc --cov=./ --cov-fail-under=95 test/`
     — 覆盖率不到 95% 直接失败
  4. 上传 coverage 报告到 Codecov
- **本地复现**：`make check`（= `make lint` + `make test`）

## pyantv Docs Deploy（docs-deploy.yml）

### 触发条件

仅满足以下**全部条件**时才会触发：

1. push 到 `master` 或 `main` 分支
2. 本次提交涉及 `docs/**`、`mkdocs.yml` 或 workflow 自身

也支持手动触发：GitHub 仓库 → Actions → "pyantv Docs Deploy" → Run workflow。

### 流程

```
build job:
  ↓ checkout（fetch-depth: 0，给 setuptools-scm 完整 git 历史）
  ↓ setup Python 3.12
  ↓ uv sync --group docs
  ↓ uv run mkdocs build --strict --site-dir site
  ↓ actions/upload-pages-artifact@v3

deploy job (needs: build):
  ↓ actions/deploy-pages@v4
  → https://sunhailin-Leo.github.io/pyantv
```

### 一次性配置

仓库管理员需要做以下设置（**仅首次部署前需要做**）：

1. **GitHub 仓库 → Settings → Pages**
   - Source 选择 `GitHub Actions`（不是 `Deploy from a branch`）
2. 首次部署成功后，`github-pages` environment 会自动创建

### 安全性

- 使用 GitHub 官方的 `actions/deploy-pages@v4`，无需配置任何 token / secret
- 通过 `id-token: write` 权限走 OIDC 流程，零密钥
- `concurrency: pages` 保证同一时间只有一个部署任务

## Release（release.yml）

### 触发条件

推送形如 `v0.1.0`、`v1.2.3` 的 git tag（`v*` 通配）。

### 流程概览

1. setuptools-scm 从 git tag 自动派生版本号（无需手动改 `__version__`）
2. `python -m build` 构建 sdist + wheel
3. `twine upload dist/*` 发布到 PyPI（需配置 `PYPI_API_TOKEN` secret）

详细发布步骤请参考 [贡献指南](../CONTRIBUTING.md#发布流程)。

## 本地与 CI 同构的命令速查

| 想做什么 | 本地命令 | CI 中对应的 step |
|---------|---------|-----------------|
| 跑 lint | `make lint` | `lint` job |
| 校验文档 | `make docs-build` | `docs` job |
| 跑全量单元测试 + 覆盖率 | `make test` | `build` job 的 pytest step |
| lint + test 完整组合 | `make check` | `lint` + `build` |
| 本地预览文档 | `make docs` | — |
| 重建 uv.lock | `make uv-lock` | — |

## 常见问题

### Q1：`docs` job 失败，提示 `Doc file 'foo.md' contains a link 'bar.md', but the target is not found`

**原因**：你在 `docs/foo.md` 里引用了不存在的 `bar.md`。

**解决**：检查链接拼写，或先创建 `docs/bar.md`，或把 `bar.md` 加到 `mkdocs.yml` 的 `nav` 中。

### Q2：`docs` job 失败，提示 `The following pages exist in the docs directory, but are not included in the "nav" configuration`

**原因**：你在 `docs/` 下新建了 `.md` 文件但忘了加到 `mkdocs.yml` 的 `nav`。

**解决**：把新文件加进 `nav`；如果它确实只是一个被其他文档引用的"内嵌片段"，
可以考虑放到 `docs/_includes/` 或类似不会被 mkdocs 扫描的目录。

### Q3：本地 `make docs-build` 报 `mkdocs: command not found`

**原因**：本地没装 `docs` 依赖组。

**解决**：`uv sync --group docs`（推荐）；或 `pip install -e . --group docs`（需 pip >= 25.1）。

### Q4：CI 上 `lint` 失败但本地通过

**原因**：本地 flake8 版本与 CI 不一致；或本地用 IDE 修改时未触发 flake8。

**解决**：用 uv 跑同一份依赖：`uv run make lint`，与 CI 完全一致。

# Contributing to pyantv

感谢你有兴趣为 pyantv 做贡献！我们欢迎任何形式的贡献，包括但不限于：修复 bug、添加新功能、改进文档、编写测试、优化性能等。

本文档面向人类开发者，提供了参与 pyantv 开发的完整指南。如果你是 AI agent，请参考 [CLAUDE.md](CLAUDE.md)。

## Getting Started

### 环境搭建

首先克隆仓库并安装开发依赖：

```bash
# 克隆仓库
git clone https://github.com/sunhailin-Leo/pyantv.git
cd pyantv

# 使用 uv 安装（推荐，CI 同构）
pip install uv
uv sync --group dev --group test --extra all

# 或者使用 pip 安装（fallback，需要 pip >= 25.1 才支持 --group）
pip install --upgrade pip
pip install -e '.[all]' --group dev --group test --group docs
```

安装完成后，你可以运行以下命令验证环境：

```bash
# 运行测试
pytest test/

# 运行代码检查
make lint
```

### 项目结构

了解项目的基本结构有助于你快速找到需要修改的代码：

- `pyantv/` - 核心源代码目录
  - `charts/` - 图表类实现
  - `options/` - 配置选项类
  - `render/` - 渲染引擎
  - `commons/` - 公共工具
  - `datasets/` - 内置数据集
- `test/` - 测试代码目录
- `example/` - 示例代码目录
- `docs/` - 文档目录
- `scripts/` - 辅助脚本目录

## Development Workflow

### 开发流程

pyantv 遵循标准的开发工作流程：

1. **Fork 仓库**：在 GitHub 上 fork pyantv 仓库到你的账号
2. **创建分支**：基于 `master` 分支创建你的功能分支
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **编写代码**：按照代码规范编写你的代码
4. **运行测试**：确保所有测试通过
   ```bash
   pytest test/
   ```
5. **代码格式化**：使用 black 和 isort 格式化代码
   ```bash
   make format
   # 或
   black .
   isort .
   ```
6. **代码检查**：运行 linter 检查代码质量
   ```bash
   make lint
   ```
7. **提交更改**：编写清晰的提交信息并提交
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
8. **推送分支**：将分支推送到你的 fork 仓库
   ```bash
   git push origin feature/your-feature-name
   ```
9. **创建 PR**：在 GitHub 上创建 Pull Request

### 代码规范

pyantv 使用以下工具来保证代码质量：

- **black**：代码格式化工具，确保代码风格统一
- **isort**：import 语句排序工具
- **flake8**：代码检查工具，检查代码风格和潜在问题

在提交 PR 之前，请确保：

1. 代码通过 `make lint` 检查
2. 代码通过 `make format` 格式化
3. 所有测试通过 `make test`

## Pull Request Guidelines

### PR 规范

创建 Pull Request 时，请遵循以下规范：

1. **使用 PR 模板**：创建 PR 时会自动加载 [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md)，请完整填写模板中的内容
2. **清晰的标题**：PR 标题应该简洁明了地描述你的更改
3. **详细的描述**：在 PR 描述中说明：
   - 你解决了什么问题
   - 你如何解决的
   - 相关的 issue 编号（如果有的话）
4. **小而专注**：每个 PR 应该只解决一个问题或添加一个功能
5. **测试覆盖**：为新功能添加相应的测试
6. **文档更新**：如果更改了 API，请更新相关文档

### PR 审查流程

提交 PR 后，维护者会进行代码审查。审查过程中可能会要求你：

- 修改代码实现
- 添加更多测试
- 改进文档
- 优化性能

请积极响应审查意见，并及时更新你的 PR。

### PR 合并

PR 满足以下条件后会被合并：

1. 所有测试通过
2. 代码审查通过
3. 至少一位维护者批准
4. 没有冲突

## Testing

### 测试规范

pyantv 使用 pytest 作为测试框架。测试代码位于 `test/` 目录下，按模块组织：

- `test/test_*.py` - 各个图表类的测试
- `test/test_options.py` - 配置选项的测试
- `test/test_render.py` - 渲染功能的测试

### 运行测试

```bash
# 运行所有测试
make test
# 或
pytest -v --cov-config=.coveragerc --cov=./ test/

# 运行单个测试文件
pytest test/test_line.py

# 运行单个测试方法
pytest test/test_line.py::TestLineChart::test_line_base

# 运行特定标记的测试
pytest -m "not slow"
```

### 编写测试

为新功能编写测试时，请遵循以下原则：

1. **测试独立**：每个测试应该独立运行，不依赖其他测试
2. **测试覆盖**：尽量覆盖所有边界情况
3. **清晰的测试名称**：测试名称应该清楚地描述测试的内容
4. **使用 fixture**：合理使用 pytest fixture 来减少重复代码

### 视觉测试

pyantv 包含双轨视觉回归测试（pixel + SSIM），以确保图表渲染的正确性：

- **Pixel 路径**：基于 `test/baselines/` 目录下的基线 PNG，逐像素对比
- **SSIM 路径**（Sprint 66 引入）：基于 `scikit-image` 的结构相似性指数，对抗锯齿更鲁棒
  - 助手模块：`test/visual_ssim_helpers.py`
  - 基线目录：`test/baselines_ssim/`（与 pixel 基线完全隔离）
  - 依赖：`pip install 'pyantv[test]'`（包含 `scikit-image>=0.19.0`）
  - 未安装 `skimage` 时，相关用例会通过 `pytest.importorskip` 优雅 skip

运行视觉测试：

```bash
pytest test/test_visual_regression.py   # pixel 路径
pytest test/test_visual_ssim.py         # SSIM 路径
```

## Release Process

### 发布流程

pyantv 自 **Sprint 72** 起采用 `setuptools-scm` + git tag 自动派生版本号，无需手动维护版本字符串。完整发布流程如下：

1. **更新 CHANGELOG**：在 `CHANGELOG.md` 顶部追加本次发布的更改（`### Added` / `### Changed` / `### Fixed`）
2. **本地预检**：跑全量测试 + lint，确保零回归
   ```bash
   make check   # 等价于 make lint + make test
   ```
3. **本地构建并验证 wheel**（可选，CI 也会做）
   ```bash
   make build
   ls dist/     # 确认产生 .tar.gz + .whl
   ```
4. **打 git tag 并推送**：tag 名遵循 `vX.Y.Z` 格式，`setuptools-scm` 会据此自动派生版本号
   ```bash
   git tag -a v1.2.3 -m "Release v1.2.3"
   git push origin v1.2.3
   ```
5. **GitHub Actions 自动发布**：`.github/workflows/release.yml` 会在 tag 推送时自动构建、校验并上传到 PyPI，无需手动 `make publish`
6. **创建 GitHub Release**：在 GitHub 上基于 tag 创建 Release，复制 CHANGELOG 对应章节作为 release notes

> 紧急情况下也可手动 `make publish`（内部依次执行 `clean → python -m build → twine upload dist/*`），但**首选 tag 触发的自动化流程**。

### 版本号规范

pyantv 遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范：

- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

## 与 CLAUDE.md 的关系

pyantv 项目包含两份面向不同受众的开发文档：

- **CLAUDE.md**：面向 AI agent（如 Claude Code），提供项目架构、构建命令、测试方法等技术细节，帮助 AI agent 更好地理解和修改代码
- **CONTRIBUTING.md**（本文件）：面向人类开发者，提供完整的贡献指南，包括环境搭建、开发流程、PR 规范等

这两份文档互相补充，各有侧重：
- CLAUDE.md 更注重技术实现细节和命令行操作
- CONTRIBUTING.md 更注重社区协作和开发规范

如果你是 AI agent，请优先参考 CLAUDE.md；如果你是人类开发者，请阅读本文件。

## Good First Issues

如果你是第一次贡献，可以从 [Good First Issues](docs/good-first-issues.md) 列表中选择适合的任务开始。这些任务通常难度较低，有明确的实现指引，是熟悉项目的好方式。

## 获取帮助

如果在贡献过程中遇到任何问题，可以通过以下方式获取帮助：

- **GitHub Issues**：在 [Issues](https://github.com/sunhailin-Leo/pyantv/issues) 中提问
- **GitHub Discussions**：在 [Discussions](https://github.com/sunhailin-Leo/pyantv/discussions) 中讨论
- **文档**：查阅 [docs/](docs/) 目录下的文档

## 行为准则

参与 pyantv 社区时，请遵守我们的行为准则：

- 尊重所有贡献者
- 欢迎不同观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

感谢你的贡献！

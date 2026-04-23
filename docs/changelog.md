# 更新日志

> 本页是文档站内的精简变更日志摘要。完整原文请参阅仓库根目录的 [CHANGELOG.md](https://github.com/sunhailin-Leo/pyantv/blob/master/CHANGELOG.md)。

## [Unreleased]

### Sprint 73 — Jupyter Notebook 深度集成
- 图表对象自动支持 `_repr_html_`，cell 末位置图表对象即可内联渲染
- 新增 `pyantv.render.notebook.notebook_config()` 全局配置（width / height / theme）
- 新增 `notebooks/quickstart.ipynb` 快速入门 notebook
- 三语 README 追加 Colab / Binder badge

### Sprint 72 — 版本管理自动化
- 迁移到 `setuptools-scm` + git tag 派生版本号，移除手动版本维护
- 新增 `.github/workflows/release.yml`：tag 推送时自动 build + 校验 + 发布到 PyPI
- 新增 `test/test_version.py` 验证版本号格式与作者信息

### Sprint 71 — 截图脚本与 Colab 集成
- 新增 `scripts/gen_doc_screenshots.py` 自动批量截图（Playwright）
- README 三语版同步追加 Colab / Binder 入口
- 新增 `test/test_doc_screenshots.py`（脚本可达性、--help、空白 HTML 容错）

### Sprint 70 — 图表文档自动化
- 新增 `scripts/gen_chart_docs.py`：AST 解析 → 自动生成 `docs/charts/<type>.md`（44 个图表页）
- 新增 `docs/charts/index.md` 图表总览，按 8 大分类组织
- `mkdocs.yml` nav 段重构为 8 顶级条目
- 新增 `--check` 模式用于 CI 一致性验证

### Sprint 69 — ROADMAP 刷新与覆盖率门禁
- ROADMAP 标记已完成功能并新增 Sprint 70-73 计划
- CI 添加 `--cov-fail-under=95` 强制门禁
- 新增专属测试文件：`test_interval3d.py` / `test_line3d.py` / `test_point3d.py` / `test_text.py`

### Sprint 68 — 社区与可发现性
- 新增 `docs/assets/gallery_preview.png` 4×3 示例画廊预览图
- `.github/ISSUE_TEMPLATE/` 升级为结构化 YAML Forms（bug / feature / docs / config）
- 新增 `CONTRIBUTING.md`、`docs/comparison.md`、`docs/good-first-issues.md`

### Sprint 67 — Property-based 测试
- 集成 Hypothesis：3 个 profile（dev=20 / ci=100 / exhaustive=1000）
- 新增 `test/test_hypothesis_properties.py`，17 个 property 测试

### Sprint 66 — 视觉测试增强（SSIM 双轨）
- 新增 `test/visual_ssim_helpers.py`，基于 scikit-image 的 SSIM 对比
- 抗锯齿边缘掩码（Canny + 形态学膨胀）
- 与原 pixel 路径并行，零改动旧用例

### Sprint 65 — 类型提示完整度
- 新增 `scripts/gen_type_stubs.py`：AST 自动生成 `pyantv/options/*.pyi`
- Makefile 新增 `make stubs` / `make stubs-check`
- 4 个退出码契约 + 幂等性保证

### Sprint 64 — 大数据性能
- 新增 `downsample()` 函数：LTTB / uniform / random 三种算法
- `Chart.set_data()` 新增 `sample_if_large` 等采样参数
- 新增 `compact` JSON 序列化（HTML 体积减少 ≥40%）
- 新增性能基线（本地 500ms / CI 800ms）

### Sprint 63 — 离线资源支持
- 新增 `pyantv.offline` 模块：`AssetRegistry`、`install_assets()`、`set_offline_host()`
- 跨平台 `file://` URI（Windows/Linux/macOS）
- 默认锁定 G2 5.2.11 版本

### Sprint 62 — 打包现代化
- `pyproject.toml` 成为 Single Source of Truth，`build-backend` 修正为官方 `setuptools.build_meta`
- `setup.py` 精简为 thin shim（< 10 行），删除 `UploadCommand`
- `uv` 作为 CI 必装依赖管理器，`uv.lock` 入 git
- `MANIFEST.in` 全面重写
- 新增 `make publish` 替代 `python setup.py upload`

---

## 历史版本

### Sprint 37-61 — 预设系统、事件系统、高级图表
- 33 个 Preset 函数（主题 / 动画 / 布局 / 坐标系 / 交互 / 转换 / 格式化）
- `ChartEvent` 枚举（90+ G2 事件常量）+ `Chart.set_events()` API
- 高级图表：`Funnel` / `WaterFall` / `Bullet`
- 基础图表扩展：`Partition` / `Beeswarm`
- 快捷方法：`from_data()` / `from_dataframe()` / `set_title()` / `set_padding()` / `set_size()`
- 自定义主题：Tech / Business / Fresh
- 数据格式化：`format_number` / `format_percent` / `format_currency` / `format_date`
- 批量导出：`batch_export_png()`

### Sprint 29-36 — 核心质量与生态基础
- 输入校验与 `TypeError` 友好提示
- 标注系统：`LineAnnotationOpts` / `RegionAnnotationOpts` / `TextAnnotationOpts`
- 数据变换：25 种 Transform 选项类
- Streamlit 集成：`st_pyantv()`
- 图表导出：`export_png()` / `export_svg()` + `save_as_image()` / `save_as_svg()`（Playwright）
- CI/CD：flake8 lint + PyPI 自动发布
- 文档站：MkDocs 基础配置 + `make docs`

### Sprint 25-28 — 数据源与图表扩展
- pandas DataFrame / numpy ndarray 数据源支持
- Web 框架集成：Flask / Django / Sanic（`render_chart_to_html()` / `make_response()`）
- 3D 图表：`Point3D` / `Line3D` / `Interval3D`
- 插件系统：`use_renderer()` / `use_rough()` / `use_lottie()`

> 完整变更日志请参阅 [CHANGELOG.md](https://github.com/sunhailin-Leo/pyantv/blob/master/CHANGELOG.md)

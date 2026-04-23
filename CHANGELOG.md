# Changelog

本文件记录 pyantv 的版本变更历史。格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [0.2.0]

### Removed

- **Python 3.8 支持**：Python 3.8 已于 2024-10-07 正式 EOL，且大量上游开发依赖（如 `black>=25.1`、`mypy` 新版等）已不再支持 3.8，导致 `uv sync` 在 universal lock 求解阶段无法找到可行解。`requires-python` 收紧到 `>=3.9`；`pyproject.toml` classifier、CI 矩阵、Issue 模板下拉选项同步移除 3.8

### Changed

- **PEP 735 dependency groups 迁移**：`dev` / `test` / `docs` 三组开发向依赖从 `[project.optional-dependencies]` 迁移到 `[dependency-groups]`（PEP 735），与 uv/pip 官方主推方向对齐；安装命令从 `uv sync --dev --extra all` / `pip install -e '.[dev,test,all]'` 切换为 `uv sync --group dev --group test --extra all` / `pip install -e '.[all]' --group dev --group test --group docs`（后者需要 pip >= 25.1）；用户向 `pip install pyantv[all]` 等用法不受影响

### Added

- **文档 CI 校验**：`.github/workflows/python-app.yml` 新增 `docs` job，每次 push / PR 都执行 `uv run mkdocs build --strict`，任何死链 / 未引用文档 / Markdown 解析告警都会让 CI 失败
- **GitHub Pages 自动部署**：新增 `.github/workflows/docs-deploy.yml`，master 分支变更 `docs/**` 或 `mkdocs.yml` 时自动构建并部署到 GitHub Pages（基于 `actions/deploy-pages@v4` + OIDC，无需配置任何 secret）
- **Makefile 同构目标**：新增 `make docs-build` 目标，本地与 CI 中 docs job 行为完全一致
- **CI / CD 文档**：新增 `docs/development/ci.md`，详细说明 CI / Docs Deploy / Release 三个 workflow、本地与 CI 同构的命令速查表、4 条 FAQ
- **Jupyter Notebook 深度集成**：所有 Chart 子类继承 `_repr_html_()`，在 Jupyter Notebook / JupyterLab / Google Colab / VS Code Notebook 中直接内联渲染；新增 `pyantv/render/notebook.py` 提供 `build_iframe_html()` / `is_notebook()` / `notebook_config()`
- **Notebook 全图表展示**：新增 `notebooks/all_charts.ipynb`，展示 20+ 个图表类型；新增 `scripts/gen_notebooks.py` 从 `example/*.py` 自动生成 Notebook
- **Notebook 使用指南**：新增 `docs/notebook-guide.md`（Colab / Binder / VS Code Notebook 全覆盖）；三语言 README 追加 Binder badge
- **图表截图生成器**：新增 `scripts/gen_chart_screenshots.py`，基于 Playwright 自动从 `example/` 目录的 HTML 文件生成图表截图，输出到 `docs/assets/charts/`
- **Colab 快速入门**：新增 `notebooks/quickstart.ipynb` 与 Colab badge（三语 README）
- **图表文档自动化**：新增 `scripts/gen_chart_docs.py`，基于 AST 自动从 `pyantv/charts/basic_charts/` 与 `pyantv/charts/composition_charts/` 生成 `docs/charts/<type>.md`，支持 `--check` 模式做 CI 一致性校验
- **图表总览页**：新增 `docs/charts/index.md`，按 8 大分类（统计 / 分布 / 关系 / 地理 / 特殊 / 3D / 组合 / 基础标记）组织 44 个图表类型导航
- **示例画廊预览图**：新增 `scripts/gen_gallery_preview.py` 与 `scripts/gallery_preview_manifest.yaml`，自动生成 4×3 网格预览图（`docs/assets/gallery_preview.png`）
- **社区文档**：新增 `CONTRIBUTING.md`、`docs/comparison.md`、`docs/good-first-issues.md`；`.github/ISSUE_TEMPLATE/` 升级为结构化 YAML Forms（bug_report / feature_request / documentation / config）；`.github/PULL_REQUEST_TEMPLATE.md` 新增 Summary / Type / Checklist 三段结构
- **版本管理自动化**：迁移到 `setuptools-scm` + git tag 派生版本号；`.github/workflows/release.yml` 在推送 `v*` tag 时自动构建并发布到 PyPI
- **类型存根生成器**：新增 `scripts/gen_type_stubs.py`，AST 自动生成 `pyantv/options/*.pyi`；`make stubs` / `make stubs-check` 两个目标
- **离线资源管理**：新增 `pyantv.offline` 模块（`install_assets` / `set_offline_host` / `get_active_host` / `AssetRegistry` / `OfflineInstallError`），默认注册 G2 5.2.11，支持内网部署与 `file://` 协议
- **大数据降采样**：新增 `pyantv.data.pipeline.downsample()`，支持 LTTB（默认）/ uniform / random 三种算法；`Chart.set_data()` 新增 `sample_if_large` / `sample_method` / `sample_x_field` / `sample_y_field` 参数
- **紧凑 JSON 序列化**：`Base.dump_options()` / `render()` / `render_embed()` 新增 `compact: bool` 参数，启用后 HTML 体积减少 ≥40%；JsCode 占位符在 compact 模式下逐字节保留
- **快捷出图 API**：`Chart.from_data()` / `Chart.from_dataframe()` 类方法，一行代码出图，自动推断编码字段；`from_dataframe()` 自动把 NaN/NaT 转为 None
- **事件系统**：新增 `ChartEvent` 枚举类（90+ 个 G2 v5 事件常量，含 ELEMENT / PLOT / LEGEND / AXIS / TOOLTIP / BRUSH / SLIDER 等分类）+ `Chart.set_events()` Pythonic 事件绑定 API
- **Preset 系统**：新增 `pyantv.presets` 模块，31 个开箱即用的预设函数（主题 / 动画 / 布局 / 坐标系 / 交互 / 数据转换 / 格式化 / 工具）
  - 主题：`with_dark_theme` / `with_tech_theme` / `with_business_theme` / `with_fresh_theme`
  - 交互：`with_tooltip` / `with_element_highlight` / `with_element_select` / `with_brush_highlight` / `with_brush_filter` / `with_fisheye` / `with_slider_filter`
  - 数据转换：`with_sort_by` / `with_stack` / `with_normalize` / `with_group` / `with_jitter`
  - 格式化：`format_number` / `format_percent` / `format_currency` / `format_date`
  - 工具：`batch_export_png` 支持一次导出多个图表为 PNG
- **快捷配置方法**：`set_title(text, subtitle, align)` / `set_padding(top, right, bottom, left)` / `set_size(width, height, is_auto_fit)` 简化常用配置
- **新增图表类型**：`Funnel`（漏斗图）、`WaterFall`（瀑布图）、`Bullet`（子弹图）、`Partition`（分区图）、`Beeswarm`（蜂群图）
- **顶层导出**：`ChartEvent`、`JsCode`、`presets` 模块可从 `pyantv` 顶层直接导入
- **视觉测试增强**：新增 SSIM 视觉回归测试路径（`test/test_visual_ssim.py` + `test/visual_ssim_helpers.py`），与原 pixel 路径双轨并存；支持抗锯齿边缘掩码与 SSIM 分数水印
- **Property-based 测试**：集成 Hypothesis（`test/test_hypothesis_properties.py`，17 个测试），通过 `HYPOTHESIS_PROFILE` 环境变量切换 dev / ci / exhaustive 三档
- **性能基线测试**：新增 `test/test_performance.py` 与 `test/baselines/perf_baseline.json`，本地 / CI 阈值分层（500ms / 800ms），通过 `CI` 环境变量自动切换；`benchmarks/bench_render.py` 扩展 `html_size` / `compact_vs_pretty` / `downsample` 三组基准
- **依赖分组**：`optional-dependencies` 扩充到 10 个分组（pandas / numpy / export / streamlit / notebook / offline / docs / test / dev / all）；`all` 仅包含"用户向"分组，避免拉入 500MB+ 开发依赖

### Changed

- **打包现代化**：`pyproject.toml` 成为依赖与元数据的 Single Source of Truth；`build-backend` 改为官方 `setuptools.build_meta`；`setup.py` 精简为 thin shim
- **依赖管理**：CI 切换到 `uv` 作为依赖管理器（`uv sync` + `uv run`），本地推荐 `make uv-install`；`uv.lock` 纳入 git 版本控制保证可重现构建
- **构建产物**：`make build` 改用 `python -m build`（PEP 517 标准），替代 `python setup.py sdist bdist_wheel`
- **CI 覆盖率门禁**：pytest 启用 `--cov-fail-under=95`，覆盖率不足 95% 直接失败
- **CI 矩阵**：`build` job 扩展为 3 个 OS（Ubuntu / macOS / Windows）× 6 个 Python 版本（3.8 / 3.9 / 3.10 / 3.11 / 3.12 / 3.13）= 18 个并行 job
- **MANIFEST.in 全面重写**：补上 `CHANGELOG.md` / `LICENSE` / `pyproject.toml` / `*.pyi` / `uv.lock`；修复原 `include changelog.md`（小写）在大小写敏感文件系统上漏打包的 bug
- **mkdocs 导航**：`mkdocs.yml` nav 段重构为 9 个顶级条目（首页 / 快速开始 / 图表 / Presets / Options / API 参考 / 对比 / 贡献指南 / 开发者指南 / 更新日志 / 社区）
- **README 三语版同步**：源码安装推荐 `make uv-install`；单元测试段改用 `make test` / `make lint` / `make check`；新增 Docs Deploy badge；CI badge 链接精确到对应 workflow
- **文档全量对齐**：修复 mkdocs 死链（histogram / facet / space / repeat → facet_circle / facet_rect / space_flex / space_layer / repeat_matrix / view）；修正 `BoxPlot` 类名（驼峰）；统一图表数量为 44、Preset 数量为 31、示例数量为 440+；扩充 `docs/api-reference.md` 补齐 from_data / from_dataframe / set_events / ChartEvent / set_title / set_padding / set_size / install_assets / downsample 等 API 与精确签名

### Removed

- **`UploadCommand`**：从 `setup.py` 移除（该类通过 `os.system("python setup.py sdist bdist_wheel")` 自调用，在 thin shim 下会无限递归）；改用 `make publish` 串行执行 `clean → build → twine upload`
- **手动版本号维护**：移除手动维护的 `__version__` 常量，迁移到 `setuptools-scm` 自动派生
- **`python setup.py install` / `python test.py`**：CI workflow 中的老派写法被淘汰，改用 `uv run pytest`

### Other

- 单元测试总数 833+，覆盖率 99.89%（CI 门禁 ≥ 95%）
- `make lint` 零错误零警告
- 新增 `test/test_packaging.py`（10 个配置回归测试）、`test/test_chart_docs.py`、`test/test_doc_screenshots.py`、`test/test_notebook_render.py`、`test/test_offline.py`、`test/test_downsample.py`、`test/test_set_data_sampling.py`、`test/test_dump_options_compact.py`、`test/test_performance.py`、`test/test_type_stubs_generator.py`、`test/test_version.py`、`test/test_interval3d.py` / `test_line3d.py` / `test_point3d.py` / `test_text.py` 等专项测试文件
- `pyproject.toml` 新增依赖：`setuptools-scm>=8.0`（构建时）、`scikit-image>=0.19.0`（视觉测试）、`hypothesis>=6.0.0`（property 测试）、`pytest-benchmark>=4.0.0`（性能基准）、`ipython>=7.0`（Notebook 集成）

---

## [0.1.0]

### Added

- **核心 API**：`Chart` 基类与链式 API（`set_data` / `set_encode` / `set_global_options` / `render` / `render_embed` 等）
- **基础图表**：`Line`（折线图）、`Interval`（柱状图）、`Area`（面积图）、`Point`（散点图）等基于 G2 mark 的基础图表
- **统计与分布图**：`BoxPlot`（箱线图）、`Density`（密度图）等
- **关系图**：`Sankey`（桑基图）、`Chord`（弦图）、`ForceGraph`（力导向图）、`Treemap`（矩形树图）、`Tree`（树图）、`Pack`（圆形打包）
- **地理图**：`GeoPath`、`GeoView`
- **特殊图**：`Gauge`（仪表盘）、`Liquid`（水波图）、`Wordcloud`（词云）
- **3D 图表**：`Point3D`、`Line3D`、`Interval3D`
- **基础标记**：`Rect` / `Cell` / `Link` / `Arc` / `Text` / `Path` / `Shape` / `Connector` / `Range` / `Image` / `Polygon` / `Vector` / `Heatmap` / `Box`
- **组合图表**：`FacetCircle` / `FacetRect` / `SpaceFlex` / `SpaceLayer` / `RepeatMatrix` / `View` / `TimingKeyFrame`
- **数据变换**：25 种 Transform 选项类（`GroupXOpts` / `StackYOpts` / `NormalizeYOpts` 等）
- **标注系统**：`LineAnnotationOpts`（参考线）、`RegionAnnotationOpts`（区域标注）、`TextAnnotationOpts`（文本标注）、`Chart.set_annotations()`
- **pandas 集成**：`set_data()` 支持 DataFrame / Series / numpy ndarray，自动转换为 G2 所需的字典列表
- **输入校验**：`set_data()` / `Base.__init__()` / `use_renderer()` 传入错误参数时抛出清晰的 `TypeError`
- **手写类型存根**：`pyantv/charts/chart.pyi` / `base.pyi` / `mixins.pyi`，IDE 可正确推断链式调用返回类型
- **Web 框架集成**：`render_chart_to_html()` / `make_response()`（Flask / Django / Sanic）；`pyantv.web.streamlit.st_pyantv()` Streamlit 组件
- **图表导出**：`export_png()` / `export_svg()` 函数 + `Chart.save_as_image()` / `Chart.save_as_svg()` 实例方法（基于 Playwright）
- **插件系统**：`use_renderer()`（Canvas / SVG / WebGL）、`use_rough()`（手绘风格）、`use_lottie()`（Lottie 动画）
- **CI/CD**：GitHub Actions lint 检查 + PyPI 自动发布工作流
- **文档站**：MkDocs 基础配置 + `make docs` 命令
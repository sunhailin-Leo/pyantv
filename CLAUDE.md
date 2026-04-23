# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pyantv is a Python visualization library that generates AntV G2 charts. It provides a simple API with method chaining support for creating interactive charts.

## Build, Test, and Lint Commands

### Install dev dependencies (recommended: uv with PEP 735 dependency groups)

```bash
# uv path (CI uses the same commands)
pip install uv
uv sync --group dev --group test --extra all
# Or via Makefile:
make uv-install

# Pure pip fallback (requires pip >= 25.1 for --group support)
pip install -e '.[all]' --group dev --group test --group docs
# Or via Makefile:
make install-dev
```

> Note: dev / test / docs dependencies live under `[dependency-groups]` (PEP 735),
> not `[project.optional-dependencies]`. So `uv sync --dev` and
> `pip install -e '.[dev]'` are no longer valid — always use `--group <name>`.

### Test / Lint / Build

```bash
# Run all tests
make test
# or
pytest -v --cov-config=.coveragerc --cov=./ test/

# Run a single test file
pytest test/test_line.py

# Run a specific test method
pytest test/test_line.py::TestLineChart::test_line_base

# Run linter
make lint
# or
flake8 --exclude=build,example,.venv,examples --max-line-length=89

# Format code
black .
isort .

# Build package (PEP 517)
make build
# or
python -m build
```

## Architecture Overview

### Package Structure

- **`pyantv/charts/`**: Chart classes organized by type
  - `basic_charts/`: Line, Area, Bar (Interval), Point, Pie, Heatmap, Rect, Polygon, Box, Boxplot, Cell, Chord, Density, ForceGraph, Gauge, Image, Link, Liquid, Pack, Range, Sankey, Shape, Tree, Treemap, Vector, WordCloud
  - `composition_charts/`: View, FacetCircle, FacetRect, SpaceFlex, SpaceLayer, RepeatMatrix, TimingKeyFrame, GeoView
- **`pyantv/options/`**: Configuration option classes
  - `global_options.py`: Axis, Legend, Tooltip, Label, Style, Interaction, Animation, etc.
  - `chart_options.py`: Data, Encode, Scale, Coordinate, Transform, etc.
  - `series_options.py`: Base option classes (BasicOpts)
- **`pyantv/render/`**: Rendering engine for HTML and Notebook output
- **`pyantv/commons/`**: Shared utilities
- **`pyantv/datasets/`**: Built-in example datasets

### Core Classes

- **`Base`** (`pyantv/charts/base.py`): Root class for all charts, handles initialization, rendering, and JavaScript dependencies
- **`Chart`** (`pyantv/charts/chart.py`): Provides common chart methods (set_data, set_encode, set_global_options, etc.)
- **`ChartMixin`** (`pyantv/charts/mixins.py`): Mixin for JSON rendering
- **Option classes**: All use `BasicOpts` base class with `opts` dict pattern

### Key Patterns

1. **Method chaining**: All chart modification methods return `self`
2. **Options pattern**: Configuration via dataclass-like opts (e.g., `opts.TitleOpts(title="...")`)
3. **Import convention**: `from pyantv import options as opts`
4. **Rendering**: Uses Jinja2 templates with JSON-serialized options
5. **Composition**: View container holds multiple chart children

### JavaScript Dependencies

Charts use AntV G2 library loaded via CDN (default: `https://unpkg.com/`). Configurable via `CurrentConfig`.

## Additional Notes

- Default page title is "Awesome-pyantv"; configurable via `CurrentConfig`
- The project uses `setuptools` for package management
- Tests use `pytest` with `pytest-cov` for coverage
- Coverage config is in `.coveragerc`
- **For human contributors**: see [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide (environment setup, PR process, release workflow, etc.)

---

## Harness 开发模式

> **重要**：本项目采用 Harness 开发模式管理所有功能开发的完整生命周期。

### 强制启动仪式

收到任何涉及 **sprint / harness / 合约 / 评估 / 需求开发** 的任务时，或修改 `pyantv/`、`test/`、`example/` 路径下的代码时，**必须先读取以下 3 个文件**：

```bash
read_file .harness/README.md
read_file .harness/prompts/generator.md
read_file .harness/prompts/evaluator.md
```

### 三 Agent 架构执行顺序

```
Step 1: [Planner]    需求分析 → 扩展为完整技术规格
Step 2: [Generator]  写 sprint-N-contract.md（合约先行）
Step 3: [Evaluator]  独立审查合约（sub agent，怀疑视角）
Step 4: ⏸️ 用户确认   与用户讨论合约，等待用户确认
Step 5: [Generator]  实现代码
Step 6: ⚠️ 全量回归   pytest -v --cov-config=.coveragerc --cov=./ test/
Step 7: [Evaluator]  执行评估脚本 + 独立代码审查
Step 8: 评分判定     ≥ 90 → 继续；< 90 → 修复后重跑（最多 3 轮）
```

### 关键约束

- **禁止跳过合约阶段**：必须先写合约、经 Evaluator 审查、用户确认后才能实现
- **禁止"就近验证"**：回归测试必须跑全量 `pytest -v --cov-config=.coveragerc --cov=./ test/`，禁止只跑修改涉及的文件
- **评分通过阈值**：90 分（满分 100）
- **独立 Evaluator**：使用 sub agent 以怀疑论者视角独立审查，不受 Generator 自评影响

### 豁免场景

以下场景不触发 Harness：
- 纯文档修改（`.md` 文件）
- 配置文件调整（`.gitignore`、`setup.py` 等）
- CI/CD 脚本修改
- 纯重构（不改变外部行为）

### Harness 文件结构

详见 `.harness/README.md`。

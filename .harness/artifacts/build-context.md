# Build Context — pyantv

> 累积的架构决策和项目上下文，供 Agent 在每个 Sprint 中参考。

## 项目概述

pyantv 是一个 Python 可视化库，用于生成 AntV G2 图表。它提供：
- 简洁的 Python API，支持方法链调用
- 丰富的图表类型：基础图表（20+ 种）、组合图表（8 种）
- 灵活的配置系统：通过 Options 模式配置图表样式
- 多种渲染方式：HTML 文件、Notebook 嵌入
- 多环境支持：Jupyter Notebook、JupyterLab、Zeppelin

## 核心设计模式

### 方法链
```python
from pyantv.charts import View, Line, Point
from pyantv import options as opts

c = (
    View()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_view_children(children=[line.options, point.options])
    .set_scale(scale_opts=opts.ScaleOpts(...))
    .render("output.html")
)
```

### Options 模式
```python
from pyantv.options.series_options import BasicOpts

class TitleOpts(BasicOpts):
    def __init__(self, title="", subtitle="", ...):
        self.opts = {"title": title, "subtitle": subtitle, ...}
```

### 渲染引擎
- Jinja2 模板生成 HTML
- AntV G2 选项通过 JSON 序列化嵌入
- JS 依赖通过 CDN 加载（默认: `https://unpkg.com/`）

## 项目结构

```
pyantv/
├── charts/                      # 图表类
│   ├── base.py                  # Base 基类（所有图表的根）
│   ├── chart.py                 # Chart 类（通用图表方法）
│   ├── mixins.py                # ChartMixin（JSON 渲染混入）
│   ├── basic_charts/            # 基础图表
│   │   ├── line.py              # 折线图
│   │   ├── area.py              # 面积图
│   │   ├── interval.py          # 柱状图（Interval）
│   │   ├── point.py             # 散点图
│   │   ├── pie.py               # 饼图
│   │   ├── heatmap.py           # 热力图
│   │   ├── box.py               # 箱线图
│   │   ├── boxplot.py           # 箱线统计图
│   │   ├── cell.py              # 单元格图
│   │   ├── chord.py             # 弦图
│   │   ├── density.py           # 密度图
│   │   ├── force_graph.py       # 力导向图
│   │   ├── gauge.py             # 仪表盘
│   │   ├── image.py             # 图片
│   │   ├── link.py              # 链接图
│   │   ├── liquid.py            # 水球图
│   │   ├── pack.py              # 打包图
│   │   ├── polygon.py           # 多边形图
│   │   ├── range.py             # 范围图
│   │   ├── range_x.py           # X 范围图
│   │   ├── range_y.py           # Y 范围图
│   │   ├── rect.py              # 矩形图
│   │   ├── sankey.py            # 桑基图
│   │   ├── shape.py             # 形状图
│   │   ├── tree.py              # 树图
│   │   ├── treemap.py           # 矩形树图
│   │   ├── vector.py            # 向量图
│   │   └── wordcloud.py         # 词云图
│   └── composition_charts/      # 组合图表
│       ├── view.py              # 视图容器
│       ├── facet_circle.py      # 圆形分面
│       ├── facet_rect.py        # 矩形分面
│       ├── space_flex.py        # 弹性空间布局
│       ├── space_layer.py       # 层叠空间布局
│       ├── repeat_matrix.py     # 重复矩阵
│       ├── timing_key_frame.py  # 关键帧动画
│       └── geo_view.py          # 地理视图
│
├── options/                     # 配置选项类
│   ├── global_options.py        # 全局选项（Axis, Legend, Tooltip, Label, Style...）
│   ├── chart_options.py         # 图表选项（Data, Encode, Scale, Coordinate, Transform...）
│   └── series_options.py        # 系列选项基类（BasicOpts）
│
├── render/                      # 渲染引擎
│   ├── engine.py                # 渲染核心逻辑
│   ├── display.py               # Notebook 显示
│   └── templates/               # Jinja2 HTML 模板
│
├── commons/                     # 共享工具
│   └── utils.py                 # 工具函数（JSON 处理、占位符替换等）
│
├── datasets/                    # 内置数据集
│
├── globals.py                   # 全局配置（CurrentConfig, FileType, ChartType...）
├── types.py                     # 类型定义
├── __init__.py                  # 包入口（导出版本信息）
└── _version.py                  # 版本号（0.1.0）
```

## 核心组件

### Base
- 位置: `pyantv/charts/base.py`
- 职责: 所有图表的根类，处理初始化、渲染、JS 依赖
- 关键方法: `render()`, `render_notebook()`

### Chart
- 位置: `pyantv/charts/chart.py`
- 职责: 提供通用图表方法
- 关键方法: `set_data()`, `set_encode()`, `set_global_options()`, `set_view_children()`

### ChartMixin
- 位置: `pyantv/charts/mixins.py`
- 职责: JSON 渲染混入
- 关键方法: `json_render()`

### Options 体系
- 基类: `BasicOpts`（位于 `pyantv/options/series_options.py`）
- 全局选项: `TitleOpts`, `LegendOpts`, `TooltipOpts`, `AxisOpts`, `LabelOpts` 等
- 图表选项: `DataOpts`, `EncodeOpts`, `ScaleOpts`, `CoordinateOpts`, `TransformOpts` 等

## 构建与测试命令

```bash
# 构建
make build
# 或
python setup.py sdist bdist_wheel

# 单元测试
make test
# 或
pytest -v --cov-config=.coveragerc --cov=./ test/

# Lint
make lint
# 或
flake8 --exclude=build,example,.venv --max-line-length=89 --ignore=F401

# 格式化
black .
isort .
```

## 已知约束

1. Python >= 3.6 兼容性要求
2. 默认页面标题为 "Awesome-pyantv"，可通过 `CurrentConfig` 配置
3. JS 依赖通过 CDN 加载（默认 unpkg.com），离线使用需配置本地资源
4. 核心依赖仅 jinja2 和 simplejson
5. `global_options.py` 文件较大（约 90KB），包含大量 Options 类定义

## Sprint 历史

（随着 Sprint 完成逐步填充）

| Sprint | 功能 | 日期 | 评分 |
|--------|------|------|------|
| — | 尚无 Sprint | — | — |

## 技术债务

（随着开发过程逐步记录）

| 编号 | 描述 | 优先级 | 来源 Sprint |
|------|------|--------|------------|
| — | 尚无技术债务 | — | — |

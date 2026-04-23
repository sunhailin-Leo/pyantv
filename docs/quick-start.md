# 快速开始

## 安装

### 用户：使用 pip（推荐）

```bash
pip install pyantv -U

# 按需启用可选特性：
pip install 'pyantv[pandas]'       # DataFrame 支持
pip install 'pyantv[export]'       # PNG/SVG 导出（Playwright）
pip install 'pyantv[streamlit]'    # Streamlit 集成
pip install 'pyantv[notebook]'     # Jupyter 小部件
pip install 'pyantv[offline]'      # 离线资源下载（requests）
pip install 'pyantv[all]'          # 以上用户向特性一次到位
```

### 开发者：使用 uv（推荐，CI 同构）

本项目从 **Sprint 62** 起采用 `pyproject.toml` 作为依赖的唯一来源，并将 [uv](https://docs.astral.sh/uv/) 作为官方推荐的依赖管理器。

```bash
git clone https://github.com/sunhailin-Leo/pyantv.git
cd pyantv

# 一键安装所有 dev/test 依赖 + 用户向特性
# 等价于：pip install uv && uv sync --group dev --group test --extra all
# （dev/test/docs 自 Sprint 74 起迁移到 PEP 735 [dependency-groups]）
make uv-install

# 首次生成或更新 uv.lock（lock 文件会提交到 git，保证跨机器可重现构建）
make uv-lock
```

### 开发者：纯 pip fallback

若无法使用 uv，可以退回到纯 pip 方式（**需要 pip >= 25.1** 才支持 `--group` 参数）：

```bash
pip install --upgrade pip                                      # 确保 pip >= 25.1
pip install -e '.[all]' --group dev --group test --group docs
# 或等价的 Makefile 目标：
make install-dev
```

> 旧版 `pip install -e '.[dev,test,all]'` 自 Sprint 74 起不再可用，因为 `dev`/`test`/`docs`
> 已经从 `[project.optional-dependencies]` 迁移到 `[dependency-groups]`（PEP 735），
> 这是 uv/pip 官方主推的现代写法，且开发依赖不会再污染 PyPI 包元数据。

### 发布到 PyPI（维护者）

```bash
make publish   # 内部依次执行 clean → python -m build → twine upload dist/*
```

> 旧的 `python setup.py upload` 命令已于 Sprint 62 移除（原实现通过 `os.system` 调用自身，在 thin shim 下会无限递归）。

## 一行式快捷出图（推荐）

> Sprint 50+ 引入。`from_data()` / `from_dataframe()` 自动推断编码并构造图表，适合快速出图。

```python
from pyantv import Line

# 从原始数据
chart = Line.from_data(
    data=[{"year": "2020", "value": 3}, {"year": "2021", "value": 4}],
    x_field_name="year",
    y_field_name="value",
)
chart.render("quick.html")
```

```python
import pandas as pd
from pyantv import Line

df = pd.DataFrame({"year": ["2020", "2021", "2022"], "value": [3, 4, 5]})
chart = Line.from_dataframe(df, x_field_name="year", y_field_name="value")
chart.render("quick_df.html")
```

## 事件绑定

> Sprint 51 引入。绑定 G2 v5 原生事件，支持 90+ 事件常量（详见 `pyantv.globals.ChartEvent`）。

```python
from pyantv import Line, ChartEvent

chart = (
    Line.from_data(
        data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}],
        x_field_name="x", y_field_name="y",
    )
    .set_events({
        ChartEvent.ELEMENT_CLICK: "(ev) => { console.log('clicked:', ev.data); }",
    })
)
chart.render("event_demo.html")
```

## Preset 系统（一行启用主题 / 交互 / 数据转换）

> Sprint 47-50 引入，31 个预设函数。详见 [Presets 总览](presets/index.md)。

```python
from pyantv import Line
from pyantv.presets import (
    with_dark_theme, with_smooth_animation,
    with_tooltip, with_brush_filter,
)

chart = Line.from_data(
    data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}],
    x_field_name="x", y_field_name="y",
)
with_dark_theme(chart)
with_smooth_animation(chart, duration=800)
with_tooltip(chart, shared=True, show_crosshairs=True)
with_brush_filter(chart)
chart.render("preset_demo.html")
```

## 离线资源（内网部署）

> Sprint 63 引入。下载 AntV 资源到本地目录，再切换 host 即可在内网使用。

```python
from pyantv.offline import install_assets, set_offline_host
from pathlib import Path

# 下载 G2 默认版本（5.2.11）到 ~/.pyantv/assets
result = install_assets()
print(result)  # {'G2': '/Users/.../g2.min.js'}

# 切换到本地 host（支持 file:// 协议）
set_offline_host(Path(result["G2"]).parent.as_uri())
```

## 基础折线图

```python
from pyantv import Line

line = (
    Line()
    .set_data(data=[
        {"year": "2020", "value": 3},
        {"year": "2021", "value": 4},
        {"year": "2022", "value": 3.5},
        {"year": "2023", "value": 5},
    ])
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(width=640, height=480, is_auto_fit=True)
)
line.render("line_chart.html")
```

## pandas DataFrame 数据源

```python
import pandas as pd
from pyantv import Line

df = pd.DataFrame({
    "year": ["2020", "2021", "2022", "2023"],
    "value": [3, 4, 3.5, 5],
})
line = Line().set_data(data=df).set_encode(x_field_name="year", y_field_name="value")
line.render("line_from_dataframe.html")
```

## 3D 散点图

```python
from pyantv import Point3D, options as opts

point3d = (
    Point3D()
    .set_data(data=[
        {"x": 1, "y": 2, "z": 3},
        {"x": 4, "y": 5, "z": 6},
    ])
    .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
    .set_coordinate(opts.CoordinateCartesian3DOpts())
)
point3d.render("point3d_chart.html")
```

## Web 框架集成

### Flask

```python
from flask import Flask
from pyantv import Line
from pyantv.web import make_response

app = Flask(__name__)

@app.route("/chart")
def chart_view():
    line = (
        Line()
        .set_data(data=[{"x": 1, "y": 2}])
        .set_encode(x_field_name="x", y_field_name="y")
    )
    return make_response(line)
```

### Streamlit

```python
import streamlit as st
from pyantv import Line
from pyantv.web import st_pyantv

line = (
    Line()
    .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
    .set_encode(x_field_name="x", y_field_name="y")
)
st_pyantv(line, height=400)
```

## 插件系统

```python
from pyantv import Interval

# 手绘风格
chart = Interval().set_data(data=[...]).use_rough(roughness=2.0)

# 切换渲染器
chart = Interval().set_data(data=[...]).use_renderer("svg")
```

## 标注系统

```python
from pyantv import Line, options as opts

line = (
    Line()
    .set_data(data=[...])
    .set_encode(x_field_name="x", y_field_name="y")
    .set_annotations([
        opts.LineAnnotationOpts(y=100, text="目标线"),
        opts.RegionAnnotationOpts(
            x_start="Q2", x_end="Q3",
            fill="rgba(255,0,0,0.1)"
        ),
    ])
)
```

## 主题系统

```python
from pyantv import Line
from pyantv.globals import ThemeType

# 使用内置暗色主题
line = (
    Line()
    .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
    .set_encode(x_field_name="x", y_field_name="y")
    .set_theme(ThemeType.DARK)
)
line.render("dark_theme.html")
```

内置主题：`ThemeType.CLASSIC`（默认）、`ThemeType.DARK`（暗色）、`ThemeType.ACADEMY`（学术）

## 数据变换

```python
from pyantv import Interval, options as opts

# 堆叠柱状图
bar = (
    Interval()
    .set_data(data=[
        {"city": "北京", "type": "食品", "value": 100},
        {"city": "北京", "type": "服装", "value": 80},
        {"city": "上海", "type": "食品", "value": 120},
        {"city": "上海", "type": "服装", "value": 90},
    ])
    .set_encode(x_field_name="city", y_field_name="value", color_field="type")
    .set_transform(opts.StackYOpts())
)
bar.render("stacked_bar.html")
```

常用变换：`StackYOpts`（堆叠）、`GroupXOpts`（分组）、`NormalizeYOpts`（归一化）、`SortXOpts`（排序）、`JitterOpts`（抖动）

## 更多图表类型

### 饼图（极坐标 + Interval）

```python
from pyantv import Interval, options as opts

pie = (
    Interval()
    .set_data(data=[
        {"type": "分类A", "value": 27},
        {"type": "分类B", "value": 25},
        {"type": "分类C", "value": 18},
    ])
    .set_encode(y_field_name="value", color_field="type")
    .set_transform(opts.StackYOpts())
    .set_coordinate(opts.CoordinatePolarOpts())
)
pie.render("pie_chart.html")
```

### 面积图

```python
from pyantv import Area

area = (
    Area()
    .set_data(data=[
        {"year": "2020", "value": 3},
        {"year": "2021", "value": 4},
        {"year": "2022", "value": 3.5},
    ])
    .set_encode(x_field_name="year", y_field_name="value")
    .set_style(opts.BaseChartStyleOpts(fill="steelblue", opacity=0.5))
)
area.render("area_chart.html")
```

### 水波图

```python
from pyantv import Liquid

liquid = Liquid().set_data(data=0.65)
liquid.render("liquid_chart.html")
```

## 导出为图片

```python
from pyantv import Line

line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
line.save_as_image("chart.png", width=1200, height=800)
```

> 需要安装 Playwright：`pip install playwright && playwright install chromium`

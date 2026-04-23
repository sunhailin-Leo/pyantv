<h1 align="center">pyantv</h1>
<p align="center">
    <em>Python ❤️ AntV = pyantv</em>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/python-app.yml/badge.svg" alt="CI Status">
    </a>
    <a href="https://github.com/sunhailin-Leo/pyantv/actions/workflows/docs-deploy.yml">
        <img src="https://github.com/sunhailin-Leo/pyantv/actions/workflows/docs-deploy.yml/badge.svg" alt="Docs Deploy Status">
    </a>
    <a href="https://codecov.io/gh/sunhailin-Leo/pyantv">
        <img src="https://codecov.io/gh/sunhailin-Leo/pyantv/branch/master/graph/badge.svg" alt="Codecov">
    </a>
</p>
<p align="center">
    <a href="https://github.com/sunhailin-Leo/pyantv/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
    <a href="https://colab.research.google.com/github/sunhailin-Leo/pyantv/blob/main/notebooks/quickstart.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
    </a>
    <a href="https://mybinder.org/v2/gh/sunhailin-Leo/pyantv/main?labpath=notebooks/quickstart.ipynb">
        <img src="https://mybinder.org/badge_logo.svg" alt="Binder">
    </a>
</p>

[中文 README](README.md) | [English README](README.en.md) | [日本語（にほんご）README](README.jp.md)

## 📣 简介

[AntV](https://github.com/antvis) 是蚂蚁集团推出的一套数据可视化解决方案，专注于 Web 数据可视化领域。它基于它基于可视化语法库 AntV Design 和渲染引擎 G 进行封装，在满足数据呈现的同时，还支持面向叙事场景的动画编排、丰富的交互能力和定制化的图表风格，简单易用的配置大大降低了用户的学习成本。而 Python 是一门富有表达力的语言，非常适合用于数据处理、AI 等场景。当数据分析，建模遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts)、[py-vchart](https://github.com/VisActor/py-vchart) 和 [py-antv](https://github.com/sunhailin-Leo/pyantv) 诞生了。

## ✨ 特性

* [pyecharts](https://github.com/pyecharts/pyecharts) like 的 API 设计，使用如丝滑般流畅，支持链式调用
* 囊括了 AntV G2 的大部分图表（后续兼容 AntV G2 的更多图表以及 AntV 生态的其他图表）
* 支持主流 Notebook 环境，Jupyter Notebook、JupyterLab
* 可轻松集成至 Flask、Sanic、Django、Streamlit 等主流 Web 框架
* 支持 3D 图表（Point3D、Line3D、Interval3D）
* 内置插件系统，支持渲染器切换（Canvas/SVG/WebGL）、手绘风格（Rough）、Lottie 动画
* 支持 pandas DataFrame / numpy ndarray 直接作为数据源
* 标注系统：参考线、区域标注、文本标注
* 图表导出：支持导出为 PNG 图片（基于 Playwright）
* 输入校验：传入错误参数时给出清晰的错误提示
* 高度灵活的配置项，可轻松搭配出精美的图表
* 详细的文档和示例，帮助开发者更快的上手项目（[在线文档](https://sunhailin-Leo.github.io/pyantv)）
* 🆕 **快捷出图**：`from_data()` / `from_dataframe()` 一行代码即可创建图表，自动推断编码字段
* 🆕 **事件系统**：90+ 个 G2 事件常量 + `set_events()` Pythonic API，轻松绑定交互事件
* 🆕 **预设系统**：31 个开箱即用的 Preset 函数（主题、动画、布局、坐标系、交互、数据转换、格式化）
* 🆕 **交互预设**：`with_element_highlight()`、`with_brush_filter()`、`with_fisheye()` 等一行启用交互
* 🆕 **数据转换预设**：`with_stack()`、`with_normalize()`、`with_sort_by()` 等一行应用数据变换
* 🆕 **自定义主题**：科技风、商务风、清新风三套内置主题 + 数据格式化函数
* 🆕 **快捷方法**：`set_title()`、`set_padding()`、`set_size()` 简化常用配置
* 🆕 **高级图表封装**：Funnel 漏斗图、WaterFall 瀑布图、Bullet 子弹图，开箱即用

### 📊 图表画廊

![Gallery Preview](docs/assets/gallery_preview.png)

## 🔰 安装

**pip 安装**
```shell
# 安装
$ pip install pyantv -U
```

**源码安装（推荐使用 uv）**
```shell
# 源码安装
$ git clone https://github.com/sunhailin-Leo/pyantv
$ cd pyantv

# 推荐：使用 uv（与 CI 同构，自动管理 lock 文件）
$ make uv-install

# 或：使用 pip fallback（PEP 517 编辑安装）
$ pip install -e '.[dev,test,all]'
```

> 自 Sprint 62 起，pyantv 以 `pyproject.toml` 作为依赖唯一来源；自 Sprint 72 起，版本号通过 `setuptools-scm` + git tag 自动派生，无需手动维护。

## 🚀 快速开始

### 基础折线图

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

### 分组柱状图

```python
from pyantv import Interval

interval = (
    Interval()
    .set_data(data=[
        {"city": "北京", "month": "Jan", "value": 12},
        {"city": "北京", "month": "Feb", "value": 15},
        {"city": "上海", "month": "Jan", "value": 10},
        {"city": "上海", "month": "Feb", "value": 14},
    ])
    .set_encode(
        x_field_name="month",
        y_field_name="value",
        color_field="city",
    )
    .set_global_options(is_auto_fit=True)
)
interval.render("bar_chart.html")
```

### 在 Jupyter Notebook 中使用

```python
from pyantv import Line

line = Line()
line.set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
line.set_encode(x_field_name="x", y_field_name="y")
line.render_notebook()
```

> 更多示例请参考 [examples/](examples/) 目录，包含 440+ 个完整示例。

### 快捷出图（from_data / from_dataframe）

```python
from pyantv import Line

# 一行代码创建图表
chart = Line.from_data(
    data=[{"year": "2020", "value": 3}, {"year": "2021", "value": 4}],
    x_field_name="year",
    y_field_name="value",
)
chart.render("quick_line.html")
```

```python
import pandas as pd
from pyantv import Line

df = pd.DataFrame({"year": ["2020", "2021", "2022"], "value": [3, 4, 5]})

# 自动推断 x/y 编码字段
chart = Line.from_dataframe(df)
chart.render("line_from_dataframe.html")
```

### 事件绑定

```python
from pyantv import Line
from pyantv.globals import ChartEvent

line = (
    Line()
    .set_data(data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}])
    .set_encode(x_field_name="x", y_field_name="y")
    .set_events({
        ChartEvent.ELEMENT_CLICK: "(ev) => { console.log('clicked:', ev.data); }",
    })
)
line.render("event_bindling.html")
```

### 预设主题

```python
from pyantv import Line
from pyantv.presets import with_dark_theme, with_auto_fit, with_smooth_animation

chart = Line.from_data(
    data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}],
    x_field_name="x", y_field_name="y",
)
with_dark_theme(chart)
with_auto_fit(chart)
with_smooth_animation(chart)
chart.render("preset_chart.html")
```

### 高级图表封装

```python
from pyantv import Funnel, WaterFall, Bullet

# 漏斗图
funnel = (
    Funnel()
    .set_data(data=[
        {"stage": "浏览", "value": 100},
        {"stage": "加购", "value": 60},
        {"stage": "下单", "value": 30},
    ])
    .set_encode(x_field_name="stage", y_field_name="value")
)
funnel.render("funnel.html")

# 瀑布图
waterfall = (
    WaterFall()
    .set_data(data=[
        {"category": "收入", "value": 120},
        {"category": "支出", "value": -40},
        {"category": "利润", "value": 80},
    ])
    .set_encode(x_field_name="category", y_field_name="value")
)
waterfall.render("waterfall.html")
```

### pandas DataFrame 数据源

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

### 3D 散点图

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

### Web 框架集成

**Flask**

```python
from flask import Flask
from pyantv import Line
from pyantv.web import make_response

app = Flask(__name__)

@app.route("/chart")
def chart_view():
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return make_response(line)
```

**Django**

```python
from django.http import HttpResponse
from pyantv import Line
from pyantv.web import render_chart_to_html

def chart_view(request):
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return HttpResponse(render_chart_to_html(line))
```

**Sanic**

```python
from sanic import Sanic
from sanic.response import html
from pyantv import Line
from pyantv.web import render_chart_to_html

app = Sanic("ChartApp")

@app.route("/chart")
async def chart_view(request):
    line = Line().set_data(data=[{"x": 1, "y": 2}]).set_encode(x_field_name="x", y_field_name="y")
    return html(render_chart_to_html(line))
```

### 插件系统

```python
from pyantv import Interval

# 手绘风格
chart = Interval().set_data(data=[...]).use_rough(roughness=2.0)

# 切换渲染器
chart = Interval().set_data(data=[...]).use_renderer("svg")
```

### 标注系统

```python
from pyantv import Line, options as opts

line = (
    Line()
    .set_data(data=[
        {"month": "Jan", "value": 80},
        {"month": "Feb", "value": 120},
        {"month": "Mar", "value": 95},
    ])
    .set_encode(x_field_name="month", y_field_name="value")
    .set_annotations([
        opts.LineAnnotationOpts(y=100, text="目标线"),
        opts.RegionAnnotationOpts(x_start="Feb", x_end="Mar", fill="rgba(255,0,0,0.1)"),
    ])
)
line.render("annotation_chart.html")
```

### Streamlit 集成

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

### 图表导出

```python
from pyantv import Line

line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")

# 导出为 PNG 图片（需要安装 playwright）
line.save_as_image("chart.png", width=1200, height=800)
```

> 需要安装 Playwright：`pip install playwright && playwright install chromium`

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -e '.[test]'
$ make test          # 运行全量单元测试 + 覆盖率
$ make lint          # 运行 flake8 代码检查
$ make check         # lint + test 的组合
```

### 集成测试

使用 Github Actions 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 😉 Author

pyantv 主要由以下几位开发者开发维护

* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

## 💡 贡献

期待能有更多的开发者参与到 pyantv 的开发中来，我们会保证尽快 Reivew PR 并且及时回复。但提交 PR 请确保

1. 通过所有单元测试，如若是新功能，请为其新增单元测试
2. 遵守开发规范，使用 black 以及 isort 格式化代码（$ pip install -r requirements-dev.txt）
3. 如若需要，请更新相对应的文档

我们也非常欢迎开发者能为 pyantv 提供更多的示例。完整文档请参阅 [docs/](docs/) 目录或在线文档站：<https://sunhailin-Leo.github.io/pyantv>；首次贡献可参考 [docs/good-first-issues.md](docs/good-first-issues.md)。

## 📃 License

MIT [©sunhailin-Leo](https://github.com/sunhailin-Leo)
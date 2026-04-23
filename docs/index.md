# pyantv

**Python ❤️ AntV = pyantv**

pyantv 是一个基于 [AntV G2](https://g2.antv.antgroup.com/) 的 Python 数据可视化库，提供流畅的链式 API，让你用 Python 轻松创建精美的交互式图表。

## 特性

- 🎨 **丰富的图表类型** — 44 种图表，覆盖统计、分布、关系、地理、特殊、3D、组合及基础标记 8 大类
- 🔗 **链式 API** — pyecharts 风格的流畅接口，代码简洁优雅
- ⚡ **快捷出图** — `from_data()` / `from_dataframe()` 一行代码出图，自动推断编码字段
- 🎁 **Preset 系统** — 31 个预设函数（主题 / 动画 / 布局 / 坐标系 / 交互 / 转换 / 格式化）
- 🎯 **事件系统** — `ChartEvent` 90+ 个 G2 事件常量 + `set_events()` Pythonic 绑定
- 📊 **pandas 集成** — 直接传入 DataFrame / Series / numpy ndarray 作为数据源
- 🌐 **Web 框架集成** — Flask、Django、Sanic、Streamlit 一键集成
- 🎭 **插件系统** — 渲染器切换（Canvas/SVG/WebGL）、手绘风格（Rough）、Lottie 动画
- 📓 **Notebook 深度集成** — Jupyter / JupyterLab / Google Colab / VS Code Notebook 原生渲染（`_repr_html_`）
- 📦 **离线资源** — `pyantv.offline` 模块支持内网部署，预置 G2 5.2.11 等资源
- 🚀 **大数据性能** — 内置 LTTB / uniform / random 三种降采样算法 + compact JSON 序列化（HTML 体积减少 ≥40%）
- 🖼️ **图表导出** — `save_as_image()` / `save_as_svg()` 基于 Playwright 一键导出 PNG / SVG

## 安装

```bash
pip install pyantv -U

# 按需启用可选特性
pip install 'pyantv[pandas]'    # DataFrame 支持
pip install 'pyantv[notebook]'  # Jupyter 深度集成
pip install 'pyantv[export]'    # PNG/SVG 导出
pip install 'pyantv[offline]'   # 离线资源下载
pip install 'pyantv[all]'       # 一次安装全部用户向特性
```

## 快速示例

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
)
line.render("chart.html")
```

或使用一行式快捷出图：

```python
from pyantv import Line

chart = Line.from_data(
    data=[{"year": "2020", "value": 3}, {"year": "2021", "value": 4}],
    x_field_name="year",
    y_field_name="value",
)
chart.render("quick.html")
```

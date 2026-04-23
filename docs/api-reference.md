# API 参考

> 本页覆盖 pyantv 全部 44 个图表类型 + 核心方法 + 高级 API。完整章节列表见目录侧栏。

## 图表类

### 基础图表

| 类名 | 说明 | 示例 |
|------|------|------|
| `Line` | 折线图 | `Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Interval` | 柱状图 / 条形图 | `Interval().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Point` | 散点图 | `Point().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Area` | 面积图 | `Area().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Cell` | 色块图 | `Cell().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Rect` | 矩形图 | `Rect().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `HeatMap` | 热力图 | `HeatMap().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Box` | 箱形图（基础标记） | `Box().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `BoxPlot` | 箱线图（统计） | `BoxPlot().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Arc` | 弧形图 | `Arc().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Path` | 路径图 | `Path().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Range` | 范围图 | `Range().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Text` | 文本标记 | `Text().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Image` | 图片标记 | `Image().set_data(data=[...]).set_encode(x_field_name="x", src_field="src")` |
| `Vector` | 向量图 | `Vector().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Link` | 链接图 | `Link().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Polygon` | 多边形 | `Polygon().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Shape` | 自定义形状 | `Shape().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Connector` | 连接器 | `Connector().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Density` | 密度图 | `Density().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Beeswarm` | 蜂群图 | `Beeswarm().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Gauge` | 仪表盘 | `Gauge().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")` |
| `Liquid` | 水波图 | `Liquid().set_data(data=0.3)` |
| `Wordcloud` | 词云图 | `Wordcloud().set_data(data=[...]).set_encode(x_field_name="text", y_field_name="value")` |
| `Sankey` | 桑基图 | `Sankey().set_data(data={...})` |
| `TreeMap` | 矩形树图 | `TreeMap().set_data(data={...})` |
| `ForceGraph` | 力导向图 | `ForceGraph().set_data(data={...})` |
| `Pack` | 打包图 | `Pack().set_data(data={...})` |
| `Tree` | 树图 | `Tree().set_data(data={...})` |
| `Partition` | 分区图 | `Partition().set_data(data={...})` |
| `Chord` | 弦图 | `Chord().set_data(data={...})` |
| `GeoPath` | 地理路径 | `GeoPath().set_data(data={...})` |

### 高级图表封装

> 在基础图表之上封装常用业务可视化模板，开箱即用。

| 类名 | 说明 | 示例 |
|------|------|------|
| `Funnel` | 漏斗图 | `Funnel().set_data(data=[...]).set_encode(x_field_name="stage", y_field_name="value")` |
| `WaterFall` | 瀑布图 | `WaterFall().set_data(data=[...]).set_encode(x_field_name="category", y_field_name="value")` |
| `Bullet` | 子弹图 | `Bullet().set_data(data=[...]).set_encode(x_field_name="title", y_field_name="ranges")` |

### 3D 图表

| 类名 | 说明 | 示例 |
|------|------|------|
| `Point3D` | 3D 散点图 | `Point3D().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y", z_field_name="z")` |
| `Line3D` | 3D 折线图 | `Line3D().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y", z_field_name="z")` |
| `Interval3D` | 3D 柱状图 | `Interval3D().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y", z_field_name="z")` |

### 组合图表

| 类名 | 说明 |
|------|------|
| `View` | 视图容器，用于叠加多个图表 |
| `SpaceFlex` | 弹性空间布局，水平/垂直排列子图 |
| `SpaceLayer` | 图层叠加布局，多图层叠加 |
| `FacetRect` | 矩形分面，按维度拆分为网格 |
| `FacetCircle` | 圆形分面，按维度拆分为扇形 |
| `RepeatMatrix` | 重复矩阵，多维度交叉展示 |

## 核心方法详解

### `set_data(data)`

设置图表数据源。

| 参数 | 类型 | 说明 |
|------|------|------|
| `data` | `list[dict]` / `dict` / `DataFrame` / `ndarray` / `float` | 数据源 |

**支持的数据类型**：

```python
# 字典列表（最常用）
chart.set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])

# pandas DataFrame
import pandas as pd
df = pd.DataFrame({"x": [1, 2], "y": [2, 5]})
chart.set_data(data=df)

# numpy ndarray
import numpy as np
arr = np.array([[1, 2], [2, 5]])
chart.set_data(data=arr)

# 标量值（如 Liquid 水波图）
chart.set_data(data=0.3)

# Fetch 远程数据
chart.set_data(data=opts.FetchDataOpts(value="https://example.com/data.json"))
```

### `set_encode(...)`

设置视觉编码通道，将数据字段映射到视觉属性。

| 参数 | 类型 | 说明 |
|------|------|------|
| `x_field_name` | `str` / `list[str]` / `JsCode` | X 轴字段 |
| `y_field_name` | `str` / `list[str]` / `JsCode` | Y 轴字段 |
| `z_field_name` | `str` / `list[str]` / `JsCode` | Z 轴字段（3D 图表） |
| `color_field` | `str` / `list[str]` / `JsCode` | 颜色通道字段 |
| `size_field` | `str` / `JsCode` | 大小通道字段 |
| `shape_field` | `str` / `JsCode` | 形状通道字段 |
| `series_field` | `str` / `JsCode` | 系列字段（分组） |
| `opacity_field` | `str` / `JsCode` | 透明度通道字段 |
| `ext_field` | `dict` | 扩展编码通道 |

```python
chart.set_encode(
    x_field_name="year",
    y_field_name="value",
    color_field="category",
    size_field="weight",
)
```

### `set_style(style_opts)`

设置图形样式。

| 参数 | 类型 | 说明 |
|------|------|------|
| `style_opts` | `BaseChartStyleOpts` / `dict` | 样式配置 |

```python
chart.set_style(opts.BaseChartStyleOpts(fill="steelblue", opacity=0.8))
```

### `set_annotations(annotation_list)`

设置图表标注（参考线、区域标注、文本标注）。

| 参数 | 类型 | 说明 |
|------|------|------|
| `annotation_list` | `list[Annotation]` | 标注配置列表 |

```python
chart.set_annotations([
    opts.LineAnnotationOpts(y=100, text="目标线"),
    opts.RegionAnnotationOpts(x_start="Q2", x_end="Q3", fill="rgba(255,0,0,0.1)"),
    opts.TextAnnotationOpts(x="Q4", y=200, text="峰值"),
])
```

### `set_transform(transform_opts)`

设置数据变换。

| 参数 | 类型 | 说明 |
|------|------|------|
| `transform_opts` | `Transform` / `list[Transform]` | 变换配置 |

**常用变换类型**：`GroupXOpts`、`StackYOpts`、`NormalizeYOpts`、`SortXOpts`、`SortYOpts`、`JitterOpts`、`SelectOpts`

```python
chart.set_transform(opts.StackYOpts())
chart.set_transform([opts.GroupXOpts(), opts.StackYOpts()])
```

### `set_coordinate(coordinate_opts)`

设置坐标系。

| 参数 | 类型 | 说明 |
|------|------|------|
| `coordinate_opts` | `Coordinate` | 坐标系配置 |

**坐标系类型**：`CoordinatePolarOpts`（极坐标）、`CoordinateCartesian3DOpts`（3D 笛卡尔）、`CoordinateHelixOpts`（螺旋）

```python
# 极坐标（饼图/环形图）
chart.set_coordinate(opts.CoordinatePolarOpts(inner_radius=0.5))

# 3D 笛卡尔坐标
chart.set_coordinate(opts.CoordinateCartesian3DOpts())
```

### `set_theme(theme)`

设置图表主题。

| 参数 | 类型 | 说明 |
|------|------|------|
| `theme` | `str` / `dict` | 主题名称或自定义主题字典 |

**内置主题**：`ThemeType.CLASSIC`、`ThemeType.DARK`、`ThemeType.ACADEMY`

```python
from pyantv.globals import ThemeType
chart.set_theme(ThemeType.DARK)
```

### `set_global_options(...)`

一次性设置多个全局配置项。

| 参数 | 类型 | 说明 |
|------|------|------|
| `width` | `int` | 图表宽度 |
| `height` | `int` | 图表高度 |
| `is_auto_fit` | `bool` | 是否自适应容器 |
| `transform_opts` | `Transform` | 数据变换 |
| `coordinate_opts` | `Coordinate` | 坐标系 |
| `style_opts` | `BaseChartStyle` | 样式 |
| `animate_opts` | `Animate` | 动画 |
| `tooltip_opts` | `Tooltip` | 提示框 |
| `axis_opts` | `Axis` | 坐标轴 |
| `legend_opts` | `Legend` | 图例 |
| `label_opts` | `Label` | 标签 |
| `title_opts` | `Title` | 标题 |

```python
chart.set_global_options(
    width=800,
    height=600,
    is_auto_fit=True,
    title_opts=opts.TitleOpts(title="销售趋势"),
    tooltip_opts=opts.TooltipOpts(),
)
```

### 快捷构造（类方法）

> Sprint 50+ 引入的一行式构造方法，自动推断编码字段，适合快速出图。

| 方法 | 签名 | 说明 |
|------|------|------|
| `Chart.from_data(data, x_field_name=None, y_field_name=None, color_field=None, size_field=None, shape_field=None, series_field=None)` | 返回 `Chart` | 一行从数据构造图表，编码字段以具名参数方式传入 |
| `Chart.from_dataframe(dataframe, x_field_name=None, y_field_name=None, color_field=None, size_field=None, shape_field=None, series_field=None)` | 返回 `Chart` | 从 pandas DataFrame 构造；NaN/NaT 自动转 None；需安装 pandas，否则抛 `ImportError` |

```python
from pyantv import Line
chart = Line.from_data(
    data=[{"year": "2020", "value": 3}, {"year": "2021", "value": 4}],
    x_field_name="year", y_field_name="value",
)
```

### 快捷配置方法

> 简化常用全局配置，与 `set_global_options(...)` 等价但更直观。

| 方法 | 签名 | 说明 |
|------|------|------|
| `set_title(text=None, subtitle=None, align=None)` | `(str|None, str|None, str|None) -> self` | 设置标题 / 副标题 / 对齐方式 |
| `set_padding(top=None, right=None, bottom=None, left=None)` | 全部 `Optional[Numeric]` | 设置画布四向内边距，仅传入非 None 的值生效 |
| `set_size(width=None, height=None, is_auto_fit=None)` | `(Numeric|None, Numeric|None, bool|None) -> self` | 设置宽高与自适应（参数名为 `is_auto_fit`） |

### 事件系统

> Sprint 51 引入。绑定 G2 v5 原生事件，支持 90+ 个事件常量。

| 方法 | 签名 | 说明 |
|------|------|------|
| `set_events(events_dict)` | `(dict[str, str|JsCode]) -> self` | 批量绑定事件回调 |

```python
from pyantv import Line
from pyantv.globals import ChartEvent  # 也可从 pyantv 顶层直接导入

chart = (
    Line.from_data(data=[...], x_field_name="x", y_field_name="y")
    .set_events({
        ChartEvent.ELEMENT_CLICK: "(ev) => { console.log('clicked:', ev.data); }",
        ChartEvent.PLOT_POINTER_MOVE: "(ev) => { console.log('hover at', ev.x, ev.y); }",
    })
)
```

完整事件常量见 `pyantv.globals.ChartEvent`（涵盖 element / plot / legend / axis / brush / tooltip 等 90+ 事件）。

### 渲染与导出

| 方法 | 参数 | 说明 |
|------|------|------|
| `render(path, compact=False)` | `path: str = "render.html"`, `compact: bool = False` | 渲染为 HTML 文件，`compact=True` 可减少 ≥40% 体积 |
| `render_embed(compact=False)` | — | 渲染为 HTML 字符串 |
| `render_notebook()` | — | 在 Jupyter Notebook 中显式渲染（推荐直接放置图表对象，依赖 `_repr_html_`） |
| `_repr_html_()` | — | Jupyter / IPython 自动调用，cell 末位置图表对象即可内联渲染 |
| `save_as_image(path, width=1200, height=800)` | `path: str` | 导出为 PNG 图片（Playwright） |
| `save_as_svg(path, width=1200, height=800)` | `path: str` | 导出为 SVG 矢量图（Playwright） |
| `dump_options(compact=False)` | `compact: bool` | 序列化图表配置为 JSON 字符串，`compact=True` 时无缩进无空格 |

### 插件方法

| 方法 | 参数 | 说明 |
|------|------|------|
| `use_renderer(type)` | `renderer_type: str`（canvas/svg/webgl） | 切换渲染器 |
| `use_rough(roughness, bowing)` | `roughness: float = 1.0`, `bowing: float = 1.0` | 启用手绘风格 |
| `use_lottie(autoplay)` | `autoplay: bool = True` | 启用 Lottie 动画 |

## 标注选项类

| 类名 | 说明 | 关键参数 |
|------|------|----------|
| `LineAnnotationOpts` | 参考线 | `x`/`y`（位置）、`text`（标签）、`style`（样式） |
| `RegionAnnotationOpts` | 区域标注 | `x_start`/`x_end`/`y_start`/`y_end`（范围）、`fill`（填充色） |
| `TextAnnotationOpts` | 文本标注 | `x`/`y`（位置）、`text`（内容）、`style`（样式） |

## Notebook 集成

> Sprint 73 深度集成。详见 [Notebook 使用指南](notebook-guide.md)。

| 函数 / 方法 | 模块 | 说明 |
|------|------|------|
| `notebook_config(width, height, theme)` | `pyantv.render.notebook` | 全局配置 notebook 渲染参数（width / height / theme） |
| `Chart._repr_html_()` | `pyantv.charts.base` | IPython 自动调用，cell 末放置图表即可内联显示 |

```python
from pyantv import Line
from pyantv.render.notebook import notebook_config

notebook_config(width="80%", height="400px", theme="dark")
chart = Line.from_data(data=[{"x": 1, "y": 2}], x_field_name="x", y_field_name="y")
chart  # cell 末，自动 inline 渲染
```

## Preset 系统

> Sprint 47-50 引入，31 个预设函数，详见 [Presets 总览](presets/index.md)。

| 分类 | 代表函数 |
|------|----------|
| 主题 | `with_dark_theme` / `with_classic_theme` / `with_academy_theme` / `with_tech_theme` / `with_business_theme` / `with_fresh_theme` |
| 动画 | `with_smooth_animation` |
| 布局 | `with_auto_fit` / `with_legend_hidden` / `with_axis_hidden` / `with_labels` / `with_padding` |
| 坐标系 | `with_transpose` / `with_polar` |
| 交互 | `with_tooltip` / `with_element_highlight` / `with_element_select` / `with_brush_highlight` / `with_brush_filter` / `with_fisheye` / `with_slider_filter` |
| 数据转换 | `with_sort_by` / `with_stack` / `with_normalize` / `with_group` / `with_jitter` |
| 格式化 | `format_number` / `format_percent` / `format_currency` / `format_date` |
| 批量工具 | `batch_export_png` |

## 离线资源（pyantv.offline）

> Sprint 63 引入，用于在内网 / 离线环境下使用 pyantv。

| 函数 / 类 | 说明 |
|------|------|
| `install_assets(target_dir=None, libs=None, version_map=None, use_cache=True)` | 一键下载 AntV 前端资源到本地（默认目录 `~/.pyantv/assets`），返回 `{lib_name: local_path}` |
| `set_offline_host(host)` | 设置离线 host，优先于在线 CDN（支持 `file://` 协议） |
| `get_active_host()` | 获取当前生效的 host（优先级：`OFFLINE_HOST` > 环境变量 `PYANTV_OFFLINE_HOST` > `ONLINE_HOST`） |
| `AssetRegistry` | 资源注册表（类方法 `register` / `get` / `list_registered` / `unregister`），默认注册 G2 5.2.11 |
| `OfflineInstallError` | 下载失败时抛出的异常类型 |

## 大数据降采样（pyantv.commons.utils）

> Sprint 64 引入，支持百万级数据点的高性能渲染。

| 函数 / 方法 | 说明 |
|------|------|
| `downsample(data, max_points, method="lttb", x_field=None, y_field=None, random_state=None)` | 降采样到 `max_points`：`lttb`（默认，保留形状特征）/ `uniform`（时序稳定）/ `random`（支持 `random_state` 重现），位于 `pyantv.data.pipeline` |
| `Chart.set_data(data, sample_if_large=None, sample_method="lttb", sample_x_field=None, sample_y_field=None)` | `set_data` 内置降采样开关，当 `sample_if_large` 为 int 且数据点数超过该阈值时自动调用 `downsample` 并发出 `UserWarning`（默认 `None` 不采样） |

## Web 集成

| 函数 | 模块 | 说明 |
|------|------|------|
| `make_response(chart)` | `pyantv.web` | 生成 Flask Response |
| `render_chart_to_html(chart)` | `pyantv.web` | 生成 HTML 字符串 |
| `st_pyantv(chart, height, width)` | `pyantv.web` | Streamlit 组件 |

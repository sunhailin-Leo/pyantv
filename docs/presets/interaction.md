# 交互 Presets

交互 Presets 增强图表的用户交互能力，让用户能够通过鼠标操作探索数据。

## with_tooltip

应用标准 tooltip 配置，在鼠标悬停时显示数据详情。

**函数签名：**
```python
def with_tooltip(chart, shared=True, show_crosshairs=False)
```

**参数：**
- `chart` (Chart): 图表实例
- `shared` (bool, 可选): 是否共享 tooltip（多系列时显示所有系列数据），默认 `True`
- `show_crosshairs` (bool, 可选): 是否显示十字准线，默认 `False`

**返回：** 应用 tooltip 后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_tooltip

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 默认配置（共享 tooltip，无十字准线）
with_tooltip(chart)

# 启用十字准线
with_tooltip(chart, show_crosshairs=True)

# 不共享 tooltip（仅显示当前系列）
with_tooltip(chart, shared=False)

chart.render("tooltip.html")
```

---

## with_element_highlight

启用元素高亮交互，鼠标悬停时高亮当前元素，其他元素变暗。

**函数签名：**
```python
def with_element_highlight(chart, background=False)
```

**参数：**
- `chart` (Chart): 图表实例
- `background` (bool, 可选): 是否显示高亮背景，默认 `False`

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_element_highlight

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 基本高亮（无背景）
with_element_highlight(chart)

# 带背景的高亮
with_element_highlight(chart, background=True)

chart.render("element_highlight.html")
```

---

## with_element_select

启用元素选中交互，点击选中元素，保持高亮状态。

**函数签名：**
```python
def with_element_select(chart, background=False)
```

**参数：**
- `chart` (Chart): 图表实例
- `background` (bool, 可选): 是否显示选中背景，默认 `False`

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_element_select

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 基本选中（无背景）
with_element_select(chart)

# 带背景的选中
with_element_select(chart, background=True)

chart.render("element_select.html")
```

---

## with_brush_highlight

启用框选高亮交互，拖拽框选区域内的元素高亮，区域外的元素变暗。

**函数签名：**
```python
def with_brush_highlight(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Scatter
from pyantv.presets import with_brush_highlight

chart = Scatter.from_data(data=data, x_field_name="x", y_field_name="y")

with_brush_highlight(chart)

chart.render("brush_highlight.html")
```

---

## with_brush_filter

启用框选过滤交互，拖拽框选区域外的元素隐藏，仅显示区域内的元素。

**函数签名：**
```python
def with_brush_filter(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Scatter
from pyantv.presets import with_brush_filter

chart = Scatter.from_data(data=data, x_field_name="x", y_field_name="y")

with_brush_filter(chart)

chart.render("brush_filter.html")
```

---

## with_fisheye

启用鱼眼放大镜交互，鼠标悬停时放大局部区域。

**函数签名：**
```python
def with_fisheye(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Scatter
from pyantv.presets import with_fisheye

chart = Scatter.from_data(data=data, x_field_name="x", y_field_name="y")

with_fisheye(chart)

chart.render("fisheye.html")
```

---

## with_slider_filter

启用滑块过滤交互，通过滑块筛选数据范围。

**函数签名：**
```python
def with_slider_filter(chart, x_axis=True, y_axis=False)
```

**参数：**
- `chart` (Chart): 图表实例
- `x_axis` (bool, 可选): 是否在 x 轴启用滑块，默认 `True`
- `y_axis` (bool, 可选): 是否在 y 轴启用滑块，默认 `False`

**返回：** 应用交互后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_slider_filter

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 仅在 x 轴启用滑块
with_slider_filter(chart)

# 在 x 轴和 y 轴都启用滑块
with_slider_filter(chart, x_axis=True, y_axis=True)

# 仅在 y 轴启用滑块
with_slider_filter(chart, x_axis=False, y_axis=True)

chart.render("slider_filter.html")
```

## 交互类型对比

| Preset | 交互类型 | 触发方式 | 适用场景 |
|--------|---------|---------|---------|
| `with_tooltip` | 提示框 | 鼠标悬停 | 查看数据详情 |
| `with_element_highlight` | 元素高亮 | 鼠标悬停 | 突出显示当前元素 |
| `with_element_select` | 元素选中 | 鼠标点击 | 持续高亮选中元素 |
| `with_brush_highlight` | 框选高亮 | 拖拽框选 | 局部数据探索 |
| `with_brush_filter` | 框选过滤 | 拖拽框选 | 数据筛选 |
| `with_fisheye` | 鱼眼放大 | 鼠标悬停 | 局部细节查看 |
| `with_slider_filter` | 滑块过滤 | 滑块拖动 | 范围筛选 |

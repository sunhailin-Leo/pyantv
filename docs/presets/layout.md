# 布局 Presets

布局 Presets 控制图表的容器自适应、图例、坐标轴和内边距等布局相关配置。

## with_auto_fit

启用自适应容器大小，使图表随窗口大小自动调整。

**函数签名：**
```python
def with_auto_fit(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用自适应后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_auto_fit

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_auto_fit(chart)
chart.render("auto_fit.html")
```

---

## with_legend_hidden

隐藏图例，适用于图例信息冗余或需要节省空间的场景。

**函数签名：**
```python
def with_legend_hidden(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 隐藏图例后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_legend_hidden

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_legend_hidden(chart)
chart.render("no_legend.html")
```

---

## with_axis_hidden

隐藏所有坐标轴（包括 x 轴和 y 轴），适用于极简风格或数据标签已充分展示的场景。

**函数签名：**
```python
def with_axis_hidden(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 隐藏坐标轴后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_axis_hidden

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")
with_axis_hidden(chart)
chart.render("no_axis.html")
```

---

## with_padding

应用统一内边距，控制图表内容与容器边缘的距离。

**函数签名：**
```python
def with_padding(chart, top=20, right=20, bottom=20, left=20)
```

**参数：**
- `chart` (Chart): 图表实例
- `top` (int, 可选): 上内边距，默认 `20`
- `right` (int, 可选): 右内边距，默认 `20`
- `bottom` (int, 可选): 下内边距，默认 `20`
- `left` (int, 可选): 左内边距，默认 `20`

**返回：** 应用内边距后的图表实例

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_padding

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 使用默认内边距（四周均为 20）
with_padding(chart)

# 为坐标轴标签预留更多空间
with_padding(chart, top=20, right=20, bottom=50, left=60)

# 极简风格，减少内边距
with_padding(chart, top=10, right=10, bottom=10, left=10)

chart.render("padding.html")
```

**内边距建议：**

| 场景 | 上 | 右 | 下 | 左 | 说明 |
|------|----|----|----|----|------|
| 标准图表 | 20 | 20 | 40 | 60 | y 轴标签需要更多空间 |
| 无坐标轴 | 10 | 10 | 10 | 10 | 极简风格 |
| 大字号标签 | 30 | 20 | 60 | 80 | 为大标签预留空间 |
| 数据大屏 | 40 | 40 | 60 | 80 | 大屏幕需要更多留白 |

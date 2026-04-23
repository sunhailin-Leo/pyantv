# 数据转换 Presets

数据转换 Presets 对数据进行排序、堆叠、归一化、分组、抖动等预处理操作。

## with_sort_by

应用排序数据转换，按指定字段对数据进行排序。

**函数签名：**
```python
def with_sort_by(chart, field, order="ascending")
```

**参数：**
- `chart` (Chart): 图表实例
- `field` (str): 排序字段名
- `order` (str, 可选): 排序方向，`"ascending"`（升序）或 `"descending"`（降序），默认 `"ascending"`

**返回：** 应用排序后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_sort_by

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 按 y 字段升序排序
with_sort_by(chart, field="y", order="ascending")

# 按 y 字段降序排序
with_sort_by(chart, field="y", order="descending")

chart.render("sorted.html")
```

---

## with_stack

应用堆叠数据转换，适用于堆叠柱状图、堆叠面积图等。

**函数签名：**
```python
def with_stack(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用堆叠后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_stack

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value", color_field_name="type")

with_stack(chart)

chart.render("stacked.html")
```

---

## with_normalize

应用归一化数据转换，将堆叠数据转换为百分比形式，适用于百分比堆叠图。

**函数签名：**
```python
def with_normalize(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用归一化后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_normalize

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value", color_field_name="type")

with_normalize(chart)

chart.render("normalized.html")
```

---

## with_group

应用分组数据转换，将数据按指定通道分组并排显示。

**函数签名：**
```python
def with_group(chart, channels=None)
```

**参数：**
- `chart` (Chart): 图表实例
- `channels` (list, 可选): 分组通道列表，默认 `["x"]`

**返回：** 应用分组后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_group

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value", color_field_name="type")

# 默认按 x 通道分组
with_group(chart)

# 自定义分组通道
with_group(chart, channels=["x"])

chart.render("grouped.html")
```

---

## with_jitter

应用抖动数据转换，为数据点添加随机偏移，避免数据点重叠。

**函数签名：**
```python
def with_jitter(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用抖动后的图表实例

**示例：**
```python
from pyantv import Point
from pyantv.presets import with_jitter

chart = Point.from_data(data=data, x_field_name="category", y_field_name="value")

with_jitter(chart)

chart.render("jittered.html")
```

## 数据转换对比

| Preset | 转换类型 | 适用图表 | 典型场景 |
|--------|---------|---------|---------|
| `with_sort_by` | 排序 | Interval, Line, Area | 按值排序展示 |
| `with_stack` | 堆叠 | Interval, Area | 多系列堆叠对比 |
| `with_normalize` | 归一化 | Interval, Area | 百分比堆叠对比 |
| `with_group` | 分组 | Interval, Point | 多系列并排对比 |
| `with_jitter` | 抖动 | Point | 避免数据点重叠 |

## 转换组合

数据转换可以组合使用：

```python
from pyantv import Interval
from pyantv.presets import with_stack, with_normalize

# 创建百分比堆叠图
chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value", color_field_name="type")
with_stack(chart)
with_normalize(chart)
chart.render("percent_stacked.html")
```

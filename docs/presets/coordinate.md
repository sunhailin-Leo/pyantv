# 坐标系 Presets

坐标系 Presets 改变图表的坐标系类型，可以将柱形图变为条形图或将图表转换为极坐标形式。

## with_transpose

转置坐标系，将 x 轴和 y 轴互换。常用于将柱形图转换为条形图。

**函数签名：**
```python
def with_transpose(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 转置后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_transpose

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 将柱形图转换为条形图
with_transpose(chart)

chart.render("transpose.html")
```

**效果：**
- 原始：x 轴为类别，y 轴为数值（柱形图）
- 转置后：x 轴为数值，y 轴为类别（条形图）

---

## with_polar

应用极坐标系，将直角坐标转换为极坐标。常用于创建玫瑰图、雷达图等。

**函数签名：**
```python
def with_polar(chart)
```

**参数：**
- `chart` (Chart): 图表实例

**返回：** 应用极坐标后的图表实例

**示例：**
```python
from pyantv import Interval
from pyantv.presets import with_polar

chart = Interval.from_data(data=data, x_field_name="category", y_field_name="value")

# 将柱形图转换为玫瑰图
with_polar(chart)

chart.render("polar.html")
```

**效果：**
- 原始：直角坐标系（普通柱形图）
- 极坐标：角度代表类别，半径代表数值（玫瑰图）

## 坐标系对比

| Preset | 坐标系类型 | 适用图表 | 典型场景 |
|--------|-----------|---------|---------|
| `with_transpose` | 直角坐标（转置） | Interval, Line, Area | 横向对比、长标签展示 |
| `with_polar` | 极坐标 | Interval, Point, Line | 玫瑰图、雷达图、环形图 |

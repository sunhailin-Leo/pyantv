# FacetCircle

## 概述

环形分面（FacetCircle）组合图表。

基于 G2 的 `facetCircle` 复合视图，将子图表按 `position` 字段
沿圆周方向分面排列，常用于呈现按角度/方位分组的多组数据，
例如 24 小时分布、月份分布等。

## 配置项

- **set_facet_circle_encode(position)**: 指定分面字段，决定每个子视图在圆周上的位置
- **set_facet_circle_children(children)**: 设置子图表列表（每个子项需 `Chart.get_options()` 序列化后传入）

## 示例

```python
from pyantv import FacetCircle, Line

# 准备子图表
sub_chart = (
    Line()
    .set_data(data=[...])
    .set_encode(x_field_name="x", y_field_name="y")
)

facet = (
    FacetCircle()
    .set_facet_circle_encode(position="hour")
    .set_facet_circle_children(children=[sub_chart.get_options()])
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

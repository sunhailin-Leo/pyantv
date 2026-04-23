# FacetRect

## 概述

矩形分面（FacetRect）组合图表。

基于 G2 的 `facetRect` 复合视图，将子图表按 `x`、`y` 字段
切分为网格化的多个子视图，常用于多维交叉对比，
例如「按地区 × 按品类」的销售分布矩阵。

## 配置项

- **set_facet_rect_encode(x_field_name, y_field_name)**: 指定行/列分面字段，可传 `str` 或 `Sequence[str]`
- **set_facet_rect_children(children)**: 设置子图表列表（每个子项需 `Chart.get_options()` 序列化后传入）

## 示例

```python
from pyantv import FacetRect, Interval

sub_chart = (
    Interval()
    .set_data(data=[...])
    .set_encode(x_field_name="month", y_field_name="value")
)

facet = (
    FacetRect()
    .set_facet_rect_encode(
        x_field_name="region",
        y_field_name="category",
    )
    .set_facet_rect_children(children=[sub_chart.get_options()])
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

# View

## 概述

通用视图容器（View）组合图表。

基于 G2 的 `view` 复合视图，是组合多个子图表的最基础容器，
支持子图表列表管理以及多视图之间的 `tooltip`、`brush` 联动，
适合实现联动分析仪表盘。

## 配置项

- **set_view_children(children)**: 一次性设置所有子图表
- **add_child(chart)**: 链式追加单个子 `Chart`
- **link_tooltip(shared=True)**: 启用子视图间的 tooltip 联动
- **link_brush(brush_type="rect", shared=True)**: 启用子视图间的框选联动；`brush_type` 可选 `"rect"` / `"x"` / `"y"`

## 示例

```python
from pyantv import View, Line, Interval

line_chart = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
bar_chart = Interval().set_data(data=[...]).set_encode(x_field_name="cat", y_field_name="v")

dashboard = (
    View()
    .add_child(line_chart)
    .add_child(bar_chart)
    .link_tooltip(shared=True)
    .link_brush(brush_type="rect")
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

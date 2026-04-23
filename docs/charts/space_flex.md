# SpaceFlex

## 概述

弹性布局（SpaceFlex）组合图表。

基于 G2 的 `spaceFlex` 复合视图，将多个子图表按弹性比例
水平或垂直排列，可灵活控制每个子视图的尺寸占比，
适合搭建「主图 + 辅助小图」类的仪表盘布局。

## 配置项

- **set_space_flex_children(children)**: 一次性设置所有子图表（每个子项需 `Chart.get_options()`）
- **add_child(chart)**: 链式添加单个 `Chart` 子图表，内部会自动调用 `get_options()` 累加

## 示例

```python
from pyantv import SpaceFlex, Line, Interval

main_chart = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
side_chart = Interval().set_data(data=[...]).set_encode(x_field_name="cat", y_field_name="v")

dashboard = (
    SpaceFlex()
    .add_child(main_chart)
    .add_child(side_chart)
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

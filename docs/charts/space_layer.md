# SpaceLayer

## 概述

层叠布局（SpaceLayer）组合图表。

基于 G2 的 `spaceLayer` 复合视图，将多个子图表叠加在同一画布上，
共享坐标系空间，常用于「背景图 + 前景图」「多 Mark 叠加」等场景。
`Bullet` 子弹图就是基于 `SpaceLayer` 实现的典型案例。

## 配置项

- **set_space_layer_children(children)**: 一次性设置所有叠加层（每个子项需 `Chart.get_options()`）
- **add_child(chart)**: 链式追加单个 `Chart` 作为新的叠加层

## 示例

```python
from pyantv import SpaceLayer, Interval

background = (
    Interval()
    .set_data(data=[{"x": "A", "y": 100}])
    .set_encode(x_field_name="x", y_field_name="y")
)
foreground = (
    Interval()
    .set_data(data=[{"x": "A", "y": 70}])
    .set_encode(x_field_name="x", y_field_name="y")
)

layered = (
    SpaceLayer()
    .add_child(background)
    .add_child(foreground)
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

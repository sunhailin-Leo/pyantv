# Bullet

## 概述

子弹图高级封装类。

基于 G2 的 SpaceLayer + 多个 Interval mark 叠加实现。
构造时自动创建 range（背景范围）和 measure（实际值）两层，
可选添加 target（目标值）标记层。

用户只需通过 `set_bullet_data` 传入数据和字段名，
即可自动生成标准子弹图。

## 配置项

通过 `set_bullet_style` 调整子弹图样式，常用参数如下：

- **range_fill**: 范围背景条填充色
- **measure_fill**: 实际值前景条填充色
- **target_fill**: 目标值标记填充色
- **measure_max_width**: 实际值条最大宽度
- **target_min_width**: 目标值标记最小宽度
- **transpose**: 是否转置坐标系（水平子弹图，默认 True）
- **hide_y_axis**: 是否隐藏 Y 轴（默认 True）

## 示例

```python
from pyantv import Bullet

bullet = Bullet().set_bullet_data(
    data=[
        {"title": "Revenue", "ranges": 300,
         "actual": 270, "target": 250},
    ],
    title_field="title",
    range_field="ranges",
    measure_field="actual",
    target_field="target",
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

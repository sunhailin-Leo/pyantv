# Beeswarm

## 概述

蜂群图 Mark 类。
用于展示一维数据分布，通过力模拟避免点重叠。
基于 G2 的 beeswarm mark 实现，使用 d3-force
力模拟算法对数据点进行布局。
Examples:
>>> from pyantv import Beeswarm
>>> beeswarm = (
...     Beeswarm()
...     .set_data(data=[
...         {"value": 1, "category": "A"},
...         {"value": 2, "category": "A"},
...         {"value": 3, "category": "B"},
...     ])
...     .set_encode(x_field_name="value", y_field_name="category")
... )

## 配置项

暂无配置项说明

## 示例

```python
# 示例代码暂未添加
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

# Funnel

## 概述

漏斗图高级封装类。
基于 G2 的 interval mark + symmetryY transform + transpose coordinate
组合实现。构造时自动预置漏斗图所需的 transform、coordinate 配置，
并在 set_encode 时自动注入漏斗形状。
支持两种形状：
- funnel（默认）：标准漏斗形状
- pyramid：金字塔形状
Examples:
>>> from pyantv import Funnel
>>> funnel = (
...     Funnel()
...     .set_data(data=[
...         {"action": "浏览网站", "pv": 50000},
...         {"action": "放入购物车", "pv": 35000},
...         {"action": "生成订单", "pv": 25000},
...         {"action": "支付订单", "pv": 15000},
...         {"action": "完成交易", "pv": 8000},
...     ])
...     .set_encode(x_field_name="action", y_field_name="pv",
...                 color_field="action")
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

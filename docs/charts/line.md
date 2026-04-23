# Line

## 概述



## 配置项

暂无配置项说明

## 示例

```python
from pyantv import options as opts
from pyantv.charts import View, Line, Point


TEST_LINE_DATA = [
    {"year": "1991", "value": 3},
    {"year": "1992", "value": 4},
    {"year": "1993", "value": 3.5},
    {"year": "1994", "value": 5},
    {"year": "1995", "value": 4.9},
    {"year": "1996", "value": 6},
    {"year": "1997", "value": 7},
    {"year": "1998", "value": 9},
    {"year": "1999", "value": 13},
]

line = (
    Line()
    .set_global_options(
        label_opts=[
            opts.Lab```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

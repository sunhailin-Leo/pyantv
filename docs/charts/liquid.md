# Liquid

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import Liquid
from pyantv.globals import ChartType

from test import chart_base_test


c = (
    Liquid(
        render_opts=opts.RenderOpts(
            is_auto_fit=True,
        ),
    )
    .set_data(data=0.3)
    .set_liquid_style(
        outline_border=4,
        outline_distance=8,
        wave_length=128,
    )
)
c.render("liquid_example.html")
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

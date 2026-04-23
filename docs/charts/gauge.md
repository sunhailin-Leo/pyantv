# Gauge

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import Wordcloud, Gauge
from pyantv.globals import ChartType

from test import chart_base_test


c = (
    Gauge(
        render_opts=opts.RenderOpts(
            is_auto_fit=True,
        ),
    )
    .set_data(
        data={
            "value": {
                "target": 120,
                "total": 400,
                "name": "score",
            }
        }
    )
    .set_global_options(legend_opts=False)
)
c.render(```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

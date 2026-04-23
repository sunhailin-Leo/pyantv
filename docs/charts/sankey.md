# Sankey

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import Sankey
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


c = (
    Sankey(
        render_opts=opts.RenderOpts(
            is_auto_fit=True,
        ),
        init_opts=opts.InitOpts(
            width="900px",
            height="600px",
        ),
    )
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

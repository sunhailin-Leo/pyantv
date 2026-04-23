# BoxPlot

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import BoxPlot
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test

c = (
    BoxPlot()
    .set_data(
        data=opts.FetchDataOpts(value="https://assets.antv.antgroup.com/g2/morley.json")
    )
    .set_encode(
        x_field_name="Expt",
        y_field_name="Speed",
    )
    .set_global_options(inset=6, padding_left="60")
)

c.render("boxplot_example.html")
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

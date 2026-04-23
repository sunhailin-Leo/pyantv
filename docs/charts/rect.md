# Rect

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import View, Rect, LineX
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


rect = (
    Rect()
    .set_encode(
        x_field_name="IMDB Rating",
    )
    .set_scale(y_scale_opts=opts.ScaleLinearOpts(domain_max=1000))
    .set_global_options(
        transform_opts=[
            opts.TransformBinXOpts(
                channel_name="y",
                channel_t```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

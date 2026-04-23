# HeatMap

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import View, HeatMap, Point, Image
from pyantv.commons.utils import JsCode

from test import chart_base_test


# heatmap = (
#     HeatMap()
#     .set_data(data={
#         "transform": [
#             opts.CustomDataOpts(
#                 callback=JsCode("(data) => {const dv = new DataSet.View().source(data); dv.transform({type: 'kernel-smooth.density', fields: ['carat', 'price'], as: ['carat', 'price', 'density']}); retur```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

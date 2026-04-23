# Polygon

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import Polygon
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


transform_func = """
(data) => {
  const dv = new DataSet.View().source(data).transform({
    type: 'bin.hexagon',
    fields: ['longitude', 'latitude'],
    binWidth: [2, 3],
    as: ['longitude', 'latitude', 'count'],
  });
  return dv.rows;
}
"""


c = (
    Polygon()
    .add_js_dependencies(*["a```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

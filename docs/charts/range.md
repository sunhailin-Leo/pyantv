# Range

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from pyantv import options as opts
from pyantv.charts import View, LineX, LineY, Range, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


line_x = LineX().set_data(data=[0])

line_y = LineY().set_data(data=[0])

range_ = (
    Range()
    .set_data(
        data=[
            {"x": [-25, 0], "y": [-30, 0], "region": "1"},
            {"x": [-25, 0], "y": [0, 20], "region": "2"},
            {"x": [0, 5], "y": [```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

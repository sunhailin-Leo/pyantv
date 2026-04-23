# Tree

## 概述



## 配置项

暂无配置项说明

## 示例

```python
import unittest

from simplejson import JSONEncoder

from pyantv import options as opts
from pyantv.charts import Tree
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class CustomJSONEncoder(JSONEncoder):
    def encode(self, obj):
        # 调用父类的 encode 方法获取默认的 JSON 字符串
        default_encoded = super().encode(obj)
        # 替换多余的反斜杠转义
        result = default_encoded.replace("\\\\", "\\")
        return result.replace('\\"', '"')```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

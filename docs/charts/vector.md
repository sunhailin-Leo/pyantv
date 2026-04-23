# Vector

## 概述



## 配置项

暂无配置项说明

## 示例

```python
from pyantv import options as opts
from pyantv.charts import Vector
from pyantv.commons.utils import JsCode


c = (
    Vector()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/antfincdn/F5VcgnqRku/wind.json",
        )
    )
    .set_encode(
        x_field_name="longitude",
        y_field_name="latitude",
        color_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
        size_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
        rotate_f```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

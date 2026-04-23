# Point

## 概述



## 配置项

暂无配置项说明

## 示例

```python
from pyantv import options as opts
from pyantv.charts import Point

point = (
    Point()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
        ),
    )
    .set_encode(x_field_name="height", y_field_name="weight", color_field="gender")
)
point.render("point_example.html")
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

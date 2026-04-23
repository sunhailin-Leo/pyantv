# Link

## 概述



## 配置项

暂无配置项说明

## 示例

```python
from pyantv import options as opts
from pyantv.charts import Link, View
from pyantv.commons.utils import JsCode


link_1 = (
    Link()
    .set_encode(
        x_field_name="Date",
        y_field_name=["Low", "High"],
        color_field=JsCode("(d) => Math.sign(d.Close - d.Open)"),
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="black"),
        tooltip_opts=opts.TooltipOpts(
            title=JsCode("(d) => d.Date.toLocaleString()"),
            items=[
    ```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

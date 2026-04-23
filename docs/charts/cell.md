# Cell

## 概述



## 配置项

暂无配置项说明

## 示例

```python
from pyantv import options as opts
from pyantv.charts import Cell
from pyantv.commons.utils import JsCode


cell = (
    Cell()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/bmw-prod/bd287f2c-3e2b-4d0a-8428-6a85211dce33.json",
        )
    )
    .set_encode(x_field_name="x", y_field_name="y", color_field="index")
    .set_scale(color_scale_opts=opts.ScaleOrdinalOpts())
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
     ```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)

"""
图例项样式
G2 文档: https://g2.antv.antgroup.com/examples/component/legend/#legend-item-style
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"product": "A", "sales": 120, "region": "华东"},
    {"product": "B", "sales": 150, "region": "华东"},
    {"product": "A", "sales": 100, "region": "华北"},
    {"product": "B", "sales": 130, "region": "华北"},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="product", y_field_name="sales", color_field="region")
    .set_global_options(
        title_opts=opts.TitleOpts(title="图例项样式"),
        transform_opts=[opts.TransformDodgeXOpts()],
    )
)
chart.render("legend_item_style.html")

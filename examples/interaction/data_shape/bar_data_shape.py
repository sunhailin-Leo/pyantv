"""
条形图-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "产品A", "value": 120}, {"name": "产品B", "value": 200},
    {"name": "产品C", "value": 150}, {"name": "产品D", "value": 80},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="条形图-数形交互"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("bar_data_shape.html")

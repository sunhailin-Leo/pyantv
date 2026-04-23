"""
圆柱
G2 文档: https://g2.antv.antgroup.com/examples/threed/bar/#cylinder
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 40}, {"name": "B", "value": 65},
    {"name": "C", "value": 50}, {"name": "D", "value": 75},
    {"name": "E", "value": 55},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="圆柱"),
    )
)
chart.render("cylinder.html")

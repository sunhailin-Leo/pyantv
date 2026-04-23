"""
圆锥
G2 文档: https://g2.antv.antgroup.com/examples/threed/bar/#cone
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 35}, {"name": "B", "value": 60},
    {"name": "C", "value": 48}, {"name": "D", "value": 72},
    {"name": "E", "value": 58},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="圆锥"),
    )
)
chart.render("cone.html")

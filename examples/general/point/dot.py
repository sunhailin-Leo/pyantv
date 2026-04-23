"""
点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#dot
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"name": "January", "value": 51},
    {"name": "February", "value": 91},
    {"name": "March", "value": 34},
    {"name": "April", "value": 47},
    {"name": "May", "value": 63},
    {"name": "June", "value": 58},
    {"name": "July", "value": 56},
    {"name": "August", "value": 77},
    {"name": "September", "value": 99},
    {"name": "October", "value": 106},
    {"name": "November", "value": 88},
    {"name": "December", "value": 56},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="value", y_field_name="name", color_field="#5B8FF9")
    .set_global_options(
        title_opts=opts.TitleOpts(title="点图"),
    )
)
chart.render("dot.html")

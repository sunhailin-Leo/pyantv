"""
负数面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#negative-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "Jan", "value": -20},
    {"month": "Feb", "value": -15},
    {"month": "Mar", "value": 5},
    {"month": "Apr", "value": 25},
    {"month": "May", "value": 40},
    {"month": "Jun", "value": 55},
    {"month": "Jul", "value": 60},
    {"month": "Aug", "value": 50},
    {"month": "Sep", "value": 30},
    {"month": "Oct", "value": 10},
    {"month": "Nov", "value": -10},
    {"month": "Dec", "value": -25},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(title_opts=opts.TitleOpts(title="负数面积图"))
)
chart.render("negative_area.html")

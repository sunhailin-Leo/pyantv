"""
面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "Jan", "temperature": 7},
    {"month": "Feb", "temperature": 6.9},
    {"month": "Mar", "temperature": 9.5},
    {"month": "Apr", "temperature": 14.5},
    {"month": "May", "temperature": 18.2},
    {"month": "Jun", "temperature": 21.5},
    {"month": "Jul", "temperature": 25.2},
    {"month": "Aug", "temperature": 26.5},
    {"month": "Sep", "temperature": 23.3},
    {"month": "Oct", "temperature": 18.3},
    {"month": "Nov", "temperature": 13.9},
    {"month": "Dec", "temperature": 9.6},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="temperature", shape_field="smooth")
    .set_global_options(title_opts=opts.TitleOpts(title="曲线面积图"))
)
chart.render("area.html")

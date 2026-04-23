"""
阶梯折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#step-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "Jan", "value": 100},
    {"month": "Feb", "value": 120},
    {"month": "Mar", "value": 115},
    {"month": "Apr", "value": 135},
    {"month": "May", "value": 148},
    {"month": "Jun", "value": 160},
    {"month": "Jul", "value": 155},
    {"month": "Aug", "value": 170},
    {"month": "Sep", "value": 162},
    {"month": "Oct", "value": 180},
    {"month": "Nov", "value": 195},
    {"month": "Dec", "value": 210},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", shape_field="hvh")
    .set_global_options(title_opts=opts.TitleOpts(title="阶梯折线图"))
)
chart.render("step_line.html")

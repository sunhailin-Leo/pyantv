"""
变宽折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#variable-width-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "Jan", "value": 120, "weight": 2},
    {"month": "Feb", "value": 135, "weight": 3},
    {"month": "Mar", "value": 148, "weight": 5},
    {"month": "Apr", "value": 160, "weight": 4},
    {"month": "May", "value": 175, "weight": 6},
    {"month": "Jun", "value": 190, "weight": 8},
    {"month": "Jul", "value": 205, "weight": 7},
    {"month": "Aug", "value": 220, "weight": 5},
    {"month": "Sep", "value": 235, "weight": 4},
    {"month": "Oct", "value": 250, "weight": 3},
    {"month": "Nov", "value": 265, "weight": 6},
    {"month": "Dec", "value": 280, "weight": 9},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", size_field="weight")
    .set_global_options(title_opts=opts.TitleOpts(title="变宽折线图"))
)
chart.render("variable_width_line.html")

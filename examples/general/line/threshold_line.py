"""
阈值折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#threshold-line
"""
from pyantv import options as opts
from pyantv.charts import View, Line, LineY

data = [
    {"month": "Jan", "value": 120},
    {"month": "Feb", "value": 135},
    {"month": "Mar", "value": 148},
    {"month": "Apr", "value": 260},
    {"month": "May", "value": 175},
    {"month": "Jun", "value": 190},
    {"month": "Jul", "value": 305},
    {"month": "Aug", "value": 220},
    {"month": "Sep", "value": 235},
    {"month": "Oct", "value": 250},
    {"month": "Nov", "value": 165},
    {"month": "Dec", "value": 280},
]

line = Line().set_encode(x_field_name="month", y_field_name="value")
threshold = (
    LineY()
    .set_data(data=[200])
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="red", line_dash=[4, 4]))
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[line.options, threshold.options])
    .set_global_options(title_opts=opts.TitleOpts(title="阈值折线图"))
)
chart.render("threshold_line.html")

"""
折线标记样式
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#line-marker-style
"""
from pyantv import options as opts
from pyantv.charts import View, Line, Point

data = [
    {"month": "Jan", "value": 120},
    {"month": "Feb", "value": 135},
    {"month": "Mar", "value": 148},
    {"month": "Apr", "value": 160},
    {"month": "May", "value": 175},
    {"month": "Jun", "value": 190},
    {"month": "Jul", "value": 205},
    {"month": "Aug", "value": 220},
    {"month": "Sep", "value": 235},
    {"month": "Oct", "value": 250},
    {"month": "Nov", "value": 265},
    {"month": "Dec", "value": 280},
]

line = Line()
point = (
    Point()
    .set_global_options(style_opts=opts.BaseChartStyleOpts(fill="white", stroke="#5B8FF9", line_width=2))
)

chart = (
    View()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_view_children(children=[line.options, point.options])
    .set_global_options(title_opts=opts.TitleOpts(title="折线标记样式"))
)
chart.render("line_marker_style.html")

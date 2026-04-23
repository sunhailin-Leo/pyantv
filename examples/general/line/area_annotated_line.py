"""
面积标注折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#area-annotated-line
"""
from pyantv import options as opts
from pyantv.charts import View, Line, Area

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

line = Line().set_encode(x_field_name="month", y_field_name="value")
area = (
    Area()
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.15))
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[area.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="面积标注折线图"))
)
chart.render("area_annotated_line.html")

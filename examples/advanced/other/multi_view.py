"""
多视图
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#multi-view
"""
from pyantv import options as opts
from pyantv.charts import SpaceFlex, Interval, Line

bar_data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
]

line_data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="category", y_field_name="value")
)

line = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="value")
)

chart = (
    SpaceFlex()
    .set_space_flex_children(children=[bar.options, line.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="多视图"),
    )
)
chart.render("multi_view.html")

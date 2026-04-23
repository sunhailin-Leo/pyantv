"""
点标记的条形图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/shape/#point-marked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval, Point, View

bar_data = [
    {"category": "A", "value": 50},
    {"category": "B", "value": 70},
    {"category": "C", "value": 45},
    {"category": "D", "value": 80},
]

target_data = [
    {"category": "A", "target": 60},
    {"category": "B", "target": 65},
    {"category": "C", "target": 55},
    {"category": "D", "target": 75},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)

points = (
    Point()
    .set_data(data=target_data)
    .set_encode(x_field_name="category", y_field_name="target")
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartStyleOpts(fill="red"),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, points.options])
    .set_global_options(title_opts=opts.TitleOpts(title="点标记的条形图"))
)
chart.render("point_marked_bar.html")

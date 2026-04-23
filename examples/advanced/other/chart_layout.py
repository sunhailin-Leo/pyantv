"""
图表布局
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#chart-layout
"""
from pyantv import options as opts
from pyantv.charts import SpaceFlex, Interval, Point

bar_data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 50},
    {"name": "C", "value": 45}, {"name": "D", "value": 60},
]

scatter_data = [
    {"x": 10, "y": 20}, {"x": 30, "y": 50},
    {"x": 50, "y": 40}, {"x": 70, "y": 80},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="name", y_field_name="value")
)

scatter = (
    Point()
    .set_data(data=scatter_data)
    .set_encode(x_field_name="x", y_field_name="y")
)

chart = (
    SpaceFlex()
    .set_space_flex_children(children=[bar.options, scatter.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="图表布局"),
    )
)
chart.render("chart_layout.html")

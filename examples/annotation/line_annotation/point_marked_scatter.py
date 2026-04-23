"""
点标记的散点图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#point-marked-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point, View

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(50)]
highlight = [{"x": 50, "y": 80}]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5))
)

marker = (
    Point()
    .set_data(data=highlight)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(fill="red"))
)

chart = (
    View()
    .set_view_children(children=[scatter.options, marker.options])
    .set_global_options(title_opts=opts.TitleOpts(title="点标记的散点图"))
)
chart.render("point_marked_scatter.html")

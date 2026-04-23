"""
线标记的散点图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#line-marked-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point, LineX, LineY, View

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(50)]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

x_line = (
    LineX()
    .set_data(data=[{"value": 50}])
    .set_encode(x_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=1))
)

y_line = (
    LineY()
    .set_data(data=[{"value": 50}])
    .set_encode(y_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="blue", line_width=1))
)

chart = (
    View()
    .set_view_children(children=[scatter.options, x_line.options, y_line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="线标记的散点图"))
)
chart.render("line_marked_scatter.html")

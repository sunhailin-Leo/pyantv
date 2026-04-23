"""
区域标记的四象限散点图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#quadrant-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point, LineX, LineY, View

import random
random.seed(42)
data = [{"x": random.uniform(-50, 50), "y": random.uniform(-50, 50)} for _ in range(80)]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

x_axis = (
    LineX()
    .set_data(data=[{"value": 0}])
    .set_encode(x_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="#888", line_width=1))
)

y_axis = (
    LineY()
    .set_data(data=[{"value": 0}])
    .set_encode(y_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="#888", line_width=1))
)

chart = (
    View()
    .set_view_children(children=[scatter.options, x_axis.options, y_axis.options])
    .set_global_options(title_opts=opts.TitleOpts(title="区域标记的四象限散点图"))
)
chart.render("quadrant_scatter.html")

"""
回归线
G2 文档: https://g2.antv.antgroup.com/examples/general/data-processing/#regression-line
"""
from pyantv import options as opts
from pyantv.charts import Point, Line, View

import random
random.seed(42)
data = [{"x": i, "y": 2 * i + random.gauss(0, 10)} for i in range(50)]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5),
    )
)

regression_data = [{"x": 0, "y": 0}, {"x": 49, "y": 98}]
reg_line = (
    Line()
    .set_data(data=regression_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[scatter.options, reg_line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="回归线"))
)
chart.render("regression_line.html")

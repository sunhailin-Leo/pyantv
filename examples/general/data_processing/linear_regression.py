"""
线性回归线
G2 文档: https://g2.antv.antgroup.com/examples/general/data-processing/#linear-regression
"""
from pyantv import options as opts
from pyantv.charts import Point, Line, View

import random
random.seed(42)
data = [{"x": i, "y": 3 * i + 10 + random.gauss(0, 8)} for i in range(40)]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

reg_data = [{"x": 0, "y": 10}, {"x": 39, "y": 127}]
reg_line = (
    Line()
    .set_data(data=reg_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#F4664A", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[scatter.options, reg_line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="线性回归线"))
)
chart.render("linear_regression.html")

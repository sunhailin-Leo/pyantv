"""
多项式回归线
G2 文档: https://g2.antv.antgroup.com/examples/general/data-processing/#polynomial-regression
"""
from pyantv import options as opts
from pyantv.charts import Point, Line, View

import random
random.seed(42)
data = [{"x": i, "y": 0.001 * i**3 - 0.1 * i**2 + 3 * i + random.gauss(0, 5)} for i in range(50)]
curve_data = [{"x": i, "y": 0.001 * i**3 - 0.1 * i**2 + 3 * i} for i in range(50)]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

curve = (
    Line()
    .set_data(data=curve_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#F4664A", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[scatter.options, curve.options])
    .set_global_options(title_opts=opts.TitleOpts(title="多项式回归线"))
)
chart.render("polynomial_regression.html")

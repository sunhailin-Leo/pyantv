"""
对数回归线
G2 文档: https://g2.antv.antgroup.com/examples/general/data-processing/#logarithmic-regression
"""
from pyantv import options as opts
from pyantv.charts import Point, Line, View

import random
import math
random.seed(42)
data = [{"x": i + 1, "y": 20 * math.log(i + 1) + random.gauss(0, 3)} for i in range(40)]
curve_data = [{"x": i + 1, "y": 20 * math.log(i + 1)} for i in range(40)]

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
    .set_global_options(title_opts=opts.TitleOpts(title="对数回归线"))
)
chart.render("logarithmic_regression.html")

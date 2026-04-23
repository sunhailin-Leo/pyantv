
"""
Spec 函数表达式
G2 文档: https://g2.antv.antgroup.com/examples/style/bindling/#spec-function
"""
from pyantv import options as opts
from pyantv.charts import Line

import math
data = [{"x": i * 0.1, "y": math.sin(i * 0.1)} for i in range(63)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="Spec 函数表达式"),
    )
)
chart.render("spec_function.html")

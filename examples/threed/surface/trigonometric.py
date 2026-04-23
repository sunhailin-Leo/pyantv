"""
三角函数
G2 文档: https://g2.antv.antgroup.com/examples/threed/surface/#trigonometric
"""
from pyantv import options as opts
from pyantv.charts import HeatMap

import math
data = []
for i in range(20):
    for j in range(20):
        data.append({"x": i, "y": j, "value": math.sin(i * 0.3) * math.sin(j * 0.3) * 50 + 50})

chart = (
    HeatMap()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="三角函数"),
    )
)
chart.render("trigonometric.html")

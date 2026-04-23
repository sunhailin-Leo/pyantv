"""
球体
G2 文档: https://g2.antv.antgroup.com/examples/threed/scatter/#sphere
"""
from pyantv import options as opts
from pyantv.charts import Point

import math
data = []
for i in range(100):
    theta = (i / 100) * 2 * math.pi
    phi = (i / 100) * math.pi
    data.append({"x": math.sin(phi) * math.cos(theta) * 50 + 50, "y": math.sin(phi) * math.sin(theta) * 50 + 50, "z": math.cos(phi) * 50 + 50})

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="z")
    .set_global_options(
        title_opts=opts.TitleOpts(title="球体"),
    )
)
chart.render("sphere.html")

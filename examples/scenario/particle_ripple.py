"""
粒子涟漪效果
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#particle-ripple
"""
from pyantv import options as opts
from pyantv.charts import Point

import math
data = []
for r in range(1, 6):
    for i in range(r * 8):
        angle = i * 2 * math.pi / (r * 8)
        data.append({"x": math.cos(angle) * r * 10 + 50, "y": math.sin(angle) * r * 10 + 50, "ring": r})

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="ring")
    .set_global_options(
        title_opts=opts.TitleOpts(title="粒子涟漪效果"),
    )
)
chart.render("particle_ripple.html")

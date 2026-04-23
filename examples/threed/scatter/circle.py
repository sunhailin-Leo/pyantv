"""
圆形
G2 文档: https://g2.antv.antgroup.com/examples/threed/scatter/#circle
"""
from pyantv import options as opts
from pyantv.charts import Point

import math
data = [{"x": math.cos(i * 2 * math.pi / 50) * 40 + 50, "y": math.sin(i * 2 * math.pi / 50) * 40 + 50, "index": i} for i in range(50)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="index")
    .set_global_options(
        title_opts=opts.TitleOpts(title="圆形"),
    )
)
chart.render("circle.html")

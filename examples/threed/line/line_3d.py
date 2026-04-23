"""
折线
G2 文档: https://g2.antv.antgroup.com/examples/threed/line/#line
"""
from pyantv import options as opts
from pyantv.charts import Line

import math
data = [{"x": i, "y": math.sin(i * 0.3) * 50 + 50, "z": math.cos(i * 0.3) * 50 + 50} for i in range(50)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="3D 折线"),
    )
)
chart.render("line_3d.html")

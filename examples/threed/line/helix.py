"""
螺旋线
G2 文档: https://g2.antv.antgroup.com/examples/threed/line/#helix
"""
from pyantv import options as opts
from pyantv.charts import Line

import math
data = [{"t": i, "x": math.cos(i * 0.2) * (50 + i * 0.5), "y": math.sin(i * 0.2) * (50 + i * 0.5)} for i in range(100)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="螺旋线"),
    )
)
chart.render("helix.html")

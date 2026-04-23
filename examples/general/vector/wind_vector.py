"""
风向量场
G2 文档: https://g2.antv.antgroup.com/examples/general/vector/#wind-vector
"""
import math
from pyantv import options as opts
from pyantv.charts import Vector

data = []
for i in range(8):
    for j in range(8):
        angle = (i + j) * 0.5
        data.append({
            "x": i,
            "y": j,
            "vx": math.cos(angle) * 2,
            "vy": math.sin(angle) * 2,
        })

chart = (
    Vector()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="x")
    .set_global_options(
        title_opts=opts.TitleOpts(title="风向量场"),
    )
)
chart.render("wind_vector.html")

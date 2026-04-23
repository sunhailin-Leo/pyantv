"""
珀林噪声场
G2 文档: https://g2.antv.antgroup.com/examples/general/vector/#perlin-noise
"""
import math
from pyantv import options as opts
from pyantv.charts import Vector

data = []
for i in range(10):
    for j in range(10):
        angle = math.sin(i * 0.3) * math.cos(j * 0.3) * math.pi
        magnitude = math.sqrt(i * i + j * j) * 0.1
        data.append({
            "x": i,
            "y": j,
            "vx": math.cos(angle) * magnitude,
            "vy": math.sin(angle) * magnitude,
        })

chart = (
    Vector()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="珀林噪声场"),
        style_opts=opts.BaseChartStyleOpts(stroke="#5B8FF9"),
    )
)
chart.render("perlin_noise.html")

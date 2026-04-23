"""
雷达扫描效果
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#radar-scan
"""
from pyantv import options as opts
from pyantv.charts import Point

import random, math
random.seed(42)
data = []
for _ in range(30):
    angle = random.uniform(0, 2 * math.pi)
    radius = random.uniform(10, 50)
    data.append({"x": math.cos(angle) * radius + 50, "y": math.sin(angle) * radius + 50, "distance": radius})

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="distance", size_field="distance")
    .set_global_options(
        title_opts=opts.TitleOpts(title="雷达扫描效果"),
    )
)
chart.render("radar_scan.html")

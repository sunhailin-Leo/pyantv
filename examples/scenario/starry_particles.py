"""
星空粒子系统
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#starry-particles
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "brightness": random.uniform(1, 10)} for _ in range(200)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="brightness")
    .set_global_options(
        title_opts=opts.TitleOpts(title="星空粒子系统"),
    )
)
chart.render("starry_particles.html")

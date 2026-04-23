"""
蜂群图
G2 文档: https://g2.antv.antgroup.com/examples/general/swarm/#swarm
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"category": random.choice(["A", "B", "C"]), "value": random.gauss(50, 15)}
        for _ in range(100)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="蜂群图"),
        transform_opts=[opts.TransformJitterXOpts()],
    )
)
chart.render("swarm.html")

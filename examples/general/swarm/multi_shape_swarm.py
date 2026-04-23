"""
不同形状的蜂群图
G2 文档: https://g2.antv.antgroup.com/examples/general/swarm/#multi-shape-swarm
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
shapes = ["circle", "square", "triangle"]
data = [{"category": random.choice(["X", "Y", "Z"]),
         "value": random.gauss(50, 12),
         "shape": random.choice(shapes)}
        for _ in range(120)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category",
                shape_field="shape")
    .set_global_options(
        title_opts=opts.TitleOpts(title="不同形状的蜂群图"),
        transform_opts=[opts.TransformJitterXOpts()],
    )
)
chart.render("multi_shape_swarm.html")

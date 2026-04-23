"""
横向蜂群图
G2 文档: https://g2.antv.antgroup.com/examples/general/swarm/#horizontal-swarm
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"group": random.choice(["甲", "乙", "丙"]), "score": random.gauss(60, 10)}
        for _ in range(90)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="group", y_field_name="score", color_field="group")
    .set_global_options(
        title_opts=opts.TitleOpts(title="横向蜂群图"),
        transform_opts=[opts.TransformJitterXOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("horizontal_swarm.html")

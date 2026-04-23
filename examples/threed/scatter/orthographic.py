"""
正交投影
G2 文档: https://g2.antv.antgroup.com/examples/threed/scatter/#orthographic
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "z": random.uniform(0, 100)} for _ in range(60)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="z", color_field="z")
    .set_global_options(
        title_opts=opts.TitleOpts(title="正交投影"),
    )
)
chart.render("orthographic.html")

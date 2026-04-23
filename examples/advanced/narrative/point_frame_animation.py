"""
点帧动画
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/narrative/#point-frame-animation
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "category": random.choice(["A", "B", "C"])} for _ in range(50)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="点帧动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("point_frame_animation.html")

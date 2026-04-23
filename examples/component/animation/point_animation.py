"""
点图动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#point-animation
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "size": random.uniform(5, 20)} for _ in range(40)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="size")
    .set_global_options(
        title_opts=opts.TitleOpts(title="点图动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("point_animation.html")

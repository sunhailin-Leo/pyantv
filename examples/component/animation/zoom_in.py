"""
ZoomIn 动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#zoom-in
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(30)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="ZoomIn 动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("zoom_in.html")

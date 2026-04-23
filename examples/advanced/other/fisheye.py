"""
鱼眼
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#fisheye
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "size": random.uniform(5, 20)} for _ in range(80)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="size")
    .set_global_options(
        title_opts=opts.TitleOpts(title="鱼眼"),
    )
)
chart.render("fisheye.html")

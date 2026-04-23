
"""
WebGL 渲染器
G2 文档: https://g2.antv.antgroup.com/examples/style/bindling/#webgl-bindling
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(100)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="WebGL 渲染器"),
    )
)
chart.render("webgl_renderer.html")

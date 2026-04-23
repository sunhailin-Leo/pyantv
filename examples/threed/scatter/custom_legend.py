"""
自定义图例
G2 文档: https://g2.antv.antgroup.com/examples/threed/scatter/#custom-legend
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "category": random.choice(["类型A", "类型B", "类型C"])} for _ in range(60)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义图例"),
    )
)
chart.render("custom_legend.html")

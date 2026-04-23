"""
径向扰动散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#radial-jitter-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)

categories = ["A", "B", "C", "D"]
data = []
for category in categories:
    count = random.randint(20, 40)
    for _ in range(count):
        data.append({
            "type": category,
            "value": round(random.uniform(0, 1), 2),
        })

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="径向扰动散点图"),
        transform_opts=[opts.TransformJitterXOpts()],
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("radial_jitter_scatter.html")

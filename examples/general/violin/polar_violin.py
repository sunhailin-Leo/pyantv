"""
极坐标小提琴图
G2 文档: https://g2.antv.antgroup.com/examples/general/violin/#polar-violin
"""
from pyantv import options as opts
from pyantv.charts import Density

import random
random.seed(42)
data = []
for group in ["春", "夏", "秋", "冬"]:
    mean = {"春": 15, "夏": 30, "秋": 20, "冬": 5}[group]
    for _ in range(80):
        data.append({"season": group, "temp": random.gauss(mean, 5)})

chart = (
    Density()
    .set_data(data=data)
    .set_encode(x_field_name="season", y_field_name="temp", color_field="season")
    .set_global_options(
        title_opts=opts.TitleOpts(title="极坐标小提琴图"),
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("polar_violin.html")

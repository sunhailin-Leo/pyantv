"""
小提琴图
G2 文档: https://g2.antv.antgroup.com/examples/general/violin/#violin
"""
from pyantv import options as opts
from pyantv.charts import Density

import random
random.seed(42)
data = []
for group in ["A", "B", "C"]:
    mean = {"A": 40, "B": 55, "C": 70}[group]
    for _ in range(100):
        data.append({"group": group, "value": random.gauss(mean, 12)})

chart = (
    Density()
    .set_data(data=data)
    .set_encode(x_field_name="group", y_field_name="value", color_field="group")
    .set_global_options(
        title_opts=opts.TitleOpts(title="小提琴图"),
    )
)
chart.render("violin.html")

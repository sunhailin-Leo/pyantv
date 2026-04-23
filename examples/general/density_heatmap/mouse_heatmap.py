"""
鼠标热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/density-heatmap/#mouse-heatmap
"""
from pyantv import options as opts
from pyantv.charts import HeatMap

import random
random.seed(42)
data = []
for _ in range(200):
    x = random.gauss(400, 100)
    y = random.gauss(300, 80)
    data.append({"x": round(x), "y": round(y), "value": random.randint(1, 10)})

chart = (
    HeatMap()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="鼠标热力图"),
    )
)
chart.render("mouse_heatmap.html")

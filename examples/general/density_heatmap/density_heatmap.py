"""
密度热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/density-heatmap/#density-heatmap
"""
from pyantv import options as opts
from pyantv.charts import HeatMap

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(500)]

chart = (
    HeatMap()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="密度热力图"),
    )
)
chart.render("density_heatmap.html")

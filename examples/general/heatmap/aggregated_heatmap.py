"""
聚合热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/heatmap/#aggregated-heatmap
"""
from pyantv import options as opts
from pyantv.charts import HeatMap

import random
random.seed(789)

data = []
for _ in range(200):
    data.append({
        "x": round(random.uniform(0, 10), 1),
        "y": round(random.uniform(0, 10), 1),
        "weight": random.randint(1, 10),
    })

chart = (
    HeatMap()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="weight")
    .set_heatmap_style(
        opacity=0.8,
        gradient=[
            [0, "white"],
            [0.2, "blue"],
            [0.4, "cyan"],
            [0.6, "lime"],
            [0.8, "yellow"],
            [1, "red"],
        ],
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="聚合热力图"),
    )
)
chart.render("aggregated_heatmap.html")

"""
散点分布热力
G2 文档: https://g2.antv.antgroup.com/examples/general/density-heatmap/#scatter-density
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = []
for _ in range(300):
    x = random.gauss(50, 15)
    y = random.gauss(50, 15)
    data.append({"x": x, "y": y})

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="散点分布热力"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.3),
    )
)
chart.render("scatter_density.html")

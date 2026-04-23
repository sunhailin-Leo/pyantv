"""
区域标记的散点图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/interval/#region-marked-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point, Rect, View

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(60)]
region_data = [{"x1": 30, "y1": 30, "x2": 70, "y2": 70}]

scatter = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

region = (
    Rect()
    .set_data(data=region_data)
    .set_encode(x_field_name="x1", y_field_name="y1")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.1, stroke="#5B8FF9"),
    )
)

chart = (
    View()
    .set_view_children(children=[scatter.options, region.options])
    .set_global_options(title_opts=opts.TitleOpts(title="区域标记的散点图"))
)
chart.render("region_marked_scatter.html")

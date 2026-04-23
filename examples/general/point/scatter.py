"""
散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"height": 161.2, "weight": 51.6},
    {"height": 167.5, "weight": 59.0},
    {"height": 159.5, "weight": 49.2},
    {"height": 157.0, "weight": 63.0},
    {"height": 155.8, "weight": 53.6},
    {"height": 170.0, "weight": 59.0},
    {"height": 159.1, "weight": 47.6},
    {"height": 166.0, "weight": 69.8},
    {"height": 176.2, "weight": 66.8},
    {"height": 160.2, "weight": 75.2},
    {"height": 172.5, "weight": 55.2},
    {"height": 170.9, "weight": 54.2},
    {"height": 172.9, "weight": 62.5},
    {"height": 153.4, "weight": 42.0},
    {"height": 160.0, "weight": 50.0},
    {"height": 147.2, "weight": 49.8},
    {"height": 168.2, "weight": 49.2},
    {"height": 175.0, "weight": 73.2},
    {"height": 157.0, "weight": 47.8},
    {"height": 167.6, "weight": 68.8},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="height", y_field_name="weight")
    .set_global_options(
        title_opts=opts.TitleOpts(title="散点图"),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.65),
    )
)
chart.render("scatter.html")

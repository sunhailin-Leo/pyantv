"""
一维散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#one-dimensional-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"value": 59},
    {"value": 36},
    {"value": 58},
    {"value": 42},
    {"value": 15},
    {"value": 78},
    {"value": 63},
    {"value": 91},
    {"value": 25},
    {"value": 47},
    {"value": 82},
    {"value": 70},
    {"value": 55},
    {"value": 33},
    {"value": 68},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="一维散点图"),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.65),
    )
)
chart.render("one_dimensional_scatter.html")

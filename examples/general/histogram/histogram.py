"""
直方图
G2 文档: https://g2.antv.antgroup.com/examples/general/histogram/#histogram
"""
from pyantv import options as opts
from pyantv.charts import Rect

data = [
    {"value": 1.2}, {"value": 3.4}, {"value": 2.1}, {"value": 5.6},
    {"value": 4.3}, {"value": 7.8}, {"value": 6.5}, {"value": 8.9},
    {"value": 3.2}, {"value": 4.7}, {"value": 5.1}, {"value": 2.8},
    {"value": 6.3}, {"value": 7.1}, {"value": 1.9}, {"value": 4.5},
    {"value": 3.8}, {"value": 5.9}, {"value": 8.2}, {"value": 2.5},
    {"value": 6.7}, {"value": 7.4}, {"value": 1.5}, {"value": 4.1},
    {"value": 3.6}, {"value": 5.3}, {"value": 8.6}, {"value": 2.3},
    {"value": 6.9}, {"value": 7.7}, {"value": 1.8}, {"value": 4.9},
    {"value": 3.1}, {"value": 5.7}, {"value": 8.4}, {"value": 2.6},
    {"value": 6.1}, {"value": 7.3}, {"value": 1.4}, {"value": 4.8},
]

chart = (
    Rect()
    .set_data(data=data)
    .set_encode(x_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="直方图"),
        transform_opts=[opts.TransformBinXOpts(channel_name="y", channel_transform="count")],
    )
)
chart.render("histogram.html")

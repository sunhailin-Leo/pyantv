"""
层叠直方图
G2 文档: https://g2.antv.antgroup.com/examples/general/histogram/#stacked-histogram
"""
from pyantv import options as opts
from pyantv.charts import Rect

data = [
    {"value": 1.5, "type": "A"}, {"value": 3.2, "type": "A"}, {"value": 5.1, "type": "A"},
    {"value": 7.4, "type": "A"}, {"value": 2.3, "type": "A"}, {"value": 4.6, "type": "A"},
    {"value": 6.8, "type": "A"}, {"value": 8.1, "type": "A"}, {"value": 3.7, "type": "A"},
    {"value": 5.9, "type": "A"}, {"value": 1.8, "type": "A"}, {"value": 4.2, "type": "A"},
    {"value": 2.1, "type": "B"}, {"value": 4.5, "type": "B"}, {"value": 6.3, "type": "B"},
    {"value": 8.7, "type": "B"}, {"value": 3.4, "type": "B"}, {"value": 5.6, "type": "B"},
    {"value": 7.2, "type": "B"}, {"value": 1.3, "type": "B"}, {"value": 4.8, "type": "B"},
    {"value": 6.1, "type": "B"}, {"value": 2.7, "type": "B"}, {"value": 5.4, "type": "B"},
]

chart = (
    Rect()
    .set_data(data=data)
    .set_encode(x_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="层叠直方图"),
        transform_opts=[
            opts.TransformBinXOpts(channel_name="y", channel_transform="count"),
            opts.TransformStackYOpts(),
        ],
        style_opts=opts.BaseChartStyleOpts(inset=1),
    )
)
chart.render("stacked_histogram.html")

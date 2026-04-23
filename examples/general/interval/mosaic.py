"""
马赛克图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#mosaic
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"market": "East", "segment": "Consumer", "value": 150},
    {"market": "East", "segment": "Corporate", "value": 100},
    {"market": "East", "segment": "Home Office", "value": 80},
    {"market": "West", "segment": "Consumer", "value": 200},
    {"market": "West", "segment": "Corporate", "value": 120},
    {"market": "West", "segment": "Home Office", "value": 90},
    {"market": "Central", "segment": "Consumer", "value": 130},
    {"market": "Central", "segment": "Corporate", "value": 85},
    {"market": "Central", "segment": "Home Office", "value": 65},
    {"market": "South", "segment": "Consumer", "value": 110},
    {"market": "South", "segment": "Corporate", "value": 70},
    {"market": "South", "segment": "Home Office", "value": 50},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="market", y_field_name="value", color_field="segment")
    .set_global_options(
        transform_opts=[
            opts.TransformFlexXOpts(),
            opts.TransformStackYOpts(),
            opts.TransformNormalizeYOpts(),
        ],
        title_opts=opts.TitleOpts(title="马赛克图"),
    )
)
chart.render("mosaic.html")

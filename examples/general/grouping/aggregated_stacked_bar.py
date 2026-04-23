"""
聚合堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#aggregated-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"region": "华北", "type": "产品A", "channel": "线上", "value": 50},
    {"region": "华北", "type": "产品A", "channel": "线下", "value": 30},
    {"region": "华北", "type": "产品B", "channel": "线上", "value": 40},
    {"region": "华北", "type": "产品B", "channel": "线下", "value": 25},
    {"region": "华东", "type": "产品A", "channel": "线上", "value": 60},
    {"region": "华东", "type": "产品A", "channel": "线下", "value": 35},
    {"region": "华东", "type": "产品B", "channel": "线上", "value": 45},
    {"region": "华东", "type": "产品B", "channel": "线下", "value": 30},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="region", y_field_name="value", color_field="channel", series_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="聚合堆叠条形图"),
        transform_opts=[opts.TransformDodgeXOpts(), opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("aggregated_stacked_bar.html")

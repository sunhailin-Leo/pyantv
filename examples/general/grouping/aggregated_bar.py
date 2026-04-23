"""
聚合条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#aggregated-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"city": "北京", "type": "线上", "value": 120},
    {"city": "北京", "type": "线下", "value": 80},
    {"city": "上海", "type": "线上", "value": 100},
    {"city": "上海", "type": "线下", "value": 90},
    {"city": "广州", "type": "线上", "value": 85},
    {"city": "广州", "type": "线下", "value": 70},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="city", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="聚合条形图"),
        transform_opts=[opts.TransformDodgeXOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("aggregated_bar.html")

"""
饼图, 蜘蛛布局标签
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#pie-spider-label
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "微信", "value": 30},
    {"type": "支付宝", "value": 25},
    {"type": "现金", "value": 20},
    {"type": "银行卡", "value": 15},
    {"type": "信用卡", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="饼图, 蜘蛛布局标签"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(outer_radius=0.8),
        label_opts=[
            opts.LabelOpts(text_opts="type", position="spider"),
        ],
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)
chart.render("pie_spider_label.html")

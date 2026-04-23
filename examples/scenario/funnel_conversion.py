"""
漏斗转化分析
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#funnel-conversion
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"stage": "访问", "count": 10000},
    {"stage": "注册", "count": 6000},
    {"stage": "下单", "count": 3000},
    {"stage": "付款", "count": 2000},
    {"stage": "复购", "count": 800},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="count", color_field="stage")
    .set_global_options(
        title_opts=opts.TitleOpts(title="漏斗转化分析"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("funnel_conversion.html")

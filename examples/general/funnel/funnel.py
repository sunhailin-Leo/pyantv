"""
漏斗图
G2 文档: https://g2.antv.antgroup.com/examples/general/funnel/#funnel
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"stage": "浏览", "value": 5000},
    {"stage": "加购", "value": 3500},
    {"stage": "下单", "value": 2500},
    {"stage": "支付", "value": 1800},
    {"stage": "完成", "value": 1200},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="stage", shape_field="funnel")
    .set_global_options(
        title_opts=opts.TitleOpts(title="漏斗图"),
        transform_opts=[opts.TransformSymmetryYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("funnel.html")

"""
转化漏斗图
G2 文档: https://g2.antv.antgroup.com/examples/general/funnel/#conversion-funnel
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"stage": "访问", "value": 10000},
    {"stage": "注册", "value": 6000},
    {"stage": "激活", "value": 4000},
    {"stage": "留存", "value": 2500},
    {"stage": "付费", "value": 1000},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="stage", shape_field="funnel")
    .set_global_options(
        title_opts=opts.TitleOpts(title="转化漏斗图"),
        transform_opts=[opts.TransformSymmetryYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        label_opts=[opts.LabelOpts(text_opts="value", font_size=12)],
    )
)
chart.render("conversion_funnel.html")

"""
对比漏斗图
G2 文档: https://g2.antv.antgroup.com/examples/general/funnel/#comparison-funnel
"""
from pyantv import options as opts
from pyantv.charts import View, Interval

data_a = [
    {"stage": "浏览", "value": 5000, "group": "A"},
    {"stage": "加购", "value": 3500, "group": "A"},
    {"stage": "下单", "value": 2500, "group": "A"},
    {"stage": "支付", "value": 1800, "group": "A"},
]

data_b = [
    {"stage": "浏览", "value": 4500, "group": "B"},
    {"stage": "加购", "value": 3000, "group": "B"},
    {"stage": "下单", "value": 2000, "group": "B"},
    {"stage": "支付", "value": 1500, "group": "B"},
]

bar_a = (
    Interval()
    .set_data(data=data_a)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="group")
    .set_global_options(
        transform_opts=[opts.TransformSymmetryYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

bar_b = (
    Interval()
    .set_data(data=data_b)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="group")
    .set_global_options(
        transform_opts=[opts.TransformSymmetryYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartStyleOpts(fill="#5AD8A6"),
    )
)

chart = (
    View()
    .set_view_children(children=[bar_a.options, bar_b.options])
    .set_global_options(title_opts=opts.TitleOpts(title="对比漏斗图"))
)
chart.render("comparison_funnel.html")

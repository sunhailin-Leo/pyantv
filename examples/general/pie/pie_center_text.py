"""
饼图, 中心文本
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#pie-center-text
"""
from pyantv import options as opts
from pyantv.charts import Interval, Text, SpaceLayer

data = [
    {"type": "分类一", "value": 27},
    {"type": "分类二", "value": 25},
    {"type": "分类三", "value": 18},
    {"type": "分类四", "value": 15},
    {"type": "分类五", "value": 10},
    {"type": "其他", "value": 5},
]

donut = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(inner_radius=0.6),
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)

center_text = (
    Text()
    .set_global_options(
        style_opts={
            "text": "总计\n100",
            "x": "50%",
            "y": "50%",
            "textAlign": "center",
            "fontSize": 20,
            "fontWeight": "bold",
        },
    )
)

chart = (
    SpaceLayer()
    .set_space_layer_children(children=[donut.options, center_text.options])
    .set_global_options(title_opts=opts.TitleOpts(title="饼图, 中心文本"))
)
chart.render("pie_center_text.html")

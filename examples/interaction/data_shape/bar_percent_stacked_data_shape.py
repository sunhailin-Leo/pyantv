"""
条形图-百分比堆叠-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#bar-percent-stacked
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "type": "类型1", "value": 30},
    {"name": "A", "type": "类型2", "value": 40},
    {"name": "B", "type": "类型1", "value": 50},
    {"name": "B", "type": "类型2", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="条形图-百分比堆叠-数形交互"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
        transform_opts=[opts.TransformStackYOpts(), opts.TransformNormalizeYOpts()],
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("bar_percent_stacked_data_shape.html")

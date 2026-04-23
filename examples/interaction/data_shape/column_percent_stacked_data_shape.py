"""
柱形图-百分比堆叠-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#column-percent-stacked
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "type": "A", "value": 30},
    {"month": "2月", "type": "A", "value": 45},
    {"month": "1月", "type": "B", "value": 40},
    {"month": "2月", "type": "B", "value": 50},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="柱形图-百分比堆叠-数形交互"),
        transform_opts=[opts.TransformStackYOpts(), opts.TransformNormalizeYOpts()],
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("column_percent_stacked_data_shape.html")

"""
柱形图-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 50},
    {"month": "3月", "value": 45}, {"month": "4月", "value": 60},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 55},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="month")
    .set_global_options(
        title_opts=opts.TitleOpts(title="柱形图-数形交互"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("column_data_shape.html")


"""
层叠容器
G2 文档: https://g2.antv.antgroup.com/examples/composition/space/#space-layer
"""
from pyantv import options as opts
from pyantv.charts import Interval, Line, SpaceLayer

bar_data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 60},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="value")
)

line = (
    Line()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2))
)

chart = (
    SpaceLayer()
    .set_space_layer_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="层叠容器"))
)
chart.render("space_layer.html")

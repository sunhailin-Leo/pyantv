"""
线标记的瀑布图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/connection/#line-marked-waterfall
"""
from pyantv import options as opts
from pyantv.charts import Interval, Line, View

data = [
    {"stage": "初始", "value": 200},
    {"stage": "增长", "value": 80},
    {"stage": "损耗", "value": -30},
    {"stage": "回收", "value": 50},
    {"stage": "最终", "value": 300},
]

bar = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="stage")
)

line_chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#888", line_width=1),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, line_chart.options])
    .set_global_options(title_opts=opts.TitleOpts(title="线标记的瀑布图"))
)
chart.render("line_marked_waterfall.html")

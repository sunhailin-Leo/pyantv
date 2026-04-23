"""
突出超出阈值的柱状图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#threshold-column
"""
from pyantv import options as opts
from pyantv.charts import Interval, LineY, View

data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 55},
    {"name": "C", "value": 45}, {"name": "D", "value": 70},
    {"name": "E", "value": 35}, {"name": "F", "value": 60},
]

bar = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
)

threshold = (
    LineY()
    .set_data(data=[{"value": 50}])
    .set_encode(y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, threshold.options])
    .set_global_options(title_opts=opts.TitleOpts(title="突出超出阈值的柱状图"))
)
chart.render("threshold_column.html")

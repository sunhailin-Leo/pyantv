"""
平均值线标注的直方图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#mean-line-histogram
"""
from pyantv import options as opts
from pyantv.charts import Interval, LineY, View

bar_data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
    {"category": "E", "value": 35}, {"category": "F", "value": 55},
]

mean_value = sum(d["value"] for d in bar_data) / len(bar_data)
mean_data = [{"value": mean_value}]

bar_chart = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="category", y_field_name="value")
)

mean_line = (
    LineY()
    .set_data(data=mean_data)
    .set_encode(y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[bar_chart.options, mean_line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="平均值线标注的直方图"))
)
chart.render("mean_line_histogram.html")

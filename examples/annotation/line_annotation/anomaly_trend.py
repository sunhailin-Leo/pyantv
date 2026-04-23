"""
异动趋势图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#anomaly-trend
"""
from pyantv import options as opts
from pyantv.charts import Line, Point, View

line_data = [
    {"day": 1, "value": 20}, {"day": 2, "value": 22}, {"day": 3, "value": 25},
    {"day": 4, "value": 23}, {"day": 5, "value": 50}, {"day": 6, "value": 24},
    {"day": 7, "value": 26}, {"day": 8, "value": 21}, {"day": 9, "value": 23},
    {"day": 10, "value": 22},
]

anomaly_data = [{"day": 5, "value": 50}]

line_chart = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="day", y_field_name="value")
)

anomaly_point = (
    Point()
    .set_data(data=anomaly_data)
    .set_encode(x_field_name="day", y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="red"),
        label_opts=[opts.LabelOpts(text_opts="异常", font_size=12)],
    )
)

chart = (
    View()
    .set_view_children(children=[line_chart.options, anomaly_point.options])
    .set_global_options(title_opts=opts.TitleOpts(title="异动趋势图"))
)
chart.render("anomaly_trend.html")

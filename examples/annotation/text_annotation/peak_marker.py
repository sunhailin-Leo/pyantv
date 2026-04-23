"""
峰值标记
G2 文档: https://g2.antv.antgroup.com/examples/annotation/text/#peak-marker
"""
from pyantv import options as opts
from pyantv.charts import Line, Point, View

line_data = [
    {"x": 0, "y": 20}, {"x": 1, "y": 35}, {"x": 2, "y": 50},
    {"x": 3, "y": 45}, {"x": 4, "y": 70}, {"x": 5, "y": 55},
    {"x": 6, "y": 60}, {"x": 7, "y": 85}, {"x": 8, "y": 75},
]

peak_data = [{"x": 7, "y": 85}]

line_chart = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="x", y_field_name="y")
)

peak_point = (
    Point()
    .set_data(data=peak_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="red"),
        label_opts=[opts.LabelOpts(text_opts="峰值", font_size=12)],
    )
)

chart = (
    View()
    .set_view_children(children=[line_chart.options, peak_point.options])
    .set_global_options(title_opts=opts.TitleOpts(title="峰值标记"))
)
chart.render("peak_marker.html")

"""
徽章标记的折线图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/shape/#badge-marked-line
"""
from pyantv import options as opts
from pyantv.charts import Line, Point, View

line_data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 65},
]

badge_data = [{"month": "6月", "value": 65}]

line_chart = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="value")
)

badge = (
    Point()
    .set_data(data=badge_data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#F4664A"),
        label_opts=[opts.LabelOpts(text_opts="最高", font_size=10)],
    )
)

chart = (
    View()
    .set_view_children(children=[line_chart.options, badge.options])
    .set_global_options(title_opts=opts.TitleOpts(title="徽章标记的折线图"))
)
chart.render("badge_marked_line.html")

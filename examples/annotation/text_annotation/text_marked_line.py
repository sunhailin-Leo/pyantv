"""
文本标记的折线图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/text/#text-marked-line
"""
from pyantv import options as opts
from pyantv.charts import Line, Text, View

line_data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 60},
]

text_data = [{"month": "4月", "value": 55, "text": "峰值: 55"}]

line_chart = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="value")
)

text_chart = (
    Text()
    .set_data(data=text_data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        label_opts=[opts.LabelOpts(text_opts="text", font_size=12)],
    )
)

chart = (
    View()
    .set_view_children(children=[line_chart.options, text_chart.options])
    .set_global_options(title_opts=opts.TitleOpts(title="文本标记的折线图"))
)
chart.render("text_marked_line.html")

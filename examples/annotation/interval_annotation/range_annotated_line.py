"""
区间标注的折线图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/interval/#range-annotated-line
"""
from pyantv import options as opts
from pyantv.charts import Line, RangeY, View

line_data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 60},
]

range_data = [{"y1": 35, "y2": 50}]

line_chart = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="value")
)

range_band = (
    RangeY()
    .set_data(data=range_data)
    .set_encode(y_field_name="y1")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.15),
    )
)

chart = (
    View()
    .set_view_children(children=[range_band.options, line_chart.options])
    .set_global_options(title_opts=opts.TitleOpts(title="区间标注的折线图"))
)
chart.render("range_annotated_line.html")

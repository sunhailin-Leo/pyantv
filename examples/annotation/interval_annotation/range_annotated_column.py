"""
区间标注的柱状图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/interval/#range-annotated-column
"""
from pyantv import options as opts
from pyantv.charts import Interval, RangeY, View

bar_data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 55},
    {"name": "C", "value": 45}, {"name": "D", "value": 70},
    {"name": "E", "value": 35}, {"name": "F", "value": 60},
]

range_data = [{"y1": 40, "y2": 60}]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="name", y_field_name="value")
)

range_band = (
    RangeY()
    .set_data(data=range_data)
    .set_encode(y_field_name="y1")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#F4664A", fill_opacity=0.1),
    )
)

chart = (
    View()
    .set_view_children(children=[range_band.options, bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="区间标注的柱状图"))
)
chart.render("range_annotated_column.html")

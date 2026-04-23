"""
平均值线标注的柱状图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/line/#mean-line-column
"""
from pyantv import options as opts
from pyantv.charts import Interval, LineY, View

data = [
    {"month": "1月", "sales": 120}, {"month": "2月", "sales": 150},
    {"month": "3月", "sales": 130}, {"month": "4月", "sales": 160},
    {"month": "5月", "sales": 140}, {"month": "6月", "sales": 170},
]

mean_val = sum(d["sales"] for d in data) / len(data)

bar = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="sales")
)

mean_line = (
    LineY()
    .set_data(data=[{"value": mean_val}])
    .set_encode(y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#F4664A", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, mean_line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="平均值线标注的柱状图"))
)
chart.render("mean_line_column.html")

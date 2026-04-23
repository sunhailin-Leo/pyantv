"""
两个 tooltip
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#dual-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Interval, Line, View

bar_data = [
    {"month": "1月", "sales": 120}, {"month": "2月", "sales": 150},
    {"month": "3月", "sales": 130}, {"month": "4月", "sales": 160},
]

line_data = [
    {"month": "1月", "rate": 0.3}, {"month": "2月", "rate": 0.45},
    {"month": "3月", "rate": 0.35}, {"month": "4月", "rate": 0.5},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="sales")
)

line = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="rate")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2))
)

chart = (
    View()
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="两个 tooltip"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("dual_tooltip.html")

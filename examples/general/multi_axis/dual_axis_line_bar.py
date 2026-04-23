"""
双轴折线条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#dual-axis-line-bar
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

data = [
    {"month": "Jan", "sales": 1200, "rate": 15.2},
    {"month": "Feb", "sales": 1350, "rate": 18.5},
    {"month": "Mar", "sales": 1100, "rate": 12.3},
    {"month": "Apr", "sales": 1450, "rate": 22.1},
    {"month": "May", "sales": 1680, "rate": 25.6},
    {"month": "Jun", "sales": 1520, "rate": 20.8},
    {"month": "Jul", "sales": 1890, "rate": 28.3},
    {"month": "Aug", "sales": 1750, "rate": 24.1},
]

bar = (
    Interval()
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="销售额")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.8),
    )
)

line = (
    Line()
    .set_encode(x_field_name="month", y_field_name="rate")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="转化率(%)")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#F6BD16", line_width=2),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="双轴折线条形图"))
)
chart.render("dual_axis_line_bar.html")

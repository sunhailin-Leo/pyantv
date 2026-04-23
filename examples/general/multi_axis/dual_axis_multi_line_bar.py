"""
双轴多折线条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#dual-axis-multi-line-bar
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

bar_data = [
    {"month": "Jan", "value": 1200},
    {"month": "Feb", "value": 1350},
    {"month": "Mar", "value": 1100},
    {"month": "Apr", "value": 1450},
    {"month": "May", "value": 1680},
    {"month": "Jun", "value": 1520},
]

line_data = [
    {"month": "Jan", "type": "利润率", "rate": 15.2},
    {"month": "Feb", "type": "利润率", "rate": 18.5},
    {"month": "Mar", "type": "利润率", "rate": 12.3},
    {"month": "Apr", "type": "利润率", "rate": 22.1},
    {"month": "May", "type": "利润率", "rate": 25.6},
    {"month": "Jun", "type": "利润率", "rate": 20.8},
    {"month": "Jan", "type": "增长率", "rate": 10.5},
    {"month": "Feb", "type": "增长率", "rate": 12.8},
    {"month": "Mar", "type": "增长率", "rate": 8.2},
    {"month": "Apr", "type": "增长率", "rate": 15.3},
    {"month": "May", "type": "增长率", "rate": 18.9},
    {"month": "Jun", "type": "增长率", "rate": 14.6},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="销售额")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.6),
    )
)

line = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="rate", color_field="type")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="比率(%)")),
        ),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="双轴多折线条形图"))
)
chart.render("dual_axis_multi_line_bar.html")

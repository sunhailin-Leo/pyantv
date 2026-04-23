"""
双轴堆叠分组条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#dual-axis-stacked-grouped-bar
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

bar_data = [
    {"month": "Jan", "type": "线上", "value": 800},
    {"month": "Jan", "type": "线下", "value": 400},
    {"month": "Feb", "type": "线上", "value": 900},
    {"month": "Feb", "type": "线下", "value": 450},
    {"month": "Mar", "type": "线上", "value": 750},
    {"month": "Mar", "type": "线下", "value": 350},
    {"month": "Apr", "type": "线上", "value": 1000},
    {"month": "Apr", "type": "线下", "value": 450},
    {"month": "May", "type": "线上", "value": 1100},
    {"month": "May", "type": "线下", "value": 580},
    {"month": "Jun", "type": "线上", "value": 950},
    {"month": "Jun", "type": "线下", "value": 570},
]

line_data = [
    {"month": "Jan", "rate": 66.7},
    {"month": "Feb", "rate": 66.7},
    {"month": "Mar", "rate": 68.2},
    {"month": "Apr", "rate": 69.0},
    {"month": "May", "rate": 65.5},
    {"month": "Jun", "rate": 62.5},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="type")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="销售额")),
        ),
    )
)

line = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="month", y_field_name="rate")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="线上占比(%)")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#F6BD16", line_width=2),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="双轴堆叠分组条形图"))
)
chart.render("dual_axis_stacked_grouped_bar.html")

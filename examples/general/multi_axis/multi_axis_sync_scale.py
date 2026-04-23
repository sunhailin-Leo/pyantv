"""
多轴图同步刻度
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#multi-axis-sync-scale
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

data = [
    {"month": "Jan", "sales": 1200, "target": 1000},
    {"month": "Feb", "sales": 1350, "target": 1200},
    {"month": "Mar", "sales": 1100, "target": 1100},
    {"month": "Apr", "sales": 1450, "target": 1300},
    {"month": "May", "sales": 1680, "target": 1500},
    {"month": "Jun", "sales": 1520, "target": 1400},
    {"month": "Jul", "sales": 1890, "target": 1700},
    {"month": "Aug", "sales": 1750, "target": 1600},
]

bar = (
    Interval()
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="实际销售额")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

line = (
    Line()
    .set_encode(x_field_name="month", y_field_name="target")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="目标销售额")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#F6BD16", line_width=2),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar.options, line.options])
    .set_scale(
        y_scale_opts=opts.ScaleLinearOpts(domain_min=0, domain_max=2000, is_nice=True),
    )
    .set_global_options(title_opts=opts.TitleOpts(title="多轴图同步刻度"))
)
chart.render("multi_axis_sync_scale.html")

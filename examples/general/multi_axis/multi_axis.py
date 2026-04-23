"""
多轴图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#multi-axis
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line, Point

data = [
    {"month": "Jan", "revenue": 3500, "profit": 800, "rate": 22.9},
    {"month": "Feb", "revenue": 4200, "profit": 1100, "rate": 26.2},
    {"month": "Mar", "revenue": 3800, "profit": 900, "rate": 23.7},
    {"month": "Apr", "revenue": 5100, "profit": 1500, "rate": 29.4},
    {"month": "May", "revenue": 4800, "profit": 1300, "rate": 27.1},
    {"month": "Jun", "revenue": 5500, "profit": 1800, "rate": 32.7},
]

bar = (
    Interval()
    .set_encode(x_field_name="month", y_field_name="revenue")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="营收")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.6),
    )
)

line = (
    Line()
    .set_encode(x_field_name="month", y_field_name="profit")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="利润")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#5AD8A6", line_width=2),
    )
)

point = (
    Point()
    .set_encode(x_field_name="month", y_field_name="rate")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="利润率(%)")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#F6BD16"),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar.options, line.options, point.options])
    .set_global_options(title_opts=opts.TitleOpts(title="多轴图"))
)
chart.render("multi_axis.html")

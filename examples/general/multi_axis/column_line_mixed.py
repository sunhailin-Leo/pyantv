"""
柱线混合
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#column-line-mixed
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

data = [
    {"month": "Jan", "sales": 1200, "growth": 15},
    {"month": "Feb", "sales": 1350, "growth": 12.5},
    {"month": "Mar", "sales": 1100, "growth": -18.5},
    {"month": "Apr", "sales": 1450, "growth": 31.8},
    {"month": "May", "sales": 1680, "growth": 15.9},
    {"month": "Jun", "sales": 1520, "growth": -9.5},
    {"month": "Jul", "sales": 1890, "growth": 24.3},
    {"month": "Aug", "sales": 1750, "growth": -7.4},
    {"month": "Sep", "sales": 2100, "growth": 20},
    {"month": "Oct", "sales": 1950, "growth": -7.1},
    {"month": "Nov", "sales": 2300, "growth": 17.9},
    {"month": "Dec", "sales": 2500, "growth": 8.7},
]

bar = (
    Interval()
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="销售额")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

line = (
    Line()
    .set_encode(x_field_name="month", y_field_name="growth", shape_field="smooth")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="增长率(%)")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#5AD8A6", line_width=2),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="柱线混合"))
)
chart.render("column_line_mixed.html")

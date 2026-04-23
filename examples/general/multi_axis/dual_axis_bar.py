"""
双轴条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#dual-axis-bar
"""
from pyantv import options as opts
from pyantv.charts import View, Interval

data = [
    {"city": "北京", "population": 2154, "gdp": 36102},
    {"city": "上海", "population": 2487, "gdp": 38700},
    {"city": "广州", "population": 1867, "gdp": 25019},
    {"city": "深圳", "population": 1756, "gdp": 27670},
    {"city": "杭州", "population": 1193, "gdp": 16106},
    {"city": "成都", "population": 2093, "gdp": 17716},
]

bar1 = (
    Interval()
    .set_encode(x_field_name="city", y_field_name="population")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="人口(万)")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

bar2 = (
    Interval()
    .set_encode(x_field_name="city", y_field_name="gdp")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="GDP(亿)")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5AD8A6"),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar1.options, bar2.options])
    .set_global_options(title_opts=opts.TitleOpts(title="双轴条形图"))
)
chart.render("dual_axis_bar.html")

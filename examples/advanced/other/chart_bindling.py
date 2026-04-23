"""
图表联动
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#bindling
"""
from pyantv import options as opts
from pyantv.charts import SpaceFlex, Interval, Line

data = [
    {"month": "1月", "sales": 30, "profit": 10},
    {"month": "2月", "sales": 50, "profit": 20},
    {"month": "3月", "sales": 45, "profit": 15},
    {"month": "4月", "sales": 60, "profit": 25},
]

bar = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="sales")
)

line = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="profit")
)

chart = (
    SpaceFlex()
    .set_space_flex_children(children=[bar.options, line.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="图表联动"),
    )
)
chart.render("chart_bindling.html")

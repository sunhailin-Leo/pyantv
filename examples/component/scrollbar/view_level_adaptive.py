"""
View 层级自适应
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#view-level-adaptive
"""
from pyantv import options as opts
from pyantv.charts import Interval, Line, View

bar_data = [{"name": f"项目{i}", "sales": 20 + i * 3} for i in range(20)]
line_data = [{"name": f"项目{i}", "rate": 0.1 + i * 0.02} for i in range(20)]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="name", y_field_name="sales")
)

line = (
    Line()
    .set_data(data=line_data)
    .set_encode(x_field_name="name", y_field_name="rate")
    .set_global_options(style_opts=opts.BaseChartStyleOpts(stroke="red", line_width=2))
)

chart = (
    View()
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="View 层级自适应"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("view_level_adaptive.html")

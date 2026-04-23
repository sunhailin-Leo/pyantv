"""
Link 辅助线
G2 文档: https://g2.antv.antgroup.com/examples/general/connection/#link-auxiliary
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Link

bar_data = [
    {"type": "A", "value": 120},
    {"type": "B", "value": 90},
    {"type": "C", "value": 150},
    {"type": "D", "value": 80},
]

link_data = [
    {"x": ["A", "B"], "y": [120, 90]},
    {"x": ["B", "C"], "y": [90, 150]},
    {"x": ["C", "D"], "y": [150, 80]},
]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="type", y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

link = (
    Link()
    .set_data(data=link_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#F6BD16", line_width=1),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, link.options])
    .set_global_options(title_opts=opts.TitleOpts(title="Link 辅助线"))
)
chart.render("link_auxiliary.html")

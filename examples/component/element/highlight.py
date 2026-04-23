"""
高亮
G2 文档: https://g2.antv.antgroup.com/examples/interaction/element/#highlight
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="高亮"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("highlight.html")

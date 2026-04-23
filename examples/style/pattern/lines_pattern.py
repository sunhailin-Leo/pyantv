"""
Lines Pattern
G2 文档: https://g2.antv.antgroup.com/examples/style/pattern/#lines
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "A", "value": 30}, {"type": "B", "value": 50},
    {"type": "C", "value": 45}, {"type": "D", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="Lines Pattern"),
    )
)
chart.render("lines_pattern.html")

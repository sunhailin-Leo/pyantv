"""
2.5D 柱形图
G2 文档: https://g2.antv.antgroup.com/examples/fun/fun/#column-2-5d
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 55},
    {"name": "C", "value": 45}, {"name": "D", "value": 70},
    {"name": "E", "value": 60}, {"name": "F", "value": 40},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="2.5D 柱形图"),
    )
)
chart.render("column_2_5d.html")

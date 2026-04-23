"""
ScaleInX 动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#scale-in-x
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 55},
    {"name": "C", "value": 45}, {"name": "D", "value": 70},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="ScaleInX 动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("scale_in_x.html")

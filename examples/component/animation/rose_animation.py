"""
玫瑰图动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#rose-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "A", "value": 30}, {"type": "B", "value": 50},
    {"type": "C", "value": 45}, {"type": "D", "value": 60},
    {"type": "E", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="玫瑰图动画"),
        coordinate_opts=opts.CoordinatePolarOpts(),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("rose_animation.html")

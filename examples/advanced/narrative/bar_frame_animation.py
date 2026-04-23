"""
条帧动画
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/narrative/#bar-frame-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "中国", "value": 100}, {"name": "美国", "value": 90},
    {"name": "日本", "value": 70}, {"name": "德国", "value": 60},
    {"name": "英国", "value": 50},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="条帧动画"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("bar_frame_animation.html")

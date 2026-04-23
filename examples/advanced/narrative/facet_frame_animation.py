"""
分面帧动画
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/narrative/#facet-frame-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "type": "类型1", "value": 30},
    {"category": "B", "type": "类型1", "value": 50},
    {"category": "A", "type": "类型2", "value": 40},
    {"category": "B", "type": "类型2", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="分面帧动画"),
        transform_opts=[opts.TransformDodgeXOpts()],
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("facet_frame_animation.html")

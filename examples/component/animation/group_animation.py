"""
分组动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#group-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"city": "北京", "month": "1月", "value": 30},
    {"city": "北京", "month": "2月", "value": 45},
    {"city": "上海", "month": "1月", "value": 40},
    {"city": "上海", "month": "2月", "value": 50},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="分组动画"),
        animate_opts=opts.AnimateOpts(),
        transform_opts=[opts.TransformDodgeXOpts()],
    )
)
chart.render("group_animation.html")

"""
混合帧动画
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/narrative/#mixed-frame-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 50},
    {"month": "3月", "value": 45}, {"month": "4月", "value": 60},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 55},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="month")
    .set_global_options(
        title_opts=opts.TitleOpts(title="混合帧动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("mixed_frame_animation.html")

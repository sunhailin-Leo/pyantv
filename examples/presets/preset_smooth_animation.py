"""平滑动画预设示例。"""
from pyantv import Interval
from pyantv.presets import with_smooth_animation, with_auto_fit

data = [
    {"city": "北京", "sales": 120},
    {"city": "上海", "sales": 200},
    {"city": "广州", "sales": 150},
    {"city": "深圳", "sales": 180},
]

chart = (
    Interval.from_data(data=data, x_field_name="city", y_field_name="sales")
    .set_title("城市销售额")
)
with_smooth_animation(chart, duration=1500)
with_auto_fit(chart)
chart.render("preset_smooth_animation.html")

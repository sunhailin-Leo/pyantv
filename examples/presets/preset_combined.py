"""多预设组合示例：暗色主题 + 动画 + 自适应 + 极坐标。"""
from pyantv import Line
from pyantv.presets import (
    with_dark_theme,
    with_smooth_animation,
    with_auto_fit,
    with_polar,
)

data = [
    {"direction": "N", "speed": 12},
    {"direction": "NE", "speed": 8},
    {"direction": "E", "speed": 15},
    {"direction": "SE", "speed": 10},
    {"direction": "S", "speed": 6},
    {"direction": "SW", "speed": 9},
    {"direction": "W", "speed": 14},
    {"direction": "NW", "speed": 11},
]

chart = (
    Line.from_data(data=data, x_field_name="direction", y_field_name="speed")
    .set_title("风速雷达图")
)
with_dark_theme(chart)
with_smooth_animation(chart)
with_auto_fit(chart)
with_polar(chart)
chart.render("preset_combined.html")

"""暗色主题预设示例。"""
from pyantv import Line
from pyantv.presets import with_dark_theme, with_auto_fit

data = [
    {"month": "Jan", "value": 3},
    {"month": "Feb", "value": 4},
    {"month": "Mar", "value": 3.5},
    {"month": "Apr", "value": 5},
    {"month": "May", "value": 4.9},
    {"month": "Jun", "value": 6},
]

chart = (
    Line.from_data(data=data, x_field_name="month", y_field_name="value")
    .set_title("月度趋势 — 暗色主题")
)
with_dark_theme(chart)
with_auto_fit(chart)
chart.render("preset_dark_theme.html")

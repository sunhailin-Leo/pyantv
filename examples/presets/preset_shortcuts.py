"""快捷方法示例：set_title / set_padding / set_size。"""
from pyantv import Line

data = [
    {"quarter": "Q1", "revenue": 320},
    {"quarter": "Q2", "revenue": 450},
    {"quarter": "Q3", "revenue": 380},
    {"quarter": "Q4", "revenue": 520},
]

chart = (
    Line.from_data(data=data, x_field_name="quarter", y_field_name="revenue")
    .set_title("季度营收", subtitle="单位：万元")
    .set_padding(top=40, right=30, bottom=30, left=50)
    .set_size(width=800, height=500)
)
chart.render("preset_shortcuts.html")

"""
径向条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/radial/#radial-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "Python", "value": 100},
    {"name": "JavaScript", "value": 95},
    {"name": "Java", "value": 85},
    {"name": "C++", "value": 75},
    {"name": "Go", "value": 65},
    {"name": "Rust", "value": 55},
    {"name": "TypeScript", "value": 50},
    {"name": "Swift", "value": 40},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="径向条形图"),
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.1),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)
chart.render("radial_bar.html")

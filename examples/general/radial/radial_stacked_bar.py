"""
径向堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/radial/#radial-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "Jan", "type": "食品", "value": 85},
    {"month": "Jan", "type": "日用", "value": 65},
    {"month": "Feb", "type": "食品", "value": 90},
    {"month": "Feb", "type": "日用", "value": 70},
    {"month": "Mar", "type": "食品", "value": 100},
    {"month": "Mar", "type": "日用", "value": 80},
    {"month": "Apr", "type": "食品", "value": 110},
    {"month": "Apr", "type": "日用", "value": 85},
    {"month": "May", "type": "食品", "value": 120},
    {"month": "May", "type": "日用", "value": 90},
    {"month": "Jun", "type": "食品", "value": 115},
    {"month": "Jun", "type": "日用", "value": 88},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="径向堆叠条形图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.2),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)
chart.render("radial_stacked_bar.html")

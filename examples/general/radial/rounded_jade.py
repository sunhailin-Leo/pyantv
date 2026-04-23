"""
圆角玉珏图
G2 文档: https://g2.antv.antgroup.com/examples/general/radial/#rounded-jade
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "January", "value": 51},
    {"name": "February", "value": 91},
    {"name": "March", "value": 34},
    {"name": "April", "value": 47},
    {"name": "May", "value": 63},
    {"name": "June", "value": 58},
    {"name": "July", "value": 56},
    {"name": "August", "value": 77},
    {"name": "September", "value": 99},
    {"name": "October", "value": 106},
    {"name": "November", "value": 88},
    {"name": "December", "value": 56},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_interval_style(
        base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(radius=20),
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="圆角玉珏图"),
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.1),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)
chart.render("rounded_jade.html")

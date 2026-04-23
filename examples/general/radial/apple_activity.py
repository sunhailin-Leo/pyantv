"""
Apple 活动图
G2 文档: https://g2.antv.antgroup.com/examples/general/radial/#apple-activity
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "运动", "value": 0.75, "color": "#fa541c"},
    {"type": "锻炼", "value": 0.85, "color": "#a0d911"},
    {"type": "站立", "value": 0.65, "color": "#13c2c2"},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_interval_style(
        base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(radius=20),
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="Apple 活动图"),
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.3),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
        legend_opts=False,
    )
    .set_scale(
        y_scale_opts=opts.ScaleLinearOpts(domain_min=0, domain_max=1),
    )
)
chart.render("apple_activity.html")

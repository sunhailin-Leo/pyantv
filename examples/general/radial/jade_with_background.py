"""
带背景的玉珏图
G2 文档: https://g2.antv.antgroup.com/examples/general/radial/#jade-with-background
"""
from pyantv import options as opts
from pyantv.charts import Interval, SpaceLayer

data = [
    {"name": "January", "value": 51},
    {"name": "February", "value": 91},
    {"name": "March", "value": 34},
    {"name": "April", "value": 47},
    {"name": "May", "value": 63},
]

max_value = 120
bg_data = [{"name": item["name"], "value": max_value} for item in data]

background = (
    Interval()
    .set_data(data=bg_data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.1),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
        style_opts=opts.BaseChartStyleOpts(fill="#eee"),
    )
)

foreground = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.1),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)

chart = (
    SpaceLayer()
    .set_space_layer_children(children=[background.options, foreground.options])
    .set_global_options(title_opts=opts.TitleOpts(title="带背景的玉珏图"))
)
chart.render("jade_with_background.html")

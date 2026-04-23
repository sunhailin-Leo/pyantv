"""
子弹图
G2 文档: https://g2.antv.antgroup.com/examples/general/bullet/#bullet
"""
from pyantv import options as opts
from pyantv.charts import Interval, SpaceLayer

range_data = [{"title": "收入", "range": 100}]
target_data = [{"title": "收入", "target": 80}]
measure_data = [{"title": "收入", "measure": 65}]

range_bar = (
    Interval()
    .set_data(data=range_data)
    .set_encode(x_field_name="title", y_field_name="range")
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartStyleOpts(fill="#eee"),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)

measure_bar = (
    Interval()
    .set_data(data=measure_data)
    .set_encode(x_field_name="title", y_field_name="measure")
    .set_interval_style(max_width=20)
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
        axis_opts=opts.AxisOpts(y_axis_opts=False),
    )
)

chart = (
    SpaceLayer()
    .set_space_layer_children(children=[range_bar.options, measure_bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="子弹图"))
)
chart.render("bullet.html")

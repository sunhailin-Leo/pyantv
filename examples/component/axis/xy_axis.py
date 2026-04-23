"""
x 和 y 方向坐标轴
G2 文档: https://g2.antv.antgroup.com/examples/component/axis/#xy-axis
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="x 和 y 方向坐标轴"),
        axis_opts={
            "x": opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="类别"),
            ),
            "y": opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="数值"),
            ),
        },
    )
)
chart.render("xy_axis.html")

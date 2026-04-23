"""
迷你进度条
G2 文档: https://g2.antv.antgroup.com/examples/general/mini/#mini-progress
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "已完成", "value": 75},
    {"type": "未完成", "value": 25},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="迷你进度条"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        axis_opts=opts.AxisOpts(x_axis_opts=False, y_axis_opts=False),
        legend_opts=False,
    )
)
chart.render("mini_progress.html")

"""
迷你饼图
G2 文档: https://g2.antv.antgroup.com/examples/general/mini/#mini-pie
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "分类A", "value": 40},
    {"type": "分类B", "value": 30},
    {"type": "分类C", "value": 20},
    {"type": "分类D", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="迷你饼图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(),
        axis_opts=opts.AxisOpts(x_axis_opts=False, y_axis_opts=False),
        legend_opts=False,
    )
)
chart.render("mini_pie.html")

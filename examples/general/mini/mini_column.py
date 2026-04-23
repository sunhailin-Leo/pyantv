"""
迷你柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/mini/#mini-column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"x": "周一", "y": 30},
    {"x": "周二", "y": 50},
    {"x": "周三", "y": 45},
    {"x": "周四", "y": 60},
    {"x": "周五", "y": 55},
    {"x": "周六", "y": 70},
    {"x": "周日", "y": 65},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="迷你柱形图"),
        axis_opts=opts.AxisOpts(x_axis_opts=False, y_axis_opts=False),
    )
)
chart.render("mini_column.html")

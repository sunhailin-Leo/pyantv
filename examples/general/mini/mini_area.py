"""
迷你面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/mini/#mini-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"x": 0, "y": 20},
    {"x": 1, "y": 35},
    {"x": 2, "y": 30},
    {"x": 3, "y": 50},
    {"x": 4, "y": 45},
    {"x": 5, "y": 60},
    {"x": 6, "y": 55},
    {"x": 7, "y": 70},
    {"x": 8, "y": 65},
    {"x": 9, "y": 80},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="迷你面积图"),
        axis_opts=opts.AxisOpts(x_axis_opts=False, y_axis_opts=False),
    )
)
chart.render("mini_area.html")

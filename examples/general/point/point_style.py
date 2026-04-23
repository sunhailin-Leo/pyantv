"""
point 样式
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#point-style
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"x": 1, "y": 4.5, "size": 10},
    {"x": 2, "y": 3.8, "size": 15},
    {"x": 3, "y": 5.2, "size": 20},
    {"x": 4, "y": 4.1, "size": 25},
    {"x": 5, "y": 6.0, "size": 30},
    {"x": 6, "y": 3.5, "size": 18},
    {"x": 7, "y": 5.8, "size": 22},
    {"x": 8, "y": 4.3, "size": 28},
    {"x": 9, "y": 6.5, "size": 35},
    {"x": 10, "y": 5.0, "size": 12},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="size")
    .set_global_options(
        title_opts=opts.TitleOpts(title="point 样式"),
        style_opts=opts.BaseChartStyleOpts(
            fill="#5B8FF9",
            fill_opacity=0.5,
            stroke="#5B8FF9",
            line_width=2,
        ),
    )
)
chart.render("point_style.html")

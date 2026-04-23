"""
复杂雷达图
G2 文档: https://g2.antv.antgroup.com/examples/general/radar/#complex-radar
"""
from pyantv import options as opts
from pyantv.charts import View, Area, Line, Point

data = [
    {"item": "设计", "type": "A", "score": 70},
    {"item": "开发", "type": "A", "score": 60},
    {"item": "市场", "type": "A", "score": 50},
    {"item": "用户", "type": "A", "score": 40},
    {"item": "技术", "type": "A", "score": 65},
    {"item": "管理", "type": "A", "score": 55},
    {"item": "设计", "type": "B", "score": 50},
    {"item": "开发", "type": "B", "score": 80},
    {"item": "市场", "type": "B", "score": 60},
    {"item": "用户", "type": "B", "score": 70},
    {"item": "技术", "type": "B", "score": 45},
    {"item": "管理", "type": "B", "score": 75},
]

area = (
    Area()
    .set_encode(x_field_name="item", y_field_name="score", color_field="type")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.3),
    )
)

line = (
    Line()
    .set_encode(x_field_name="item", y_field_name="score", color_field="type")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(line_width=2),
    )
)

point = (
    Point()
    .set_encode(x_field_name="item", y_field_name="score", color_field="type")
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[area.options, line.options, point.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="复杂雷达图"),
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("complex_radar.html")

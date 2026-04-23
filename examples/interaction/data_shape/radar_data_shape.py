"""
雷达图-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#radar
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"item": "设计", "user": "用户A", "score": 70},
    {"item": "开发", "user": "用户A", "score": 60},
    {"item": "营销", "user": "用户A", "score": 50},
    {"item": "运营", "user": "用户A", "score": 40},
    {"item": "技术", "user": "用户A", "score": 80},
    {"item": "设计", "user": "用户B", "score": 50},
    {"item": "开发", "user": "用户B", "score": 70},
    {"item": "营销", "user": "用户B", "score": 60},
    {"item": "运营", "user": "用户B", "score": 80},
    {"item": "技术", "user": "用户B", "score": 55},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="item", y_field_name="score", color_field="user")
    .set_global_options(
        title_opts=opts.TitleOpts(title="雷达图-数形交互"),
        coordinate_opts=opts.CoordinatePolarOpts(),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("radar_data_shape.html")

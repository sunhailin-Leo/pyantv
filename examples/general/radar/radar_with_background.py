"""
雷达图(带底色)
G2 文档: https://g2.antv.antgroup.com/examples/general/radar/#radar-with-background
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"item": "设计", "score": 70},
    {"item": "开发", "score": 60},
    {"item": "市场", "score": 50},
    {"item": "用户", "score": 40},
    {"item": "技术", "score": 65},
    {"item": "管理", "score": 55},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="item", y_field_name="score")
    .set_global_options(
        title_opts=opts.TitleOpts(title="雷达图(带底色)"),
        coordinate_opts=opts.CoordinatePolarOpts(),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5),
    )
)
chart.render("radar_with_background.html")

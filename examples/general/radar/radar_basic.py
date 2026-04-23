"""
雷达图(基础)
G2 文档: https://g2.antv.antgroup.com/examples/general/radar/#radar-basic
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"item": "攻击", "score": 80},
    {"item": "防御", "score": 65},
    {"item": "速度", "score": 90},
    {"item": "体力", "score": 70},
    {"item": "智力", "score": 85},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="item", y_field_name="score")
    .set_global_options(
        title_opts=opts.TitleOpts(title="雷达图(基础)"),
        coordinate_opts=opts.CoordinatePolarOpts(),
        style_opts=opts.BaseChartStyleOpts(line_width=2),
    )
)
chart.render("radar_basic.html")

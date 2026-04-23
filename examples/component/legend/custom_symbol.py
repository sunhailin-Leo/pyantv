"""
自定义符号
G2 文档: https://g2.antv.antgroup.com/examples/component/legend/#custom-symbol
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"x": 10, "y": 20, "type": "A"},
    {"x": 20, "y": 35, "type": "A"},
    {"x": 30, "y": 25, "type": "B"},
    {"x": 40, "y": 45, "type": "B"},
    {"x": 50, "y": 30, "type": "C"},
    {"x": 60, "y": 50, "type": "C"},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义符号"),
    )
)
chart.render("custom_symbol.html")

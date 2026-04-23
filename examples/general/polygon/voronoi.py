"""
沃罗诺伊图
G2 文档: https://g2.antv.antgroup.com/examples/general/polygon/#voronoi
"""
from pyantv import options as opts
from pyantv.charts import Polygon

data = [
    {"x": [0, 0.5, 0.3], "y": [0, 0.2, 0.5], "value": 10, "name": "A"},
    {"x": [0.5, 1, 0.8, 0.3], "y": [0.2, 0, 0.4, 0.5], "value": 20, "name": "B"},
    {"x": [0, 0.3, 0.2], "y": [0.5, 0.5, 1], "value": 15, "name": "C"},
    {"x": [0.3, 0.8, 0.6, 0.2], "y": [0.5, 0.4, 0.8, 1], "value": 25, "name": "D"},
    {"x": [0.8, 1, 0.9, 0.6], "y": [0.4, 0.5, 1, 0.8], "value": 18, "name": "E"},
]

chart = (
    Polygon()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="沃罗诺伊图"),
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)
chart.render("voronoi.html")

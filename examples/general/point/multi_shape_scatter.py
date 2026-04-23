"""
多形状散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#multi-shape-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"x": 1, "y": 4.5, "category": "A"},
    {"x": 2, "y": 3.8, "category": "A"},
    {"x": 3, "y": 5.2, "category": "A"},
    {"x": 4, "y": 4.1, "category": "A"},
    {"x": 5, "y": 6.0, "category": "A"},
    {"x": 1.5, "y": 3.2, "category": "B"},
    {"x": 2.5, "y": 4.5, "category": "B"},
    {"x": 3.5, "y": 2.8, "category": "B"},
    {"x": 4.5, "y": 5.5, "category": "B"},
    {"x": 5.5, "y": 3.9, "category": "B"},
    {"x": 1.2, "y": 5.8, "category": "C"},
    {"x": 2.8, "y": 6.2, "category": "C"},
    {"x": 3.2, "y": 4.8, "category": "C"},
    {"x": 4.8, "y": 7.0, "category": "C"},
    {"x": 5.2, "y": 5.5, "category": "C"},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="category", shape_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="多形状散点图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.65),
    )
)
chart.render("multi_shape_scatter.html")

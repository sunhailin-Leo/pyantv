"""
渐变色散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#gradient-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"x": 10, "y": 8, "temperature": 15},
    {"x": 20, "y": 12, "temperature": 22},
    {"x": 30, "y": 18, "temperature": 28},
    {"x": 40, "y": 25, "temperature": 35},
    {"x": 50, "y": 30, "temperature": 40},
    {"x": 15, "y": 10, "temperature": 18},
    {"x": 25, "y": 15, "temperature": 25},
    {"x": 35, "y": 22, "temperature": 32},
    {"x": 45, "y": 28, "temperature": 38},
    {"x": 55, "y": 35, "temperature": 42},
    {"x": 12, "y": 6, "temperature": 12},
    {"x": 22, "y": 14, "temperature": 20},
    {"x": 32, "y": 20, "temperature": 30},
    {"x": 42, "y": 26, "temperature": 36},
    {"x": 52, "y": 32, "temperature": 41},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="temperature")
    .set_global_options(
        title_opts=opts.TitleOpts(title="渐变色散点图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.7),
    )
)
chart.render("gradient_scatter.html")

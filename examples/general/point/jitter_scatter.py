"""
扰动散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#jitter-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"genre": "Sports", "sold": 275},
    {"genre": "Sports", "sold": 320},
    {"genre": "Sports", "sold": 295},
    {"genre": "Sports", "sold": 310},
    {"genre": "Sports", "sold": 280},
    {"genre": "Strategy", "sold": 115},
    {"genre": "Strategy", "sold": 130},
    {"genre": "Strategy", "sold": 125},
    {"genre": "Strategy", "sold": 140},
    {"genre": "Strategy", "sold": 120},
    {"genre": "Action", "sold": 350},
    {"genre": "Action", "sold": 380},
    {"genre": "Action", "sold": 365},
    {"genre": "Action", "sold": 390},
    {"genre": "Action", "sold": 370},
    {"genre": "Shooter", "sold": 230},
    {"genre": "Shooter", "sold": 250},
    {"genre": "Shooter", "sold": 245},
    {"genre": "Shooter", "sold": 260},
    {"genre": "Shooter", "sold": 240},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="genre", y_field_name="sold", color_field="genre")
    .set_global_options(
        transform_opts=[opts.TransformJitterXOpts()],
        title_opts=opts.TitleOpts(title="扰动散点图"),
    )
)
chart.render("jitter_scatter.html")

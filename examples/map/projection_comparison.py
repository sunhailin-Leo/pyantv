"""
投影比较
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#projection-comparison
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"city": "北京", "lon": 116.4, "lat": 39.9},
    {"city": "纽约", "lon": -74.0, "lat": 40.7},
    {"city": "伦敦", "lon": -0.1, "lat": 51.5},
    {"city": "东京", "lon": 139.7, "lat": 35.7},
    {"city": "悉尼", "lon": 151.2, "lat": -33.9},
    {"city": "圣保罗", "lon": -46.6, "lat": -23.5},
    {"city": "开罗", "lon": 31.2, "lat": 30.0},
    {"city": "莫斯科", "lon": 37.6, "lat": 55.8},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="lon", y_field_name="lat", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="投影比较"),
    )
)
chart.render("projection_comparison.html")

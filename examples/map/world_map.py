"""
世界地图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#world-map
"""
from pyantv import options as opts
from pyantv.charts import GeoView

data = [
    {"country": "中国", "value": 1400, "lon": 104.2, "lat": 35.9},
    {"country": "美国", "value": 330, "lon": -95.7, "lat": 37.1},
    {"country": "印度", "value": 1380, "lon": 78.9, "lat": 20.6},
    {"country": "巴西", "value": 213, "lon": -51.9, "lat": -14.2},
    {"country": "俄罗斯", "value": 146, "lon": 105.3, "lat": 61.5},
    {"country": "日本", "value": 126, "lon": 138.3, "lat": 36.2},
    {"country": "德国", "value": 83, "lon": 10.5, "lat": 51.2},
    {"country": "英国", "value": 67, "lon": -3.4, "lat": 55.4},
]

chart = (
    GeoView()
    .set_data(data=data)
    .set_encode(x_field_name="lon", y_field_name="lat", color_field="value", size_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="世界地图"),
    )
)
chart.render("world_map.html")

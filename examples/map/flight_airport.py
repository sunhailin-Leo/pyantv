"""
航班机场图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#flight-airport
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"airport": "PEK", "city": "北京", "lon": 116.6, "lat": 40.1, "flights": 580},
    {"airport": "PVG", "city": "上海", "lon": 121.8, "lat": 31.1, "flights": 520},
    {"airport": "CAN", "city": "广州", "lon": 113.3, "lat": 23.4, "flights": 450},
    {"airport": "CTU", "city": "成都", "lon": 103.9, "lat": 30.6, "flights": 400},
    {"airport": "SZX", "city": "深圳", "lon": 113.8, "lat": 22.6, "flights": 380},
    {"airport": "SHA", "city": "上海虹桥", "lon": 121.3, "lat": 31.2, "flights": 350},
    {"airport": "KMG", "city": "昆明", "lon": 102.7, "lat": 24.9, "flights": 320},
    {"airport": "XIY", "city": "西安", "lon": 108.8, "lat": 34.4, "flights": 300},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="lon", y_field_name="lat", size_field="flights", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="航班机场图"),
    )
)
chart.render("flight_airport.html")

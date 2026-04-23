"""
美国行政地图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#bindbindbindus-administrative
"""
from pyantv import options as opts
from pyantv.charts import GeoView

data = [
    {"state": "California", "value": 39538223, "lon": -119.4, "lat": 36.8},
    {"state": "Texas", "value": 29145505, "lon": -99.9, "lat": 31.9},
    {"state": "Florida", "value": 21538187, "lon": -81.5, "lat": 27.6},
    {"state": "New York", "value": 20201249, "lon": -75.0, "lat": 43.0},
    {"state": "Pennsylvania", "value": 13002700, "lon": -77.2, "lat": 41.2},
]

chart = (
    GeoView()
    .set_data(data=data)
    .set_encode(x_field_name="lon", y_field_name="lat", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="美国行政地图"),
    )
)
chart.render("us_administrative.html")

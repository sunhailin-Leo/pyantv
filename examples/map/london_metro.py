"""
伦敦地铁图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#london-metro
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"station": "King's Cross", "line": "Victoria", "lon": -0.124, "lat": 51.530},
    {"station": "Oxford Circus", "line": "Victoria", "lon": -0.142, "lat": 51.515},
    {"station": "Victoria", "line": "Victoria", "lon": -0.144, "lat": 51.496},
    {"station": "Brixton", "line": "Victoria", "lon": -0.114, "lat": 51.462},
    {"station": "Baker Street", "line": "Metropolitan", "lon": -0.157, "lat": 51.523},
    {"station": "Liverpool Street", "line": "Metropolitan", "lon": -0.083, "lat": 51.517},
    {"station": "Paddington", "line": "Circle", "lon": -0.175, "lat": 51.516},
    {"station": "Westminster", "line": "Circle", "lon": -0.125, "lat": 51.501},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="lon", y_field_name="lat", color_field="line")
    .set_global_options(
        title_opts=opts.TitleOpts(title="伦敦地铁图"),
    )
)
chart.render("london_metro.html")

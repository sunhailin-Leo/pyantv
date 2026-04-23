"""
对数气泡图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#log-bubble
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"country": "China", "gdp": 14700, "co2": 10065, "population": 1402},
    {"country": "USA", "gdp": 21400, "co2": 5416, "population": 331},
    {"country": "India", "gdp": 2900, "co2": 2654, "population": 1380},
    {"country": "Russia", "gdp": 1500, "co2": 1711, "population": 144},
    {"country": "Japan", "gdp": 5100, "co2": 1162, "population": 126},
    {"country": "Germany", "gdp": 3800, "co2": 759, "population": 83},
    {"country": "South Korea", "gdp": 1600, "co2": 616, "population": 52},
    {"country": "Canada", "gdp": 1600, "co2": 568, "population": 38},
    {"country": "Brazil", "gdp": 1400, "co2": 462, "population": 212},
    {"country": "UK", "gdp": 2700, "co2": 379, "population": 67},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(
        x_field_name="gdp",
        y_field_name="co2",
        size_field="population",
        color_field="country",
    )
    .set_scale(
        x_scale_opts=opts.ScaleLogOpts(),
        y_scale_opts=opts.ScaleLogOpts(),
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="对数气泡图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.6),
    )
)
chart.render("log_bubble.html")

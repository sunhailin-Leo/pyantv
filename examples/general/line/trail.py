"""
轨迹图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#trail
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2000", "country": "China", "value": 1200, "population": 1267},
    {"year": "2005", "country": "China", "value": 2300, "population": 1303},
    {"year": "2010", "country": "China", "value": 6100, "population": 1337},
    {"year": "2015", "country": "China", "value": 11000, "population": 1371},
    {"year": "2020", "country": "China", "value": 14700, "population": 1402},
    {"year": "2000", "country": "USA", "value": 10300, "population": 282},
    {"year": "2005", "country": "USA", "value": 13000, "population": 295},
    {"year": "2010", "country": "USA", "value": 15000, "population": 309},
    {"year": "2015", "country": "USA", "value": 18200, "population": 321},
    {"year": "2020", "country": "USA", "value": 21400, "population": 331},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(
        x_field_name="year",
        y_field_name="value",
        color_field="country",
        size_field="population",
        shape_field="trail"
    )
    .set_global_options(title_opts=opts.TitleOpts(title="轨迹图"))
)
chart.render("trail.html")

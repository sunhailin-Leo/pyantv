"""
水平条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#horizontal
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"country": "China", "population": 1402},
    {"country": "India", "population": 1380},
    {"country": "USA", "population": 331},
    {"country": "Indonesia", "population": 273},
    {"country": "Pakistan", "population": 220},
    {"country": "Brazil", "population": 212},
    {"country": "Nigeria", "population": 206},
    {"country": "Bangladesh", "population": 164},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="country", y_field_name="population")
    .set_coordinate(coordinate_opts=opts.CoordinateTransposeOpts())
    .set_global_options(
        title_opts=opts.TitleOpts(title="水平条形图"),
    )
)
chart.render("horizontal_bar.html")

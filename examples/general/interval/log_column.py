"""
对数柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#bindlog
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"country": "China", "population": 1402000000},
    {"country": "India", "population": 1380000000},
    {"country": "USA", "population": 331000000},
    {"country": "Indonesia", "population": 273000000},
    {"country": "Brazil", "population": 212000000},
    {"country": "Pakistan", "population": 220000000},
    {"country": "Nigeria", "population": 206000000},
    {"country": "Bangladesh", "population": 164000000},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="country", y_field_name="population")
    .set_scale(y_scale_opts=opts.ScaleLogOpts())
    .set_global_options(
        title_opts=opts.TitleOpts(title="对数柱形图"),
    )
)
chart.render("log_column.html")

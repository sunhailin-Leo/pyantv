"""
标签散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#label-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"country": "China", "gdp": 14700, "population": 1402},
    {"country": "USA", "gdp": 21400, "population": 331},
    {"country": "Japan", "gdp": 5100, "population": 126},
    {"country": "Germany", "gdp": 3800, "population": 83},
    {"country": "UK", "gdp": 2700, "population": 67},
    {"country": "India", "gdp": 2900, "population": 1380},
    {"country": "France", "gdp": 2600, "population": 67},
    {"country": "Brazil", "gdp": 1400, "population": 212},
    {"country": "Canada", "gdp": 1600, "population": 38},
    {"country": "Russia", "gdp": 1500, "population": 144},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="gdp", y_field_name="population")
    .set_global_options(
        title_opts=opts.TitleOpts(title="标签散点图"),
        label_opts=[opts.LabelOpts(text_opts="country")],
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.65),
    )
)
chart.render("label_scatter.html")

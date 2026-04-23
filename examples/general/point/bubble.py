"""
气泡图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#bubble
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"country": "China", "gdp": 14700, "life_expectancy": 77, "population": 1402},
    {"country": "USA", "gdp": 21400, "life_expectancy": 79, "population": 331},
    {"country": "Japan", "gdp": 5100, "life_expectancy": 84, "population": 126},
    {"country": "Germany", "gdp": 3800, "life_expectancy": 81, "population": 83},
    {"country": "UK", "gdp": 2700, "life_expectancy": 81, "population": 67},
    {"country": "India", "gdp": 2900, "life_expectancy": 70, "population": 1380},
    {"country": "France", "gdp": 2600, "life_expectancy": 83, "population": 67},
    {"country": "Brazil", "gdp": 1400, "life_expectancy": 76, "population": 212},
    {"country": "Canada", "gdp": 1600, "life_expectancy": 82, "population": 38},
    {"country": "Russia", "gdp": 1500, "life_expectancy": 73, "population": 144},
    {"country": "Australia", "gdp": 1400, "life_expectancy": 83, "population": 26},
    {"country": "South Korea", "gdp": 1600, "life_expectancy": 83, "population": 52},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(
        x_field_name="gdp",
        y_field_name="life_expectancy",
        size_field="population",
        color_field="country",
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="气泡图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.6),
    )
)
chart.render("bubble.html")

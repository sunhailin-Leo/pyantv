"""
百分比堆叠柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#percent-stacked-column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"country": "Europe", "year": "1750", "value": 163},
    {"country": "Europe", "year": "1800", "value": 203},
    {"country": "Europe", "year": "1850", "value": 276},
    {"country": "Europe", "year": "1900", "value": 408},
    {"country": "Europe", "year": "1950", "value": 547},
    {"country": "Europe", "year": "1999", "value": 729},
    {"country": "Europe", "year": "2050", "value": 628},
    {"country": "Asia", "year": "1750", "value": 502},
    {"country": "Asia", "year": "1800", "value": 635},
    {"country": "Asia", "year": "1850", "value": 809},
    {"country": "Asia", "year": "1900", "value": 947},
    {"country": "Asia", "year": "1950", "value": 1402},
    {"country": "Asia", "year": "1999", "value": 3634},
    {"country": "Asia", "year": "2050", "value": 5268},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="country")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts(), opts.TransformNormalizeYOpts()],
        title_opts=opts.TitleOpts(title="百分比堆叠柱形图"),
    )
)

chart.render("percent_stacked_column.html")

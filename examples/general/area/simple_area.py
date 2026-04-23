"""
简单面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#simple-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "1991", "value": 3},
    {"year": "1992", "value": 4},
    {"year": "1993", "value": 3.5},
    {"year": "1994", "value": 5},
    {"year": "1995", "value": 4.9},
    {"year": "1996", "value": 6},
    {"year": "1997", "value": 7},
    {"year": "1998", "value": 9},
    {"year": "1999", "value": 13},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(title_opts=opts.TitleOpts(title="简单面积图"))
)
chart.render("simple_area.html")

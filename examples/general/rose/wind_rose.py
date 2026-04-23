"""
Wind Rose
G2 文档: https://g2.antv.antgroup.com/examples/general/rose/#wind-rose
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"direction": "N", "level": "0-2", "value": 5},
    {"direction": "N", "level": "2-4", "value": 8},
    {"direction": "N", "level": "4-6", "value": 3},
    {"direction": "NE", "level": "0-2", "value": 7},
    {"direction": "NE", "level": "2-4", "value": 10},
    {"direction": "NE", "level": "4-6", "value": 5},
    {"direction": "E", "level": "0-2", "value": 6},
    {"direction": "E", "level": "2-4", "value": 9},
    {"direction": "E", "level": "4-6", "value": 4},
    {"direction": "SE", "level": "0-2", "value": 8},
    {"direction": "SE", "level": "2-4", "value": 12},
    {"direction": "SE", "level": "4-6", "value": 6},
    {"direction": "S", "level": "0-2", "value": 4},
    {"direction": "S", "level": "2-4", "value": 7},
    {"direction": "S", "level": "4-6", "value": 2},
    {"direction": "SW", "level": "0-2", "value": 3},
    {"direction": "SW", "level": "2-4", "value": 5},
    {"direction": "SW", "level": "4-6", "value": 2},
    {"direction": "W", "level": "0-2", "value": 5},
    {"direction": "W", "level": "2-4", "value": 6},
    {"direction": "W", "level": "4-6", "value": 3},
    {"direction": "NW", "level": "0-2", "value": 6},
    {"direction": "NW", "level": "2-4", "value": 8},
    {"direction": "NW", "level": "4-6", "value": 4},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="direction", y_field_name="value", color_field="level")
    .set_global_options(
        title_opts=opts.TitleOpts(title="Wind Rose"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("wind_rose.html")

"""
河流图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#stream
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "2000", "type": "Rock", "value": 120},
    {"year": "2000", "type": "Pop", "value": 200},
    {"year": "2000", "type": "Jazz", "value": 80},
    {"year": "2000", "type": "Classical", "value": 60},
    {"year": "2005", "type": "Rock", "value": 150},
    {"year": "2005", "type": "Pop", "value": 250},
    {"year": "2005", "type": "Jazz", "value": 90},
    {"year": "2005", "type": "Classical", "value": 55},
    {"year": "2010", "type": "Rock", "value": 130},
    {"year": "2010", "type": "Pop", "value": 300},
    {"year": "2010", "type": "Jazz", "value": 70},
    {"year": "2010", "type": "Classical", "value": 50},
    {"year": "2015", "type": "Rock", "value": 100},
    {"year": "2015", "type": "Pop", "value": 350},
    {"year": "2015", "type": "Jazz", "value": 65},
    {"year": "2015", "type": "Classical", "value": 45},
    {"year": "2020", "type": "Rock", "value": 80},
    {"year": "2020", "type": "Pop", "value": 400},
    {"year": "2020", "type": "Jazz", "value": 60},
    {"year": "2020", "type": "Classical", "value": 40},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="河流图"),
        transform_opts=[opts.TransformStackYOpts(), opts.TransformSymmetryYOpts()],
    )
)
chart.render("stream.html")

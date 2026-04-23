"""
六边形美国地图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#hex-us-map
"""
from pyantv import options as opts
from pyantv.charts import Polygon

data = [
    {"state": "CA", "row": 5, "col": 0, "value": 39},
    {"state": "TX", "row": 7, "col": 3, "value": 29},
    {"state": "FL", "row": 8, "col": 8, "value": 22},
    {"state": "NY", "row": 2, "col": 9, "value": 20},
    {"state": "PA", "row": 3, "col": 8, "value": 13},
    {"state": "IL", "row": 3, "col": 5, "value": 13},
    {"state": "OH", "row": 3, "col": 7, "value": 12},
    {"state": "GA", "row": 6, "col": 7, "value": 11},
]

chart = (
    Polygon()
    .set_data(data=data)
    .set_encode(x_field_name="col", y_field_name="row", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="六边形美国地图"),
    )
)
chart.render("hex_us_map.html")

"""
六边形中国地图
G2 文档: https://g2.antv.antgroup.com/examples/geo/geo/#hex-china-map
"""
from pyantv import options as opts
from pyantv.charts import Polygon

data = [
    {"province": "广东", "row": 6, "col": 6, "value": 126},
    {"province": "江苏", "row": 4, "col": 7, "value": 85},
    {"province": "山东", "row": 3, "col": 7, "value": 83},
    {"province": "浙江", "row": 5, "col": 7, "value": 65},
    {"province": "河南", "row": 4, "col": 6, "value": 62},
    {"province": "四川", "row": 5, "col": 4, "value": 54},
    {"province": "湖北", "row": 5, "col": 5, "value": 50},
    {"province": "湖南", "row": 6, "col": 5, "value": 47},
    {"province": "河北", "row": 3, "col": 6, "value": 40},
    {"province": "福建", "row": 6, "col": 7, "value": 42},
]

chart = (
    Polygon()
    .set_data(data=data)
    .set_encode(x_field_name="col", y_field_name="row", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="六边形中国地图"),
    )
)
chart.render("hex_china_map.html")

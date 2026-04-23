"""
图标标记
G2 文档: https://g2.antv.antgroup.com/examples/general/image/#icon-marker
"""
from pyantv import options as opts
from pyantv.charts import Image

data = [
    {"name": "北京", "x": 116.4, "y": 39.9},
    {"name": "上海", "x": 121.5, "y": 31.2},
    {"name": "广州", "x": 113.3, "y": 23.1},
    {"name": "深圳", "x": 114.1, "y": 22.5},
]

chart = (
    Image()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="图标标记"),
    )
)
chart.render("icon_marker.html")

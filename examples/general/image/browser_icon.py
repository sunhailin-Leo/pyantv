"""
浏览器图标
G2 文档: https://g2.antv.antgroup.com/examples/general/image/#browser-icon
"""
from pyantv import options as opts
from pyantv.charts import Image

data = [
    {"name": "Chrome", "value": 65, "x": 0, "y": 0},
    {"name": "Firefox", "value": 15, "x": 1, "y": 0},
    {"name": "Safari", "value": 10, "x": 2, "y": 0},
    {"name": "Edge", "value": 5, "x": 3, "y": 0},
    {"name": "Opera", "value": 3, "x": 4, "y": 0},
]

chart = (
    Image()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="浏览器图标"),
    )
)
chart.render("browser_icon.html")

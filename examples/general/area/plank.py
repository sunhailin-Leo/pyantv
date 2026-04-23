"""
板子图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#plank
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"category": "A", "value": 85},
    {"category": "B", "value": 72},
    {"category": "C", "value": 63},
    {"category": "D", "value": 55},
    {"category": "E", "value": 48},
    {"category": "F", "value": 35},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="板子图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.6),
    )
)
chart.render("plank.html")

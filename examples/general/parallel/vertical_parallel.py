"""
竖直平行坐标系
G2 文档: https://g2.antv.antgroup.com/examples/general/parallel/#vertical-parallel
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"name": "A", "cpu": 80, "memory": 60, "disk": 40, "network": 70},
    {"name": "B", "cpu": 65, "memory": 75, "disk": 55, "network": 85},
    {"name": "C", "cpu": 90, "memory": 50, "disk": 70, "network": 60},
    {"name": "D", "cpu": 55, "memory": 85, "disk": 65, "network": 45},
    {"name": "E", "cpu": 70, "memory": 70, "disk": 80, "network": 75},
]

position_data = []
for item in data:
    for key in ["cpu", "memory", "disk", "network"]:
        position_data.append({"name": item["name"], "dimension": key, "value": item[key]})

chart = (
    Line()
    .set_data(data=position_data)
    .set_encode(x_field_name="dimension", y_field_name="value", color_field="name", series_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="竖直平行坐标系"),
        style_opts=opts.BaseChartStyleOpts(line_width=1.5, stroke_opacity=0.6),
    )
)
chart.render("vertical_parallel.html")

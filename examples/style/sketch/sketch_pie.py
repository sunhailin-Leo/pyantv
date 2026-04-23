"""
手绘饼图
G2 文档: https://g2.antv.antgroup.com/examples/style/sketch/#pie
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "A", "value": 30}, {"type": "B", "value": 25},
    {"type": "C", "value": 20}, {"type": "D", "value": 15},
    {"type": "E", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="手绘饼图"),
        coordinate_opts=opts.CoordinateThetaOpts(),
        transform_opts=[opts.TransformStackYOpts()],
    )
)
chart.render("sketch_pie.html")

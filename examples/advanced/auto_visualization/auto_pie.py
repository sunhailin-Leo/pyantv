"""
自动可视化 - 饼图
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/auto/#pie
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "分类A", "value": 30}, {"type": "分类B", "value": 25},
    {"type": "分类C", "value": 20}, {"type": "分类D", "value": 15},
    {"type": "分类E", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自动可视化 - 饼图"),
        coordinate_opts=opts.CoordinateThetaOpts(),
        transform_opts=[opts.TransformStackYOpts()],
    )
)
chart.render("auto_pie.html")

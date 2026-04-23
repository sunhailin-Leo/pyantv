"""
饼图元素放大
G2 文档: https://g2.antv.antgroup.com/examples/interaction/element/#pie-element-enlarge
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
        title_opts=opts.TitleOpts(title="饼图元素放大"),
        coordinate_opts=opts.CoordinateThetaOpts(),
        transform_opts=[opts.TransformStackYOpts()],
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("pie_element_enlarge.html")

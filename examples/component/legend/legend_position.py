"""
图例位置
G2 文档: https://g2.antv.antgroup.com/examples/component/legend/#legend-position
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 30, "type": "类型1"},
    {"category": "B", "value": 50, "type": "类型1"},
    {"category": "A", "value": 40, "type": "类型2"},
    {"category": "B", "value": 60, "type": "类型2"},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="图例位置"),
        transform_opts=[opts.TransformDodgeXOpts()],
    )
)
chart.render("legend_position.html")

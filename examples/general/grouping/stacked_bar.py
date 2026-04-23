"""
层叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "type": "类型1", "value": 30},
    {"category": "A", "type": "类型2", "value": 20},
    {"category": "B", "type": "类型1", "value": 40},
    {"category": "B", "type": "类型2", "value": 25},
    {"category": "C", "type": "类型1", "value": 35},
    {"category": "C", "type": "类型2", "value": 30},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="层叠条形图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("stacked_bar.html")

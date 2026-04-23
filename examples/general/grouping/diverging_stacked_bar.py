"""
发散堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#diverging-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"question": "Q1", "type": "非常同意", "value": 30},
    {"question": "Q1", "type": "同意", "value": 25},
    {"question": "Q1", "type": "不同意", "value": -15},
    {"question": "Q1", "type": "非常不同意", "value": -10},
    {"question": "Q2", "type": "非常同意", "value": 20},
    {"question": "Q2", "type": "同意", "value": 30},
    {"question": "Q2", "type": "不同意", "value": -20},
    {"question": "Q2", "type": "非常不同意", "value": -15},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="question", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="发散堆叠条形图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("diverging_stacked_bar.html")

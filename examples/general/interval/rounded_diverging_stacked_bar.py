"""
圆角发散堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#diverging-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"question": "Q1", "type": "非常不满意", "value": -10},
    {"question": "Q1", "type": "不满意", "value": -15},
    {"question": "Q1", "type": "满意", "value": 40},
    {"question": "Q1", "type": "非常满意", "value": 35},
    {"question": "Q2", "type": "非常不满意", "value": -5},
    {"question": "Q2", "type": "不满意", "value": -20},
    {"question": "Q2", "type": "满意", "value": 45},
    {"question": "Q2", "type": "非常满意", "value": 30},
    {"question": "Q3", "type": "非常不满意", "value": -8},
    {"question": "Q3", "type": "不满意", "value": -12},
    {"question": "Q3", "type": "满意", "value": 50},
    {"question": "Q3", "type": "非常满意", "value": 30},
    {"question": "Q4", "type": "非常不满意", "value": -3},
    {"question": "Q4", "type": "不满意", "value": -7},
    {"question": "Q4", "type": "满意", "value": 55},
    {"question": "Q4", "type": "非常满意", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="question", y_field_name="value", color_field="type")
    .set_global_options(
        transform_opts=[
            opts.TransformStackYOpts(),
        ],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        style_opts=opts.BaseChartRadiusInsetStyleOpts(radius=10),
        title_opts=opts.TitleOpts(title="圆角发散堆叠条形图"),
    )
)
chart.render("rounded_diverging_stacked_bar.html")

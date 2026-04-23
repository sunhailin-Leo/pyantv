"""
堆叠玫瑰图
G2 文档: https://g2.antv.antgroup.com/examples/general/rose/#stacked-rose
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"quarter": "Q1", "type": "线上", "value": 120},
    {"quarter": "Q1", "type": "线下", "value": 80},
    {"quarter": "Q2", "type": "线上", "value": 150},
    {"quarter": "Q2", "type": "线下", "value": 100},
    {"quarter": "Q3", "type": "线上", "value": 180},
    {"quarter": "Q3", "type": "线下", "value": 120},
    {"quarter": "Q4", "type": "线上", "value": 200},
    {"quarter": "Q4", "type": "线下", "value": 140},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="quarter", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="堆叠玫瑰图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("stacked_rose.html")

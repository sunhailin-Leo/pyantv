"""
玫瑰图
G2 文档: https://g2.antv.antgroup.com/examples/general/rose/#rose
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "分类一", "value": 27},
    {"type": "分类二", "value": 25},
    {"type": "分类三", "value": 18},
    {"type": "分类四", "value": 15},
    {"type": "分类五", "value": 10},
    {"type": "其他", "value": 5},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="玫瑰图"),
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("rose.html")

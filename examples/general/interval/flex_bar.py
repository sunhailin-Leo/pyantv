"""
弹性条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#flex-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "电子产品", "value": 4500, "count": 120},
    {"category": "服装", "value": 3200, "count": 200},
    {"category": "食品", "value": 2800, "count": 350},
    {"category": "家居", "value": 1900, "count": 80},
    {"category": "图书", "value": 800, "count": 150},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_global_options(
        transform_opts=[opts.TransformFlexXOpts(field="count")],
        title_opts=opts.TitleOpts(title="弹性条形图"),
    )
)
chart.render("flex_bar.html")

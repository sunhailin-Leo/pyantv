"""
类别异常
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/insight/#category-anomaly
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 50}, {"category": "B", "value": 55},
    {"category": "C", "value": 200}, {"category": "D", "value": 45},
    {"category": "E", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="类别异常"),
    )
)
chart.render("category_anomaly.html")

"""
低方差
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/insight/#low-variance
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 50}, {"category": "B", "value": 51},
    {"category": "C", "value": 49}, {"category": "D", "value": 50},
    {"category": "E", "value": 52}, {"category": "F", "value": 48},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="低方差"),
    )
)
chart.render("low_variance.html")

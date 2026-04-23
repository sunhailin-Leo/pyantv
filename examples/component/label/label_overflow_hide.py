"""
数据标签超出隐藏
G2 文档: https://g2.antv.antgroup.com/examples/component/label/#label-overflow-hide
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 5}, {"name": "B", "value": 55},
    {"name": "C", "value": 3}, {"name": "D", "value": 70},
    {"name": "E", "value": 2}, {"name": "F", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="数据标签超出隐藏"),
        label_opts=[opts.LabelOpts(text_opts="value")],
    )
)
chart.render("label_overflow_hide.html")

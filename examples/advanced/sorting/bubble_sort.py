"""
冒泡排序
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/sorting/#bubble-sort
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"index": 0, "value": 50}, {"index": 1, "value": 30},
    {"index": 2, "value": 80}, {"index": 3, "value": 10},
    {"index": 4, "value": 60}, {"index": 5, "value": 40},
    {"index": 6, "value": 70}, {"index": 7, "value": 20},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="index", y_field_name="value", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="冒泡排序"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("bubble_sort.html")

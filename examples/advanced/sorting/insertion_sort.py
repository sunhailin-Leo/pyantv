"""
插入排序
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/sorting/#insertion-sort
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"index": 0, "value": 40}, {"index": 1, "value": 20},
    {"index": 2, "value": 70}, {"index": 3, "value": 10},
    {"index": 4, "value": 50}, {"index": 5, "value": 30},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="index", y_field_name="value", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="插入排序"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("insertion_sort.html")

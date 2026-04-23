"""
选择排序
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/sorting/#selection-sort
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"index": 0, "value": 45}, {"index": 1, "value": 25},
    {"index": 2, "value": 75}, {"index": 3, "value": 15},
    {"index": 4, "value": 55}, {"index": 5, "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="index", y_field_name="value", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="选择排序"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("selection_sort.html")

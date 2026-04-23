"""
微秒级区间条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#bindrange
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"task": "Task A", "start": 1, "end": 5},
    {"task": "Task B", "start": 3, "end": 8},
    {"task": "Task C", "start": 6, "end": 12},
    {"task": "Task D", "start": 2, "end": 9},
    {"task": "Task E", "start": 7, "end": 15},
    {"task": "Task F", "start": 10, "end": 18},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="task", y_field_name=["start", "end"])
    .set_coordinate(coordinate_opts=opts.CoordinateTransposeOpts())
    .set_global_options(
        title_opts=opts.TitleOpts(title="微妙级区间条形图"),
    )
)
chart.render("minute_range_bar.html")

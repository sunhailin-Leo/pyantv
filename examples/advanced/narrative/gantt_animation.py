"""
甘特图动画
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/narrative/#gantt-animation
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"task": "需求分析", "start": 0, "end": 3},
    {"task": "设计", "start": 2, "end": 5},
    {"task": "开发", "start": 4, "end": 9},
    {"task": "测试", "start": 8, "end": 11},
    {"task": "上线", "start": 10, "end": 12},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="task", y_field_name=["start", "end"], color_field="task")
    .set_global_options(
        title_opts=opts.TitleOpts(title="甘特图动画"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("gantt_animation.html")

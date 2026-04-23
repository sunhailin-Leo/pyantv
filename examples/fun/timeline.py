"""
时间轴 Timeline
G2 文档: https://g2.antv.antgroup.com/examples/fun/fun/#timeline
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2018", "event": "创立", "value": 10},
    {"year": "2019", "event": "A轮", "value": 30},
    {"year": "2020", "event": "B轮", "value": 60},
    {"year": "2021", "event": "C轮", "value": 100},
    {"year": "2022", "event": "上市", "value": 150},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="时间轴 Timeline"),
    )
)
chart.render("timeline.html")

"""
火车调度
G2 文档: https://g2.antv.antgroup.com/examples/general/text/#train-schedule
"""
from pyantv import options as opts
from pyantv.charts import View, Line, Text

schedule_data = [
    {"time": "06:00", "station": "北京", "train": "G1"},
    {"time": "08:30", "station": "济南", "train": "G1"},
    {"time": "10:00", "station": "南京", "train": "G1"},
    {"time": "12:00", "station": "上海", "train": "G1"},
    {"time": "07:00", "station": "北京", "train": "G3"},
    {"time": "09:00", "station": "济南", "train": "G3"},
    {"time": "11:30", "station": "南京", "train": "G3"},
    {"time": "13:30", "station": "上海", "train": "G3"},
]

line = (
    Line()
    .set_encode(x_field_name="time", y_field_name="station", color_field="train")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(line_width=2),
    )
)

text = (
    Text()
    .set_encode(x_field_name="time", y_field_name="station")
)

chart = (
    View()
    .set_data(data=schedule_data)
    .set_view_children(children=[line.options, text.options])
    .set_global_options(title_opts=opts.TitleOpts(title="火车调度"))
)
chart.render("train_schedule.html")

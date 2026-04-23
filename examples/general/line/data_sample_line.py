"""
数据样本折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#data-sample-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01-01", "value": 120},
    {"date": "2020-01-15", "value": 135},
    {"date": "2020-02-01", "value": 148},
    {"date": "2020-02-15", "value": 142},
    {"date": "2020-03-01", "value": 160},
    {"date": "2020-03-15", "value": 175},
    {"date": "2020-04-01", "value": 168},
    {"date": "2020-04-15", "value": 190},
    {"date": "2020-05-01", "value": 205},
    {"date": "2020-05-15", "value": 198},
    {"date": "2020-06-01", "value": 220},
    {"date": "2020-06-15", "value": 235},
    {"date": "2020-07-01", "value": 248},
    {"date": "2020-07-15", "value": 260},
    {"date": "2020-08-01", "value": 255},
    {"date": "2020-08-15", "value": 270},
    {"date": "2020-09-01", "value": 285},
    {"date": "2020-09-15", "value": 278},
    {"date": "2020-10-01", "value": 300},
    {"date": "2020-10-15", "value": 310},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="value")
    .set_global_options(title_opts=opts.TitleOpts(title="数据样本折线图"))
)
chart.render("data_sample_line.html")

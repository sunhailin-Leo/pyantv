"""
零值折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#zero-value-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01", "value": 120},
    {"date": "2020-02", "value": 0},
    {"date": "2020-03", "value": 85},
    {"date": "2020-04", "value": 0},
    {"date": "2020-05", "value": 150},
    {"date": "2020-06", "value": 200},
    {"date": "2020-07", "value": 0},
    {"date": "2020-08", "value": 180},
    {"date": "2020-09", "value": 95},
    {"date": "2020-10", "value": 0},
    {"date": "2020-11", "value": 220},
    {"date": "2020-12", "value": 250},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="value")
    .set_global_options(title_opts=opts.TitleOpts(title="零值折线图"))
)
chart.render("zero_value_line.html")

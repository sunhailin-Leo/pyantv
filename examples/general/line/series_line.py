"""
系列折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#series-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2018", "type": "收入", "value": 1200},
    {"year": "2018", "type": "支出", "value": 800},
    {"year": "2018", "type": "利润", "value": 400},
    {"year": "2019", "type": "收入", "value": 1500},
    {"year": "2019", "type": "支出", "value": 900},
    {"year": "2019", "type": "利润", "value": 600},
    {"year": "2020", "type": "收入", "value": 1800},
    {"year": "2020", "type": "支出", "value": 1100},
    {"year": "2020", "type": "利润", "value": 700},
    {"year": "2021", "type": "收入", "value": 2200},
    {"year": "2021", "type": "支出", "value": 1300},
    {"year": "2021", "type": "利润", "value": 900},
    {"year": "2022", "type": "收入", "value": 2600},
    {"year": "2022", "type": "支出", "value": 1500},
    {"year": "2022", "type": "利润", "value": 1100},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(title_opts=opts.TitleOpts(title="系列折线图"))
)
chart.render("series_line.html")

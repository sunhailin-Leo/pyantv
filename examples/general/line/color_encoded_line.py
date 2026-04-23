"""
颜色编码折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#color-encoded-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2018", "type": "线上", "value": 320},
    {"year": "2019", "type": "线上", "value": 450},
    {"year": "2020", "type": "线上", "value": 580},
    {"year": "2021", "type": "线上", "value": 650},
    {"year": "2022", "type": "线上", "value": 720},
    {"year": "2018", "type": "线下", "value": 500},
    {"year": "2019", "type": "线下", "value": 450},
    {"year": "2020", "type": "线下", "value": 350},
    {"year": "2021", "type": "线下", "value": 300},
    {"year": "2022", "type": "线下", "value": 280},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(title_opts=opts.TitleOpts(title="颜色编码折线图"))
)
chart.render("color_encoded_line.html")

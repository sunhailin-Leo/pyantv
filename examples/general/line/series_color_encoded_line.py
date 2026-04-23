"""
系列颜色编码折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#series-color-encoded-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01", "type": "邮件营销", "value": 120},
    {"date": "2020-02", "type": "邮件营销", "value": 132},
    {"date": "2020-03", "type": "邮件营销", "value": 101},
    {"date": "2020-04", "type": "邮件营销", "value": 134},
    {"date": "2020-05", "type": "邮件营销", "value": 90},
    {"date": "2020-01", "type": "联盟广告", "value": 220},
    {"date": "2020-02", "type": "联盟广告", "value": 182},
    {"date": "2020-03", "type": "联盟广告", "value": 191},
    {"date": "2020-04", "type": "联盟广告", "value": 234},
    {"date": "2020-05", "type": "联盟广告", "value": 290},
    {"date": "2020-01", "type": "搜索引擎", "value": 820},
    {"date": "2020-02", "type": "搜索引擎", "value": 932},
    {"date": "2020-03", "type": "搜索引擎", "value": 901},
    {"date": "2020-04", "type": "搜索引擎", "value": 934},
    {"date": "2020-05", "type": "搜索引擎", "value": 1290},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="value", color_field="type")
    .set_global_options(title_opts=opts.TitleOpts(title="系列颜色编码折线图"))
)
chart.render("series_color_encoded_line.html")

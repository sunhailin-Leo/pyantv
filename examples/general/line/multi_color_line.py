"""
多色折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#multi-color-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "Jan", "value": 120, "status": "正常"},
    {"month": "Feb", "value": 135, "status": "正常"},
    {"month": "Mar", "value": 148, "status": "正常"},
    {"month": "Apr", "value": 160, "status": "警告"},
    {"month": "May", "value": 175, "status": "警告"},
    {"month": "Jun", "value": 190, "status": "危险"},
    {"month": "Jul", "value": 205, "status": "危险"},
    {"month": "Aug", "value": 220, "status": "危险"},
    {"month": "Sep", "value": 235, "status": "警告"},
    {"month": "Oct", "value": 250, "status": "正常"},
    {"month": "Nov", "value": 265, "status": "正常"},
    {"month": "Dec", "value": 280, "status": "正常"},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="status")
    .set_global_options(title_opts=opts.TitleOpts(title="多色折线图"))
)
chart.render("multi_color_line.html")

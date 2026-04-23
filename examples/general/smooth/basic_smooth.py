"""
基础平滑图
G2 文档: https://g2.antv.antgroup.com/examples/general/smooth/#basic-smooth
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "1月", "value": 30},
    {"month": "2月", "value": 45},
    {"month": "3月", "value": 35},
    {"month": "4月", "value": 55},
    {"month": "5月", "value": 40},
    {"month": "6月", "value": 60},
    {"month": "7月", "value": 50},
    {"month": "8月", "value": 70},
    {"month": "9月", "value": 55},
    {"month": "10月", "value": 75},
    {"month": "11月", "value": 65},
    {"month": "12月", "value": 80},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", shape_field="smooth")
    .set_global_options(
        title_opts=opts.TitleOpts(title="基础平滑图"),
    )
)
chart.render("basic_smooth.html")

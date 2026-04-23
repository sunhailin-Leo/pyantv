"""
南丁格尔玫瑰环图
G2 文档: https://g2.antv.antgroup.com/examples/general/rose/#nightingale-donut-rose
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "Jan", "value": 120},
    {"month": "Feb", "value": 90},
    {"month": "Mar", "value": 150},
    {"month": "Apr", "value": 200},
    {"month": "May", "value": 180},
    {"month": "Jun", "value": 250},
    {"month": "Jul", "value": 300},
    {"month": "Aug", "value": 280},
    {"month": "Sep", "value": 220},
    {"month": "Oct", "value": 170},
    {"month": "Nov", "value": 130},
    {"month": "Dec", "value": 100},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="month")
    .set_global_options(
        title_opts=opts.TitleOpts(title="南丁格尔玫瑰环图"),
        coordinate_opts=opts.CoordinatePolarOpts(inner_radius=0.4),
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)
chart.render("nightingale_donut_rose.html")

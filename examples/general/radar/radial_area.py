"""
径向面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/radar/#radial-area
"""
from pyantv import options as opts
from pyantv.charts import Area

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
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="径向面积图"),
        coordinate_opts=opts.CoordinatePolarOpts(),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5),
    )
)
chart.render("radial_area.html")

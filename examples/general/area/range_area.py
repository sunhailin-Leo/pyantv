"""
区间面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#range-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "Jan", "temperature": [2, 12]},
    {"month": "Feb", "temperature": [3, 14]},
    {"month": "Mar", "temperature": [5, 18]},
    {"month": "Apr", "temperature": [8, 22]},
    {"month": "May", "temperature": [12, 26]},
    {"month": "Jun", "temperature": [16, 30]},
    {"month": "Jul", "temperature": [18, 33]},
    {"month": "Aug", "temperature": [17, 32]},
    {"month": "Sep", "temperature": [14, 28]},
    {"month": "Oct", "temperature": [10, 22]},
    {"month": "Nov", "temperature": [5, 16]},
    {"month": "Dec", "temperature": [2, 12]},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="temperature")
    .set_global_options(
        title_opts=opts.TitleOpts(title="区间面积图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.4),
    )
)
chart.render("range_area.html")

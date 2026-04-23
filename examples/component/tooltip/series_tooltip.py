"""
系列提示
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#series-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "1月", "city": "北京", "temp": 5},
    {"month": "2月", "city": "北京", "temp": 8},
    {"month": "3月", "city": "北京", "temp": 15},
    {"month": "1月", "city": "上海", "temp": 10},
    {"month": "2月", "city": "上海", "temp": 12},
    {"month": "3月", "city": "上海", "temp": 18},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="temp", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="系列提示"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("series_tooltip.html")

"""
点击系列图提示
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#click-series-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "1月", "city": "北京", "value": 30},
    {"month": "2月", "city": "北京", "value": 45},
    {"month": "3月", "city": "北京", "value": 35},
    {"month": "1月", "city": "上海", "value": 40},
    {"month": "2月", "city": "上海", "value": 50},
    {"month": "3月", "city": "上海", "value": 42},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="点击系列图提示"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("click_series_tooltip.html")

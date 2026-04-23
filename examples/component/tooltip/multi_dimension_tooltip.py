"""
多维度提示
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#multi-dimension-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"city": "北京", "month": "1月", "value": 30},
    {"city": "北京", "month": "2月", "value": 45},
    {"city": "上海", "month": "1月", "value": 40},
    {"city": "上海", "month": "2月", "value": 50},
    {"city": "广州", "month": "1月", "value": 25},
    {"city": "广州", "month": "2月", "value": 38},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="多维度提示"),
        tooltip_opts=opts.TooltipOpts(),
        transform_opts=[opts.TransformDodgeXOpts()],
    )
)
chart.render("multi_dimension_tooltip.html")

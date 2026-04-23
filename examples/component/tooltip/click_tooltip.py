"""
点击提示
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#click-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 55},
    {"name": "C", "value": 45}, {"name": "D", "value": 70},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="点击提示"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("click_tooltip.html")

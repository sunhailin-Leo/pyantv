"""
自定义样式
G2 文档: https://g2.antv.antgroup.com/examples/component/tooltip/#custom-style-tooltip
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"product": "A", "sales": 120}, {"product": "B", "sales": 150},
    {"product": "C", "sales": 130}, {"product": "D", "sales": 160},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="product", y_field_name="sales")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义样式"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("custom_style_tooltip.html")

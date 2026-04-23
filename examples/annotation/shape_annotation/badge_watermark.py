"""
徽章水印
G2 文档: https://g2.antv.antgroup.com/examples/annotation/shape/#badge-watermark
"""
from pyantv import options as opts
from pyantv.charts import Interval, Text, View

bar_data = [
    {"month": "1月", "sales": 120}, {"month": "2月", "sales": 150},
    {"month": "3月", "sales": 130}, {"month": "4月", "sales": 160},
    {"month": "5月", "sales": 140}, {"month": "6月", "sales": 170},
]

watermark_data = [{"x": "3月", "y": 100, "text": "DRAFT"}]

bar = (
    Interval()
    .set_data(data=bar_data)
    .set_encode(x_field_name="month", y_field_name="sales")
)

watermark = (
    Text()
    .set_data(data=watermark_data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.1),
        label_opts=[opts.LabelOpts(text_opts="text", font_size=40)],
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, watermark.options])
    .set_global_options(title_opts=opts.TitleOpts(title="徽章水印"))
)
chart.render("badge_watermark.html")

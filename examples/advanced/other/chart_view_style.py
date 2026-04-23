"""
图表视图样式
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#chart-view-style
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
    {"category": "E", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="图表视图样式"),
    )
)
chart.render("chart_view_style.html")

"""
固定宽度圆角条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#rounded-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "类别A", "value": 85},
    {"category": "类别B", "value": 72},
    {"category": "类别C", "value": 63},
    {"category": "类别D", "value": 55},
    {"category": "类别E", "value": 48},
    {"category": "类别F", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_interval_style(
        min_width=20,
        max_width=20,
        base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(radius=10),
    )
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="固定宽度圆角条形图"),
    )
)
chart.render("fixed_width_rounded_bar.html")

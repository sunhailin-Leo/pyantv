"""
调整蜘蛛布局
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#adjust-spider-layout
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "类别A", "value": 35},
    {"type": "类别B", "value": 28},
    {"type": "类别C", "value": 18},
    {"type": "类别D", "value": 12},
    {"type": "类别E", "value": 5},
    {"type": "类别F", "value": 2},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="调整蜘蛛布局"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(outer_radius=0.7),
        label_opts=[
            opts.LabelOpts(text_opts="type", position="spider"),
        ],
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)
chart.render("adjust_spider_layout.html")

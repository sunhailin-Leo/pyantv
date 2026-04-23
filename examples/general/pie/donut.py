"""
甜甜圈图
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#donut
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "家用电器", "value": 38},
    {"type": "食品饮料", "value": 22},
    {"type": "个护健康", "value": 17},
    {"type": "服饰箱包", "value": 13},
    {"type": "母婴产品", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="甜甜圈图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(inner_radius=0.6),
        label_opts=[opts.LabelOpts(text_opts="value", position="outside")],
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=2),
    )
)
chart.render("donut.html")

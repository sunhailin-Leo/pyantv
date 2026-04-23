"""
直方图范围刻度
G2 文档: https://g2.antv.antgroup.com/examples/general/histogram/#histogram-range-tick
"""
from pyantv import options as opts
from pyantv.charts import Rect

data = [
    {"score": 15}, {"score": 25}, {"score": 35}, {"score": 45},
    {"score": 55}, {"score": 65}, {"score": 75}, {"score": 85},
    {"score": 22}, {"score": 38}, {"score": 42}, {"score": 58},
    {"score": 62}, {"score": 78}, {"score": 88}, {"score": 92},
    {"score": 18}, {"score": 32}, {"score": 48}, {"score": 52},
    {"score": 68}, {"score": 72}, {"score": 82}, {"score": 95},
    {"score": 28}, {"score": 36}, {"score": 44}, {"score": 56},
    {"score": 64}, {"score": 76}, {"score": 84}, {"score": 98},
]

chart = (
    Rect()
    .set_data(data=data)
    .set_encode(x_field_name="score")
    .set_global_options(
        title_opts=opts.TitleOpts(title="直方图范围刻度"),
        transform_opts=[opts.TransformBinXOpts(thresholds=10, channel_name="y", channel_transform="count")],
        style_opts=opts.BaseChartStyleOpts(inset=1),
    )
)
chart.render("histogram_range_tick.html")

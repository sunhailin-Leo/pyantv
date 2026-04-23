"""
国庆节头像
G2 文档: https://g2.antv.antgroup.com/examples/fun/fun/#national-day-avatar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "红", "value": 40}, {"type": "黄", "value": 30},
    {"type": "蓝", "value": 20}, {"type": "绿", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="国庆节头像"),
        coordinate_opts=opts.CoordinateThetaOpts(),
        transform_opts=[opts.TransformStackYOpts()],
    )
)
chart.render("national_day_avatar.html")

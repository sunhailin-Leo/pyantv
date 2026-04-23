"""
2018年第一季度短视频用户性别分布
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#short-video-gender
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"gender": "男", "value": 55.2},
    {"gender": "女", "value": 44.8},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="gender")
    .set_global_options(
        title_opts=opts.TitleOpts(title="2018年第一季度短视频用户性别分布"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(),
        label_opts=[opts.LabelOpts(text_opts="value", position="outside")],
    )
)
chart.render("short_video_gender.html")

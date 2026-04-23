"""
WaveIn 动画
G2 文档: https://g2.antv.antgroup.com/examples/animation/animation/#wave-in
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 60},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="WaveIn 动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("wave_in.html")

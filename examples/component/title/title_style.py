"""
标题样式
G2 文档: https://g2.antv.antgroup.com/examples/component/title/#title-style
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 45},
    {"month": "3月", "value": 35}, {"month": "4月", "value": 55},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="月度销售数据", subtitle="2024年上半年"),
    )
)
chart.render("title_style.html")

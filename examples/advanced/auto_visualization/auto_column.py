"""
自动可视化 - 柱形图
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/auto/#column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "value": 30}, {"month": "2月", "value": 50},
    {"month": "3月", "value": 45}, {"month": "4月", "value": 60},
    {"month": "5月", "value": 40}, {"month": "6月", "value": 55},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自动可视化 - 柱形图"),
    )
)
chart.render("auto_column.html")

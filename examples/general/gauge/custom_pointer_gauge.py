"""
仪表盘自定义指针形状
G2 文档: https://g2.antv.antgroup.com/examples/general/gauge/#custom-pointer-gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

data = [{"target": 75, "total": 100, "name": "速度"}]

chart = (
    Gauge()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="仪表盘自定义指针形状"),
    )
)
chart.render("custom_pointer_gauge.html")

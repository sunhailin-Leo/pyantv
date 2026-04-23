
"""
配置线性渐变-仪表盘
G2 文档: https://g2.antv.antgroup.com/examples/style/bindling/#linear-gradient-gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

chart = (
    Gauge()
    .set_data(data=[{"value": 0.75}])
    .set_global_options(
        title_opts=opts.TitleOpts(title="配置线性渐变-仪表盘"),
    )
)
chart.render("linear_gradient_gauge.html")

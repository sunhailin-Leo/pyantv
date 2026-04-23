"""
完全自定义样式的仪表盘
G2 文档: https://g2.antv.antgroup.com/examples/general/gauge/#fully-custom-gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

data = [{"target": 85, "total": 100, "name": "KPI"}]

chart = (
    Gauge()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="完全自定义样式的仪表盘"),
    )
)
chart.render("fully_custom_gauge.html")

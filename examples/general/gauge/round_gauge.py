"""
仪表盘内置 round 形状
G2 文档: https://g2.antv.antgroup.com/examples/general/gauge/#round-gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

data = [{"target": 60, "total": 100, "name": "进度"}]

chart = (
    Gauge()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="仪表盘内置 round 形状"),
    )
)
chart.render("round_gauge.html")

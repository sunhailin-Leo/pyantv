"""
仪表盘
G2 文档: https://g2.antv.antgroup.com/examples/general/gauge/#gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

data = [{"target": 120, "total": 400, "name": "score"}]

chart = (
    Gauge()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="仪表盘"),
    )
)
chart.render("gauge.html")

"""
自定义仪表盘颜色
G2 文档: https://g2.antv.antgroup.com/examples/general/gauge/#custom-color-gauge
"""
from pyantv import options as opts
from pyantv.charts import Gauge

data = [{"target": 80, "total": 100, "name": "完成率"}]

chart = (
    Gauge()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义仪表盘颜色"),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)
chart.render("custom_color_gauge.html")

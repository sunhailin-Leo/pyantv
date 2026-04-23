"""
心率监测仪
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#heart-rate-monitor
"""
from pyantv import options as opts
from pyantv.charts import Line

import random
random.seed(42)
data = [{"time": i, "bpm": random.randint(60, 100)} for i in range(60)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="time", y_field_name="bpm")
    .set_global_options(
        title_opts=opts.TitleOpts(title="心率监测仪"),
    )
)
chart.render("heart_rate_monitor.html")

"""
数据脉冲网络
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#data-pulse-network
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "pulse": random.uniform(1, 10), "node": f"节点{i}"} for i in range(30)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="pulse", color_field="pulse")
    .set_global_options(
        title_opts=opts.TitleOpts(title="数据脉冲网络"),
    )
)
chart.render("data_pulse_network.html")

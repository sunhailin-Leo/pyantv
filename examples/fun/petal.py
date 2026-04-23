"""
花瓣图
G2 文档: https://g2.antv.antgroup.com/examples/fun/fun/#petal
"""
from pyantv import options as opts
from pyantv.charts import Interval

import math
data = [{"angle": i * 30, "value": abs(math.sin(i * math.pi / 6)) * 50 + 20, "type": f"花瓣{i+1}"} for i in range(12)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="花瓣图"),
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("petal.html")

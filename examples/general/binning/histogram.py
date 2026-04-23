"""
直方图
G2 文档: https://g2.antv.antgroup.com/examples/general/binning/#histogram
"""
from pyantv import options as opts
from pyantv.charts import Rect

import random
random.seed(42)
data = [{"value": random.gauss(50, 15)} for _ in range(500)]

chart = (
    Rect()
    .set_data(data=data)
    .set_encode(x_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="直方图"),
        transform_opts=[opts.TransformBinXOpts()],
    )
)
chart.render("histogram.html")

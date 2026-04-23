"""
核密度图
G2 文档: https://g2.antv.antgroup.com/examples/general/violin/#kernel-density
"""
from pyantv import options as opts
from pyantv.charts import Density

import random
random.seed(42)
data = [{"value": random.gauss(50, 15)} for _ in range(200)]

chart = (
    Density()
    .set_data(data=data)
    .set_encode(x_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="核密度图"),
    )
)
chart.render("kernel_density.html")

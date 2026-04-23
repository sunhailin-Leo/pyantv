"""
大小分箱
G2 文档: https://g2.antv.antgroup.com/examples/general/binning/#size-binning
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "count": random.randint(1, 50)} for _ in range(200)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="count")
    .set_global_options(
        title_opts=opts.TitleOpts(title="大小分箱"),
    )
)
chart.render("size_binning.html")

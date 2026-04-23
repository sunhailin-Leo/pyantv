"""
泊松分布
G2 文档: https://g2.antv.antgroup.com/examples/general/binning/#poisson
"""
from pyantv import options as opts
from pyantv.charts import Rect

import random
random.seed(42)
data = [{"value": sum(1 for _ in range(20) if random.random() < 0.3)} for _ in range(1000)]

chart = (
    Rect()
    .set_data(data=data)
    .set_encode(x_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="泊松分布"),
        transform_opts=[opts.TransformBinXOpts()],
    )
)
chart.render("poisson.html")

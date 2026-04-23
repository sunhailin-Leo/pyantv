"""
基因螺旋图
G2 文档: https://g2.antv.antgroup.com/examples/general/spiral/#gene-spiral
"""
from pyantv import options as opts
from pyantv.charts import Interval

import random
random.seed(42)
bases = ["A", "T", "G", "C"]
data = [{"position": i, "base": random.choice(bases), "value": random.uniform(0.5, 1.0)}
        for i in range(60)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="position", y_field_name="value", color_field="base")
    .set_global_options(
        title_opts=opts.TitleOpts(title="基因螺旋图"),
        coordinate_opts=opts.CoordinateHelixOpts(),
    )
)
chart.render("gene_spiral.html")

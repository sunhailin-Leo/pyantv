"""
透明度分箱
G2 文档: https://g2.antv.antgroup.com/examples/general/binning/#opacity-binning
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100), "density": random.uniform(0.1, 1.0)} for _ in range(300)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="透明度分箱"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5),
    )
)
chart.render("opacity_binning.html")

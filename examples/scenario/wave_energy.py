"""
波浪能量图
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#wave-energy
"""
from pyantv import options as opts
from pyantv.charts import Area

import math
data = [{"x": i, "y": math.sin(i * 0.2) * 30 + 50} for i in range(50)]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="波浪能量图"),
    )
)
chart.render("wave_energy.html")

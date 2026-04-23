
"""
重置刷选
G2 文档: https://g2.antv.antgroup.com/examples/interaction/brush/#reset-brush
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 100), "y": random.uniform(0, 100)} for _ in range(50)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="重置刷选"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("reset_brush.html")

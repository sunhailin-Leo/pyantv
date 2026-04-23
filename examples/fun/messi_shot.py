"""
梅西射门分析
G2 文档: https://g2.antv.antgroup.com/examples/fun/fun/#messi-shot
"""
from pyantv import options as opts
from pyantv.charts import Point

import random
random.seed(42)
data = [{"x": random.uniform(0, 68), "y": random.uniform(0, 52.5), "result": random.choice(["进球", "射正", "射偏"]), "distance": random.uniform(5, 30)} for _ in range(50)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="result", size_field="distance")
    .set_global_options(
        title_opts=opts.TitleOpts(title="梅西射门分析"),
    )
)
chart.render("messi_shot.html")

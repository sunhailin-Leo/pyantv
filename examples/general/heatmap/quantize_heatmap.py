"""
量化热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/heatmap/#quantize-heatmap
"""
from pyantv import options as opts
from pyantv.charts import Cell

import random
random.seed(456)

weeks = [f"W{i}" for i in range(1, 13)]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

data = []
for week in weeks:
    for day in days:
        data.append({
            "week": week,
            "day": day,
            "commits": random.randint(0, 30),
        })

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="week", y_field_name="day", color_field="commits")
    .set_scale(
        color_scale_opts=opts.ScaleQuantizeOpts(
            range_=["#ebedf0", "#c6e48b", "#7bc96f", "#239a3b", "#196127"],
        )
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="量化热力图"),
        style_opts=opts.BaseChartStyleOpts(inset=1),
    )
)
chart.render("quantize_heatmap.html")

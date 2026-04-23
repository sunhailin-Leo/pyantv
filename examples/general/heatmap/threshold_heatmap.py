"""
阈值热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/heatmap/#threshold-heatmap
"""
from pyantv import options as opts
from pyantv.charts import Cell

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = list(range(24))

import random
random.seed(42)
data = []
for day in days:
    for hour in hours:
        data.append({
            "day": day,
            "hour": str(hour),
            "value": random.randint(0, 100),
        })

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="hour", y_field_name="day", color_field="value")
    .set_scale(
        color_scale_opts=opts.ScaleThresholdOpts(
            domain=[20, 40, 60, 80],
            range_=["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"],
        )
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="阈值热力图"),
        style_opts=opts.BaseChartStyleOpts(inset=1),
    )
)
chart.render("threshold_heatmap.html")

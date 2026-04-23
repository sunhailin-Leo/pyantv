"""
分位数热力图
G2 文档: https://g2.antv.antgroup.com/examples/general/heatmap/#quantile-heatmap
"""
from pyantv import options as opts
from pyantv.charts import Cell

import random
random.seed(123)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["产品A", "产品B", "产品C", "产品D", "产品E"]

data = []
for month in months:
    for category in categories:
        data.append({
            "month": month,
            "category": category,
            "sales": random.randint(10, 500),
        })

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="category", color_field="sales")
    .set_scale(
        color_scale_opts=opts.ScaleQuantileOpts(
            range_=["#f7fbff", "#c6dbef", "#6baed6", "#2171b5", "#08306b"],
        )
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="分位数热力图"),
        style_opts=opts.BaseChartStyleOpts(inset=1),
    )
)
chart.render("quantile_heatmap.html")

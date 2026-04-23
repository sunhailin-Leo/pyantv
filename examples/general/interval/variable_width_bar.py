"""
可变宽度条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#variable-width-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"region": "华东", "revenue": 5200, "market_share": 35},
    {"region": "华南", "revenue": 3800, "market_share": 25},
    {"region": "华北", "revenue": 2900, "market_share": 20},
    {"region": "西南", "revenue": 1500, "market_share": 12},
    {"region": "其他", "revenue": 800, "market_share": 8},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="region", y_field_name="revenue")
    .set_global_options(
        transform_opts=[opts.TransformFlexXOpts(field="market_share")],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="可变宽度条形图"),
    )
)
chart.render("variable_width_bar.html")

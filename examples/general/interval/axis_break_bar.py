"""
坐标轴断轴条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#axis-break
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"product": "产品A", "sales": 120},
    {"product": "产品B", "sales": 98},
    {"product": "产品C", "sales": 85},
    {"product": "产品D", "sales": 1500},
    {"product": "产品E", "sales": 45},
    {"product": "产品F", "sales": 30},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="product", y_field_name="sales")
    .set_scale(y_scale_opts=opts.ScaleLinearOpts(domain=[0, 200]))
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="坐标轴断轴条形图"),
    )
)
chart.render("axis_break_bar.html")

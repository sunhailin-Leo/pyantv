"""
自定义形状水波图
G2 文档: https://g2.antv.antgroup.com/examples/general/liquid/#custom-shape-liquid
"""
from pyantv import options as opts
from pyantv.charts import Liquid

data = 0.7

chart = (
    Liquid()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义形状水波图"),
    )
)
chart.render("custom_shape_liquid.html")

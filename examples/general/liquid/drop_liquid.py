"""
水滴形状水波图
G2 文档: https://g2.antv.antgroup.com/examples/general/liquid/#drop-liquid
"""
from pyantv import options as opts
from pyantv.charts import Liquid

data = 0.8

chart = (
    Liquid()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="水滴形状水波图"),
    )
)
chart.render("drop_liquid.html")

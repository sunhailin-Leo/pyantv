"""
带背景的水波图
G2 文档: https://g2.antv.antgroup.com/examples/general/liquid/#liquid-with-background
"""
from pyantv import options as opts
from pyantv.charts import Liquid

data = 0.55

chart = (
    Liquid()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="带背景的水波图"),
    )
)
chart.render("liquid_with_background.html")

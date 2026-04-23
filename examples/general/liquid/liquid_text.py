"""
水波图 文本内容
G2 文档: https://g2.antv.antgroup.com/examples/general/liquid/#liquid-text
"""
from pyantv import options as opts
from pyantv.charts import Liquid

data = 0.65

chart = (
    Liquid()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="水波图 文本内容"),
    )
)
chart.render("liquid_text.html")

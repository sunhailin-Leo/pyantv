"""
旭日图自定义纹理
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst-custom-pattern
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "研发", "value": 150},
        {"name": "市场", "value": 100},
        {"name": "销售", "value": 80},
        {"name": "运维", "value": 60},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图自定义纹理"),
    )
)
chart.render("sunburst_custom_pattern.html")

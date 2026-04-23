"""
旭日图交互配置
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst-interaction
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "分类A", "children": [
            {"name": "A-1", "value": 100},
            {"name": "A-2", "value": 80},
        ]},
        {"name": "分类B", "children": [
            {"name": "B-1", "value": 90},
            {"name": "B-2", "value": 70},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图交互配置"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("sunburst_interaction.html")

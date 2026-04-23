"""
矩形树图下钻
G2 文档: https://g2.antv.antgroup.com/examples/graph/tree/#treemap-drill-down
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "技术部", "children": [
            {"name": "前端组", "children": [
                {"name": "React", "value": 40},
                {"name": "Vue", "value": 30},
            ]},
            {"name": "后端组", "children": [
                {"name": "Java", "value": 50},
                {"name": "Python", "value": 35},
            ]},
        ]},
        {"name": "产品部", "children": [
            {"name": "设计", "value": 45},
            {"name": "运营", "value": 30},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="矩形树图下钻"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("treemap_drill_down.html")

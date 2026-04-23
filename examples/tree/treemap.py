"""
矩形树图
G2 文档: https://g2.antv.antgroup.com/examples/graph/tree/#treemap
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "分类A", "children": [
            {"name": "A-1", "value": 100},
            {"name": "A-2", "value": 80},
            {"name": "A-3", "value": 60},
        ]},
        {"name": "分类B", "children": [
            {"name": "B-1", "value": 90},
            {"name": "B-2", "value": 70},
        ]},
        {"name": "分类C", "children": [
            {"name": "C-1", "value": 50},
            {"name": "C-2", "value": 40},
            {"name": "C-3", "value": 30},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="矩形树图"),
    )
)
chart.render("treemap.html")

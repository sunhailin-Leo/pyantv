"""
旭日图
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst
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
            {"name": "B-3", "value": 50},
        ]},
        {"name": "分类C", "children": [
            {"name": "C-1", "value": 60},
            {"name": "C-2", "value": 40},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图"),
    )
)
chart.render("sunburst.html")

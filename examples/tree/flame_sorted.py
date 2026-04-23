"""
火焰图（排序）
G2 文档: https://g2.antv.antgroup.com/examples/graph/tree/#flame-sorted
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "main()", "children": [
            {"name": "compute()", "value": 50},
            {"name": "render()", "value": 40},
            {"name": "parse()", "value": 30},
            {"name": "init()", "value": 20},
            {"name": "cleanup()", "value": 10},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="火焰图（排序）"),
    )
)
chart.render("flame_sorted.html")

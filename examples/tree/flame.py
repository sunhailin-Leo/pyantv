"""
火焰图
G2 文档: https://g2.antv.antgroup.com/examples/graph/tree/#flame
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "main()", "children": [
            {"name": "init()", "value": 20},
            {"name": "process()", "children": [
                {"name": "parse()", "value": 30},
                {"name": "compute()", "value": 50},
                {"name": "render()", "value": 40},
            ]},
            {"name": "cleanup()", "value": 10},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="火焰图"),
    )
)
chart.render("flame.html")

"""
树图
G2 文档: https://g2.antv.antgroup.com/examples/graph/tree/#tree
"""
from pyantv import options as opts
from pyantv.charts import Tree

data = {
    "name": "root",
    "children": [
        {"name": "分支A", "children": [
            {"name": "叶子A1"},
            {"name": "叶子A2"},
        ]},
        {"name": "分支B", "children": [
            {"name": "叶子B1"},
            {"name": "分支B2", "children": [
                {"name": "叶子B2a"},
                {"name": "叶子B2b"},
            ]},
        ]},
        {"name": "分支C", "children": [
            {"name": "叶子C1"},
        ]},
    ],
}

chart = (
    Tree()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="树图"),
    )
)
chart.render("tree.html")

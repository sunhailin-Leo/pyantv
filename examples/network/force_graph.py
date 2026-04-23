"""
力导向图
G2 文档: https://g2.antv.antgroup.com/examples/graph/network/#force-graph
"""
from pyantv import options as opts
from pyantv.charts import ForceGraph

data = {
    "nodes": [
        {"id": "node1", "name": "节点1", "value": 10},
        {"id": "node2", "name": "节点2", "value": 20},
        {"id": "node3", "name": "节点3", "value": 15},
        {"id": "node4", "name": "节点4", "value": 25},
        {"id": "node5", "name": "节点5", "value": 12},
        {"id": "node6", "name": "节点6", "value": 18},
    ],
    "links": [
        {"source": "node1", "target": "node2"},
        {"source": "node1", "target": "node3"},
        {"source": "node2", "target": "node4"},
        {"source": "node3", "target": "node4"},
        {"source": "node3", "target": "node5"},
        {"source": "node4", "target": "node6"},
        {"source": "node5", "target": "node6"},
    ],
}

chart = (
    ForceGraph()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="力导向图"),
    )
)
chart.render("force_graph.html")

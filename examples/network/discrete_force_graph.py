"""
离散力导向图
G2 文档: https://g2.antv.antgroup.com/examples/graph/network/#discrete-force-graph
"""
from pyantv import options as opts
from pyantv.charts import ForceGraph

data = {
    "nodes": [
        {"id": "a1", "name": "A-1", "group": "A"},
        {"id": "a2", "name": "A-2", "group": "A"},
        {"id": "a3", "name": "A-3", "group": "A"},
        {"id": "b1", "name": "B-1", "group": "B"},
        {"id": "b2", "name": "B-2", "group": "B"},
        {"id": "c1", "name": "C-1", "group": "C"},
        {"id": "c2", "name": "C-2", "group": "C"},
        {"id": "c3", "name": "C-3", "group": "C"},
    ],
    "links": [
        {"source": "a1", "target": "a2"},
        {"source": "a2", "target": "a3"},
        {"source": "a1", "target": "b1"},
        {"source": "b1", "target": "b2"},
        {"source": "b2", "target": "c1"},
        {"source": "c1", "target": "c2"},
        {"source": "c2", "target": "c3"},
        {"source": "a3", "target": "c3"},
    ],
}

chart = (
    ForceGraph()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="离散力导向图"),
    )
)
chart.render("discrete_force_graph.html")

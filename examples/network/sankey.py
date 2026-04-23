"""
桑基图
G2 文档: https://g2.antv.antgroup.com/examples/graph/network/#sankey
"""
from pyantv import options as opts
from pyantv.charts import Sankey

data = {
    "nodes": [
        {"name": "来源A"},
        {"name": "来源B"},
        {"name": "来源C"},
        {"name": "中间1"},
        {"name": "中间2"},
        {"name": "目标X"},
        {"name": "目标Y"},
    ],
    "links": [
        {"source": "来源A", "target": "中间1", "value": 30},
        {"source": "来源A", "target": "中间2", "value": 20},
        {"source": "来源B", "target": "中间1", "value": 25},
        {"source": "来源B", "target": "中间2", "value": 15},
        {"source": "来源C", "target": "中间2", "value": 35},
        {"source": "中间1", "target": "目标X", "value": 40},
        {"source": "中间1", "target": "目标Y", "value": 15},
        {"source": "中间2", "target": "目标X", "value": 30},
        {"source": "中间2", "target": "目标Y", "value": 40},
    ],
}

chart = (
    Sankey()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="桑基图"),
    )
)
chart.render("sankey.html")

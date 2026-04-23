"""
弦图
G2 文档: https://g2.antv.antgroup.com/examples/graph/network/#chord
"""
from pyantv import options as opts
from pyantv.charts import Chord

data = {
    "nodes": [
        {"name": "北京"},
        {"name": "上海"},
        {"name": "广州"},
        {"name": "深圳"},
    ],
    "links": [
        {"source": "北京", "target": "上海", "value": 100},
        {"source": "北京", "target": "广州", "value": 80},
        {"source": "北京", "target": "深圳", "value": 60},
        {"source": "上海", "target": "广州", "value": 70},
        {"source": "上海", "target": "深圳", "value": 50},
        {"source": "广州", "target": "深圳", "value": 90},
    ],
}

chart = (
    Chord()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="弦图"),
    )
)
chart.render("chord.html")

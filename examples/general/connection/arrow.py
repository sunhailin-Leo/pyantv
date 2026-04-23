"""
箭线
G2 文档: https://g2.antv.antgroup.com/examples/general/connection/#arrow
"""
from pyantv import options as opts
from pyantv.charts import Link

data = [
    {"source": "A", "target": "B", "value": 10},
    {"source": "B", "target": "C", "value": 15},
    {"source": "C", "target": "D", "value": 8},
    {"source": "A", "target": "D", "value": 12},
    {"source": "B", "target": "D", "value": 6},
]

chart = (
    Link()
    .set_data(data=data)
    .set_encode(x_field_name=["source", "target"], y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="箭线"),
        style_opts=opts.BaseChartStyleOpts(stroke="#5B8FF9", line_width=1),
    )
)
chart.render("arrow.html")

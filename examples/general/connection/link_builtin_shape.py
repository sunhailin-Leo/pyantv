"""
link 内置形状
G2 文档: https://g2.antv.antgroup.com/examples/general/connection/#link-builtin-shape
"""
from pyantv import options as opts
from pyantv.charts import Link

data = [
    {"source": "北京", "target": "上海", "value": 100},
    {"source": "北京", "target": "广州", "value": 80},
    {"source": "上海", "target": "深圳", "value": 60},
    {"source": "广州", "target": "深圳", "value": 50},
    {"source": "北京", "target": "杭州", "value": 70},
]

chart = (
    Link()
    .set_data(data=data)
    .set_encode(x_field_name=["source", "target"], y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="link 内置形状"),
        style_opts=opts.BaseChartStyleOpts(stroke="#5B8FF9", line_width=1.5),
    )
)
chart.render("link_builtin_shape.html")

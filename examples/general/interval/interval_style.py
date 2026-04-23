"""
interval 样式配置
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#bindstyle
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "家具", "sales": 380},
    {"type": "电子", "sales": 520},
    {"type": "服装", "sales": 290},
    {"type": "食品", "sales": 450},
    {"type": "图书", "sales": 180},
    {"type": "玩具", "sales": 350},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="sales")
    .set_style(
        style_opts={
            "fill": "#5B8FF9",
            "fillOpacity": 0.8,
            "stroke": "#2E5BFF",
            "lineWidth": 2,
            "radius": 8,
        },
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="interval 样式配置"),
    )
)
chart.render("interval_style.html")


"""
配置纹理
G2 文档: https://g2.antv.antgroup.com/examples/style/bindling/#pattern-config
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "A", "value": 30}, {"name": "B", "value": 50},
    {"name": "C", "value": 45}, {"name": "D", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="配置纹理"),
    )
)
chart.render("pattern_config.html")

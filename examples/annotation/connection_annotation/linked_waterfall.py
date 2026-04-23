"""
链接线标记的瀑布图
G2 文档: https://g2.antv.antgroup.com/examples/annotation/connection/#linked-waterfall
"""
from pyantv import options as opts
from pyantv.charts import Interval, Connector, View

data = [
    {"type": "收入", "value": 100},
    {"type": "成本", "value": -40},
    {"type": "税费", "value": -15},
    {"type": "利润", "value": 45},
]

bar = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value", color_field="type")
)

connector = (
    Connector()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="value")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#888"),
    )
)

chart = (
    View()
    .set_view_children(children=[bar.options, connector.options])
    .set_global_options(title_opts=opts.TitleOpts(title="链接线标记的瀑布图"))
)
chart.render("linked_waterfall.html")

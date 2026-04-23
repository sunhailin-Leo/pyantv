"""
连续图例
G2 文档: https://g2.antv.antgroup.com/examples/component/legend/#continuous-legend
"""
from pyantv import options as opts
from pyantv.charts import Cell

data = [
    {"x": "A", "y": "1", "value": 10},
    {"x": "A", "y": "2", "value": 30},
    {"x": "B", "y": "1", "value": 50},
    {"x": "B", "y": "2", "value": 70},
    {"x": "C", "y": "1", "value": 20},
    {"x": "C", "y": "2", "value": 90},
]

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="连续图例"),
    )
)
chart.render("continuous_legend.html")

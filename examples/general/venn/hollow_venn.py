"""
空心韦恩图
G2 文档: https://g2.antv.antgroup.com/examples/general/venn/#hollow-venn
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"set": "集合A", "value": 15, "x": 35, "y": 50},
    {"set": "集合B", "value": 15, "x": 65, "y": 50},
    {"set": "A∩B", "value": 5, "x": 50, "y": 50},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="value", color_field="set")
    .set_global_options(
        title_opts=opts.TitleOpts(title="空心韦恩图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.1, stroke="#333", line_width=2),
    )
)
chart.render("hollow_venn.html")

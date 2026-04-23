"""
韦恩图
G2 文档: https://g2.antv.antgroup.com/examples/general/venn/#venn
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"set": "A", "value": 12, "x": 30, "y": 50},
    {"set": "B", "value": 12, "x": 70, "y": 50},
    {"set": "A∩B", "value": 4, "x": 50, "y": 50},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="value", color_field="set")
    .set_global_options(
        title_opts=opts.TitleOpts(title="韦恩图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.5),
    )
)
chart.render("venn.html")

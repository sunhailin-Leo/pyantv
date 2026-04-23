"""
堆叠散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#stacked-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"x": "A", "y": 1, "type": "类型1"},
    {"x": "A", "y": 1, "type": "类型2"},
    {"x": "A", "y": 1, "type": "类型1"},
    {"x": "A", "y": 1, "type": "类型2"},
    {"x": "A", "y": 1, "type": "类型1"},
    {"x": "B", "y": 1, "type": "类型1"},
    {"x": "B", "y": 1, "type": "类型2"},
    {"x": "B", "y": 1, "type": "类型1"},
    {"x": "B", "y": 1, "type": "类型2"},
    {"x": "C", "y": 1, "type": "类型1"},
    {"x": "C", "y": 1, "type": "类型2"},
    {"x": "C", "y": 1, "type": "类型1"},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="type")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        title_opts=opts.TitleOpts(title="堆叠散点图"),
    )
)
chart.render("stacked_scatter.html")

"""
三角形
G2 文档: https://g2.antv.antgroup.com/examples/threed/scatter/#triangle
"""
from pyantv import options as opts
from pyantv.charts import Point

data = []
for i in range(10):
    for j in range(i + 1):
        data.append({"x": j - i / 2, "y": -i, "value": i + j})

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="三角形"),
    )
)
chart.render("triangle.html")

"""
二维单元可视化
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/unit/#two-dimensional
"""
from pyantv import options as opts
from pyantv.charts import Cell

data = [{"x": i % 10, "y": i // 10, "value": (i * 7) % 100} for i in range(100)]

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="二维单元可视化"),
    )
)
chart.render("two_dimensional.html")

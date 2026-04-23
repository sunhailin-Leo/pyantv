"""
基础单元可视化
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/unit/#basic
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [{"x": i % 10, "y": i // 10, "value": i} for i in range(100)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="基础单元可视化"),
    )
)
chart.render("basic.html")

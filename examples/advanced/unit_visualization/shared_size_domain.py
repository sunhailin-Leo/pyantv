"""
共享尺寸定义域
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/unit/#shared-size-domain
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [{"x": i % 10, "y": i // 10, "size": (i % 5 + 1) * 3, "category": "A" if i < 50 else "B"} for i in range(100)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", size_field="size", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="共享尺寸定义域"),
    )
)
chart.render("shared_size_domain.html")

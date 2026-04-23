"""
共享数据定义域
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/unit/#shared-data-domain
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [{"x": i % 10, "y": i // 10, "value": i * 2, "group": chr(65 + i % 3)} for i in range(100)]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="group")
    .set_global_options(
        title_opts=opts.TitleOpts(title="共享数据定义域"),
    )
)
chart.render("shared_data_domain.html")

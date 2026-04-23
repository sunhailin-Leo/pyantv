"""
贡献者
G2 文档: https://g2.antv.antgroup.com/examples/general/image/#contributors
"""
from pyantv import options as opts
from pyantv.charts import Image

data = [
    {"name": "Alice", "commits": 120, "x": 0, "y": 0},
    {"name": "Bob", "commits": 95, "x": 1, "y": 0},
    {"name": "Charlie", "commits": 80, "x": 2, "y": 0},
    {"name": "Diana", "commits": 65, "x": 3, "y": 0},
    {"name": "Eve", "commits": 50, "x": 4, "y": 0},
]

chart = (
    Image()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="贡献者"),
    )
)
chart.render("contributors.html")

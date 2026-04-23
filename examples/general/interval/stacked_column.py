"""
堆叠柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#stacked-column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "London", "month": "Jan.", "rainfall": 18.9},
    {"name": "London", "month": "Feb.", "rainfall": 28.8},
    {"name": "London", "month": "Mar.", "rainfall": 39.3},
    {"name": "London", "month": "Apr.", "rainfall": 81.4},
    {"name": "London", "month": "May", "rainfall": 47},
    {"name": "London", "month": "Jun.", "rainfall": 20.3},
    {"name": "London", "month": "Jul.", "rainfall": 24},
    {"name": "London", "month": "Aug.", "rainfall": 35.6},
    {"name": "Berlin", "month": "Jan.", "rainfall": 12.4},
    {"name": "Berlin", "month": "Feb.", "rainfall": 23.2},
    {"name": "Berlin", "month": "Mar.", "rainfall": 34.5},
    {"name": "Berlin", "month": "Apr.", "rainfall": 99.7},
    {"name": "Berlin", "month": "May", "rainfall": 52.6},
    {"name": "Berlin", "month": "Jun.", "rainfall": 35.5},
    {"name": "Berlin", "month": "Jul.", "rainfall": 37.4},
    {"name": "Berlin", "month": "Aug.", "rainfall": 42.4},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="rainfall", color_field="name")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        title_opts=opts.TitleOpts(title="堆叠柱形图"),
    )
)

chart.render("stacked_column.html")


"""
通过点获取数据
G2 文档: https://g2.antv.antgroup.com/examples/interaction/event/#get-data-by-point
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "产品A", "sales": 120}, {"name": "产品B", "sales": 200},
    {"name": "产品C", "sales": 150}, {"name": "产品D", "sales": 80},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="sales", color_field="name")
    .set_global_options(
        title_opts=opts.TitleOpts(title="通过点获取数据"),
        tooltip_opts=opts.TooltipOpts(),
    )
)
chart.render("get_data_by_point.html")

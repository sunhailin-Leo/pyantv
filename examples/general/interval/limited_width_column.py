"""
限制宽度的柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#column-bindwidth
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "sales": 120},
    {"month": "2月", "sales": 250},
    {"month": "3月", "sales": 180},
    {"month": "4月", "sales": 310},
    {"month": "5月", "sales": 200},
    {"month": "6月", "sales": 150},
    {"month": "7月", "sales": 290},
    {"month": "8月", "sales": 340},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_interval_style(max_width=40)
    .set_global_options(
        title_opts=opts.TitleOpts(title="限制宽度的柱形图"),
    )
)
chart.render("limited_width_column.html")

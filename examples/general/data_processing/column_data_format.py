"""
列数据格式
G2 文档: https://g2.antv.antgroup.com/examples/general/data-processing/#column-data-format
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "1月", "sales": 120},
    {"month": "2月", "sales": 150},
    {"month": "3月", "sales": 130},
    {"month": "4月", "sales": 160},
    {"month": "5月", "sales": 140},
    {"month": "6月", "sales": 170},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_global_options(
        title_opts=opts.TitleOpts(title="列数据格式"),
    )
)
chart.render("column_data_format.html")

"""
简单柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"year": "1951 年", "sales": 38},
    {"year": "1952 年", "sales": 52},
    {"year": "1956 年", "sales": 61},
    {"year": "1957 年", "sales": 145},
    {"year": "1958 年", "sales": 48},
    {"year": "1959 年", "sales": 38},
    {"year": "1960 年", "sales": 38},
    {"year": "1962 年", "sales": 38},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="sales")
    .set_global_options(
        title_opts=opts.TitleOpts(title="简单柱形图"),
    )
)

chart.render("simple_column.html")

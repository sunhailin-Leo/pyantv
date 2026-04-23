"""
限制高度的柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#column-bindheight
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"city": "北京", "temperature": 28},
    {"city": "上海", "temperature": 30},
    {"city": "广州", "temperature": 33},
    {"city": "深圳", "temperature": 32},
    {"city": "成都", "temperature": 25},
    {"city": "杭州", "temperature": 29},
    {"city": "武汉", "temperature": 31},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="city", y_field_name="temperature")
    .set_interval_style(min_height=20)
    .set_global_options(
        title_opts=opts.TitleOpts(title="限制高度的柱形图"),
    )
)
chart.render("limited_height_column.html")

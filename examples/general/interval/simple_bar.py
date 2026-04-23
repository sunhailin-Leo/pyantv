"""
简单条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"country": "巴西", "population": 18203},
    {"country": "印尼", "population": 23489},
    {"country": "美国", "population": 29034},
    {"country": "印度", "population": 104970},
    {"country": "中国", "population": 131744},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="country", y_field_name="population")
    .set_global_options(
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="简单条形图"),
    )
)

chart.render("simple_bar.html")

"""
学术风格
G2 文档: https://g2.antv.antgroup.com/examples/style/theme/#academy
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2018", "value": 100}, {"year": "2019", "value": 120},
    {"year": "2020", "value": 115}, {"year": "2021", "value": 140},
    {"year": "2022", "value": 160},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="学术风格"),
    )
)
chart.render("academy.html")

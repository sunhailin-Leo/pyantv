"""
斜率图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#slope
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2020", "category": "产品A", "value": 120},
    {"year": "2022", "category": "产品A", "value": 180},
    {"year": "2020", "category": "产品B", "value": 200},
    {"year": "2022", "category": "产品B", "value": 150},
    {"year": "2020", "category": "产品C", "value": 80},
    {"year": "2022", "category": "产品C", "value": 220},
    {"year": "2020", "category": "产品D", "value": 160},
    {"year": "2022", "category": "产品D", "value": 190},
    {"year": "2020", "category": "产品E", "value": 300},
    {"year": "2022", "category": "产品E", "value": 250},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="斜率图"),
        label_opts=[opts.LabelOpts(text_opts="value")]
    )
)
chart.render("slope.html")

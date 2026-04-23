"""
面积图特殊标签
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#area-special-label
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "2015", "value": 38},
    {"year": "2016", "value": 52},
    {"year": "2017", "value": 61},
    {"year": "2018", "value": 145},
    {"year": "2019", "value": 48},
    {"year": "2020", "value": 38},
    {"year": "2021", "value": 68},
    {"year": "2022", "value": 98},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="面积图特殊标签"),
        label_opts=[opts.LabelOpts(text_opts="value", font_size=12)],
    )
)
chart.render("area_special_label.html")

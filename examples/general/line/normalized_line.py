"""
归一化折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#normalized-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"year": "2018", "type": "产品A", "value": 100},
    {"year": "2018", "type": "产品B", "value": 500},
    {"year": "2019", "type": "产品A", "value": 150},
    {"year": "2019", "type": "产品B", "value": 600},
    {"year": "2020", "type": "产品A", "value": 200},
    {"year": "2020", "type": "产品B", "value": 750},
    {"year": "2021", "type": "产品A", "value": 280},
    {"year": "2021", "type": "产品B", "value": 900},
    {"year": "2022", "type": "产品A", "value": 350},
    {"year": "2022", "type": "产品B", "value": 1100},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="归一化折线图"),
        transform_opts=[opts.TransformNormalizeYOpts()]
    )
)
chart.render("normalized_line.html")

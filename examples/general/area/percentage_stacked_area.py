"""
百分比堆叠面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#percentage-stacked-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "2018", "type": "产品A", "value": 100},
    {"year": "2018", "type": "产品B", "value": 200},
    {"year": "2018", "type": "产品C", "value": 150},
    {"year": "2019", "type": "产品A", "value": 150},
    {"year": "2019", "type": "产品B", "value": 250},
    {"year": "2019", "type": "产品C", "value": 180},
    {"year": "2020", "type": "产品A", "value": 200},
    {"year": "2020", "type": "产品B", "value": 300},
    {"year": "2020", "type": "产品C", "value": 220},
    {"year": "2021", "type": "产品A", "value": 280},
    {"year": "2021", "type": "产品B", "value": 350},
    {"year": "2021", "type": "产品C", "value": 260},
    {"year": "2022", "type": "产品A", "value": 350},
    {"year": "2022", "type": "产品B", "value": 400},
    {"year": "2022", "type": "产品C", "value": 300},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="百分比堆叠面积图"),
        transform_opts=[opts.TransformStackYOpts(), opts.TransformNormalizeYOpts()]
    )
)
chart.render("percentage_stacked_area.html")

"""
出现顺序堆叠面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#appearance-order-stacked-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "2018", "type": "A", "value": 100},
    {"year": "2018", "type": "B", "value": 300},
    {"year": "2018", "type": "C", "value": 200},
    {"year": "2019", "type": "A", "value": 200},
    {"year": "2019", "type": "B", "value": 250},
    {"year": "2019", "type": "C", "value": 300},
    {"year": "2020", "type": "A", "value": 350},
    {"year": "2020", "type": "B", "value": 200},
    {"year": "2020", "type": "C", "value": 250},
    {"year": "2021", "type": "A", "value": 400},
    {"year": "2021", "type": "B", "value": 150},
    {"year": "2021", "type": "C", "value": 350},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="出现顺序堆叠面积图"),
        transform_opts=[opts.TransformStackYOpts(order_by="value")],
    )
)
chart.render("appearance_order_stacked_area.html")

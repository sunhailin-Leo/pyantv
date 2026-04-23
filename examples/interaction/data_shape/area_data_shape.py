"""
面积图-数形交互
G2 文档: https://g2.antv.antgroup.com/examples/interaction/data-shape/#area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "1月", "city": "北京", "value": 30},
    {"month": "2月", "city": "北京", "value": 45},
    {"month": "3月", "city": "北京", "value": 55},
    {"month": "1月", "city": "上海", "value": 40},
    {"month": "2月", "city": "上海", "value": 50},
    {"month": "3月", "city": "上海", "value": 60},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="面积图-数形交互"),
        transform_opts=[opts.TransformStackYOpts()],
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("area_data_shape.html")

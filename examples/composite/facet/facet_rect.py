
"""
矩行分面
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#facet-rect
"""
from pyantv import options as opts
from pyantv.charts import Point, FacetRect

data = [
    {"gender": "男", "age_group": "青年", "height": 175, "weight": 70},
    {"gender": "男", "age_group": "青年", "height": 180, "weight": 75},
    {"gender": "男", "age_group": "中年", "height": 172, "weight": 80},
    {"gender": "男", "age_group": "中年", "height": 178, "weight": 85},
    {"gender": "女", "age_group": "青年", "height": 162, "weight": 55},
    {"gender": "女", "age_group": "青年", "height": 165, "weight": 58},
    {"gender": "女", "age_group": "中年", "height": 160, "weight": 62},
    {"gender": "女", "age_group": "中年", "height": 163, "weight": 65},
]

scatter = (
    Point()
    .set_encode(x_field_name="height", y_field_name="weight", color_field="gender")
)

chart = (
    FacetRect()
    .set_data(data=data)
    .set_encode(x_field_name="gender", y_field_name="age_group")
    .set_facet_rect_children(children=[scatter.options])
    .set_global_options(title_opts=opts.TitleOpts(title="矩行分面"))
)
chart.render("facet_rect.html")

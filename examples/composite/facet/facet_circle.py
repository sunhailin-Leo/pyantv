
"""
圆形分面
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#facet-circle
"""
from pyantv import options as opts
from pyantv.charts import Interval, FacetCircle

data = [
    {"month": "1月", "category": "A", "value": 30},
    {"month": "1月", "category": "B", "value": 40},
    {"month": "2月", "category": "A", "value": 35},
    {"month": "2月", "category": "B", "value": 45},
    {"month": "3月", "category": "A", "value": 40},
    {"month": "3月", "category": "B", "value": 50},
    {"month": "4月", "category": "A", "value": 45},
    {"month": "4月", "category": "B", "value": 55},
]

bar = (
    Interval()
    .set_encode(x_field_name="category", y_field_name="value", color_field="category")
)

chart = (
    FacetCircle()
    .set_data(data=data)
    .set_encode(x_field_name="month")
    .set_facet_circle_children(children=[bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="圆形分面"))
)
chart.render("facet_circle.html")

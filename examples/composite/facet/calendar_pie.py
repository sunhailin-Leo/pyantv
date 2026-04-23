
"""
日历饼图
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#calendar-pie
"""
from pyantv import options as opts
from pyantv.charts import Interval, FacetRect

data = [
    {"quarter": "Q1", "category": "A", "value": 30},
    {"quarter": "Q1", "category": "B", "value": 40},
    {"quarter": "Q1", "category": "C", "value": 30},
    {"quarter": "Q2", "category": "A", "value": 25},
    {"quarter": "Q2", "category": "B", "value": 45},
    {"quarter": "Q2", "category": "C", "value": 30},
    {"quarter": "Q3", "category": "A", "value": 35},
    {"quarter": "Q3", "category": "B", "value": 35},
    {"quarter": "Q3", "category": "C", "value": 30},
    {"quarter": "Q4", "category": "A", "value": 40},
    {"quarter": "Q4", "category": "B", "value": 30},
    {"quarter": "Q4", "category": "C", "value": 30},
]

pie = (
    Interval()
    .set_encode(y_field_name="value", color_field="category")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(),
    )
)

chart = (
    FacetRect()
    .set_data(data=data)
    .set_encode(x_field_name="quarter")
    .set_facet_rect_children(children=[pie.options])
    .set_global_options(title_opts=opts.TitleOpts(title="日历饼图"))
)
chart.render("calendar_pie.html")

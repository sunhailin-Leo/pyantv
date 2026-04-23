
"""
列矩行分面
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#col-facet-rect
"""
from pyantv import options as opts
from pyantv.charts import Interval, FacetRect

data = [
    {"city": "北京", "month": "1月", "value": 30},
    {"city": "北京", "month": "2月", "value": 45},
    {"city": "上海", "month": "1月", "value": 40},
    {"city": "上海", "month": "2月", "value": 50},
    {"city": "广州", "month": "1月", "value": 25},
    {"city": "广州", "month": "2月", "value": 38},
]

bar = (
    Interval()
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
)

chart = (
    FacetRect()
    .set_data(data=data)
    .set_encode(x_field_name="city")
    .set_facet_rect_children(children=[bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="列矩行分面"))
)
chart.render("col_facet_rect.html")


"""
日历条形图
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#calendar-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval, FacetRect

data = [
    {"week": "周一", "hour": "9:00", "value": 30},
    {"week": "周一", "hour": "10:00", "value": 45},
    {"week": "周一", "hour": "11:00", "value": 50},
    {"week": "周二", "hour": "9:00", "value": 35},
    {"week": "周二", "hour": "10:00", "value": 40},
    {"week": "周二", "hour": "11:00", "value": 55},
    {"week": "周三", "hour": "9:00", "value": 25},
    {"week": "周三", "hour": "10:00", "value": 38},
    {"week": "周三", "hour": "11:00", "value": 42},
]

bar = (
    Interval()
    .set_encode(x_field_name="hour", y_field_name="value")
)

chart = (
    FacetRect()
    .set_data(data=data)
    .set_encode(y_field_name="week")
    .set_facet_rect_children(children=[bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="日历条形图"))
)
chart.render("calendar_bar.html")

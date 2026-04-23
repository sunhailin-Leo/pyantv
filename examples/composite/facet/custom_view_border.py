"""
自定义视图边框
G2 文档: https://g2.antv.antgroup.com/examples/composition/facet/#custom-view-border
"""
from pyantv import options as opts
from pyantv.charts import Interval, FacetRect

data = [
    {"region": "华东", "product": "A", "sales": 120},
    {"region": "华东", "product": "B", "sales": 150},
    {"region": "华北", "product": "A", "sales": 100},
    {"region": "华北", "product": "B", "sales": 130},
    {"region": "华南", "product": "A", "sales": 140},
    {"region": "华南", "product": "B", "sales": 160},
]

bar = (
    Interval()
    .set_encode(x_field_name="product", y_field_name="sales", color_field="product")
)

chart = (
    FacetRect()
    .set_data(data=data)
    .set_encode(x_field_name="region")
    .set_facet_rect_children(children=[bar.options])
    .set_global_options(title_opts=opts.TitleOpts(title="自定义视图边框"))
)
chart.render("custom_view_border.html")

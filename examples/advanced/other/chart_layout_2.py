"""
图表布局(二)
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#chart-layout-2
"""
from pyantv import options as opts
from pyantv.charts import SpaceFlex, Interval, Area, Line

data1 = [{"month": "1月", "value": 30}, {"month": "2月", "value": 50}, {"month": "3月", "value": 45}]
data2 = [{"month": "1月", "value": 20}, {"month": "2月", "value": 40}, {"month": "3月", "value": 35}]
data3 = [{"month": "1月", "value": 25}, {"month": "2月", "value": 45}, {"month": "3月", "value": 55}]

bar = (
    Interval()
    .set_data(data=data1)
    .set_encode(x_field_name="month", y_field_name="value")
)

area = (
    Area()
    .set_data(data=data2)
    .set_encode(x_field_name="month", y_field_name="value")
)

line = (
    Line()
    .set_data(data=data3)
    .set_encode(x_field_name="month", y_field_name="value")
)

chart = (
    SpaceFlex()
    .set_space_flex_children(children=[bar.options, area.options, line.options])
    .set_global_options(
        title_opts=opts.TitleOpts(title="图表布局(二)"),
    )
)
chart.render("chart_layout_2.html")

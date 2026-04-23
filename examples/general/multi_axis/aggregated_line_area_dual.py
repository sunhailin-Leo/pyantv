"""
聚合线面双轴图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#aggregated-line-area-dual
"""
from pyantv import options as opts
from pyantv.charts import View, Area, Line

data = [
    {"date": "2020-01", "value": 120, "count": 45},
    {"date": "2020-02", "value": 135, "count": 52},
    {"date": "2020-03", "value": 148, "count": 48},
    {"date": "2020-04", "value": 160, "count": 55},
    {"date": "2020-05", "value": 175, "count": 60},
    {"date": "2020-06", "value": 190, "count": 58},
    {"date": "2020-07", "value": 205, "count": 65},
    {"date": "2020-08", "value": 220, "count": 62},
    {"date": "2020-09", "value": 235, "count": 70},
    {"date": "2020-10", "value": 250, "count": 68},
    {"date": "2020-11", "value": 265, "count": 75},
    {"date": "2020-12", "value": 280, "count": 72},
]

area = (
    Area()
    .set_encode(x_field_name="date", y_field_name="value", shape_field="smooth")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="数值")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.3),
    )
)

line = (
    Line()
    .set_encode(x_field_name="date", y_field_name="count", shape_field="smooth")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="数量")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#5AD8A6", line_width=2),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[area.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="聚合线面双轴图"))
)
chart.render("aggregated_line_area_dual.html")

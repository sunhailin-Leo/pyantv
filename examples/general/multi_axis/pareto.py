"""
帕累托图
G2 文档: https://g2.antv.antgroup.com/examples/general/multi-axis/#pareto
"""
from pyantv import options as opts
from pyantv.charts import View, Interval, Line

raw_data = [
    {"type": "质量问题", "count": 120},
    {"type": "交付延迟", "count": 85},
    {"type": "沟通不畅", "count": 65},
    {"type": "需求变更", "count": 45},
    {"type": "资源不足", "count": 30},
    {"type": "技术难题", "count": 20},
    {"type": "其他", "count": 15},
]

total = sum(item["count"] for item in raw_data)
cumulative = 0
data = []
for item in raw_data:
    cumulative += item["count"]
    data.append({
        "type": item["type"],
        "count": item["count"],
        "cumulative": round(cumulative / total * 100, 1),
    })

bar = (
    Interval()
    .set_encode(x_field_name="type", y_field_name="count")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="频次")),
        ),
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9"),
    )
)

line = (
    Line()
    .set_encode(x_field_name="type", y_field_name="cumulative")
    .set_global_options(
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(axis_title_opts=opts.AxisTitleOpts(title="累计百分比(%)")),
        ),
        style_opts=opts.BaseChartStyleOpts(stroke="#F6BD16", line_width=2),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[bar.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="帕累托图"))
)
chart.render("pareto.html")

"""
子弹柱形图示例

子弹图用于对比实际值与目标值，同时显示范围区间。

G2 文档: https://g2.antv.antgroup.com/examples/interval/interval-bullet
"""

from pyantv import options as opts
from pyantv.charts import SpaceLayer, Interval

# 范围区间图表
ranges_chart = (
    Interval()
    .set_encode(x_field_name="title", y_field_name="ranges")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill="#d8d0c0",
            fill_opacity=0.5,
        ),
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=False,
            ),
        ),
    )
)

# 实际值图表
actual_chart = (
    Interval()
    .set_encode(x_field_name="title", y_field_name="actual")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill="#5b8ff9",
        ),
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=False,
            ),
        ),
    )
)

# 目标值标记
target_chart = (
    Interval()
    .set_encode(x_field_name="title", y_field_name="target")
    .set_interval_style(min_width=20)
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill="#5ad8a6",
        ),
        axis_opts=opts.AxisOpts(
            y_axis_opts=opts.AxisCfgOpts(
                axis_title_opts=False,
            ),
        ),
    )
)

data = [
    {"title": "Revenue", "ranges": 300, "actual": 270, "target": 250},
    {"title": "Profit", "ranges": 30, "actual": 23, "target": 26},
    {"title": "Order Size", "ranges": 600, "actual": 100, "target": 550},
    {"title": "New Customers", "ranges": 2500, "actual": 1650, "target": 2100},
    {"title": "Satisfaction", "ranges": 5, "actual": 3.2, "target": 4.4},
]

c = (
    SpaceLayer()
    .set_data(data=data)
    .set_space_layer_children(
        children=[
            ranges_chart.get_options(),
            actual_chart.get_options(),
            target_chart.get_options(),
        ]
    )
)

c.render("bullet_column.html")

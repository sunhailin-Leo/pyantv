"""
自定义坐标轴标签
G2 文档: https://g2.antv.antgroup.com/examples/component/axis/#custom-axis-label
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"category": "A", "value": 30}, {"category": "B", "value": 50},
    {"category": "C", "value": 45}, {"category": "D", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="category", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义坐标轴标签"),
        axis_opts={
            "x": opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="分类"),
            ),
        },
    )
)
chart.render("custom_axis_label.html")

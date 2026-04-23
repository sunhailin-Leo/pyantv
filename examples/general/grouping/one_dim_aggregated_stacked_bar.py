"""
一维聚合堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#one-dim-aggregated-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "类型A", "value": 40},
    {"type": "类型B", "value": 30},
    {"type": "类型C", "value": 20},
    {"type": "类型D", "value": 10},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="一维聚合堆叠条形图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("one_dim_aggregated_stacked_bar.html")

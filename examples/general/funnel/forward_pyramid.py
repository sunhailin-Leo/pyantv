"""
正向金字塔图
G2 文档: https://g2.antv.antgroup.com/examples/general/funnel/#forward-pyramid
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"stage": "决策层", "value": 100},
    {"stage": "管理层", "value": 500},
    {"stage": "高层", "value": 1500},
    {"stage": "中层", "value": 3000},
    {"stage": "基层", "value": 5000},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="stage", y_field_name="value", color_field="stage", shape_field="pyramid")
    .set_global_options(
        title_opts=opts.TitleOpts(title="正向金字塔图"),
        transform_opts=[opts.TransformSymmetryYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("forward_pyramid.html")

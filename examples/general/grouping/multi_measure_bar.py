"""
多度量条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/grouping/#multi-measure-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"name": "产品A", "metric": "销量", "value": 120},
    {"name": "产品A", "metric": "利润", "value": 80},
    {"name": "产品A", "metric": "增长率", "value": 45},
    {"name": "产品B", "metric": "销量", "value": 100},
    {"name": "产品B", "metric": "利润", "value": 60},
    {"name": "产品B", "metric": "增长率", "value": 55},
    {"name": "产品C", "metric": "销量", "value": 90},
    {"name": "产品C", "metric": "利润", "value": 70},
    {"name": "产品C", "metric": "增长率", "value": 35},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value", color_field="metric")
    .set_global_options(
        title_opts=opts.TitleOpts(title="多度量条形图"),
        transform_opts=[opts.TransformDodgeXOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("multi_measure_bar.html")

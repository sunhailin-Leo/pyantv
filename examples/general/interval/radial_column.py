"""
径向柱形图示例

使用径向坐标系创建的柱形图，适合展示周期性数据。

G2 文档: https://g2.antv.antgroup.com/api/coordinate#radial
"""

from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"question": "问题 1", "percent": 0.21},
    {"question": "问题 2", "percent": 0.40},
    {"question": "问题 3", "percent": 0.49},
    {"question": "问题 4", "percent": 0.52},
    {"question": "问题 5", "percent": 0.53},
    {"question": "问题 6", "percent": 0.84},
    {"question": "问题 7", "percent": 1.0},
    {"question": "问题 8", "percent": 1.2},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="question", y_field_name="percent")
    .set_global_options(coordinate_opts=opts.CoordinateRadialOpts(inner_radius=0.1))
)

c.render("radial_column.html")

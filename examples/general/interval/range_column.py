"""
区间柱形图示例

使用数组数据表示区间范围的柱形图。

G2 文档: https://g2.antv.antgroup.com/api/interval#range
"""

from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"x": "分类一", "y": [76, 100]},
    {"x": "分类二", "y": [56, 108]},
    {"x": "分类三", "y": [38, 129]},
    {"x": "分类四", "y": [58, 155]},
    {"x": "分类五", "y": [45, 120]},
    {"x": "分类六", "y": [23, 99]},
    {"x": "分类七", "y": [18, 56]},
    {"x": "分类八", "y": [18, 34]},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
)

c.render("range_column.html")

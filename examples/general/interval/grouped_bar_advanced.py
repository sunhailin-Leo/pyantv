"""
分组条形图（进阶）
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#grouped-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"department": "研发部", "type": "男性", "count": 45},
    {"department": "研发部", "type": "女性", "count": 25},
    {"department": "市场部", "type": "男性", "count": 30},
    {"department": "市场部", "type": "女性", "count": 35},
    {"department": "财务部", "type": "男性", "count": 15},
    {"department": "财务部", "type": "女性", "count": 20},
    {"department": "人事部", "type": "男性", "count": 10},
    {"department": "人事部", "type": "女性", "count": 18},
    {"department": "运营部", "type": "男性", "count": 22},
    {"department": "运营部", "type": "女性", "count": 28},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="department", y_field_name="count", color_field="type")
    .set_global_options(
        transform_opts=[opts.TransformDodgeXOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="分组条形图（进阶）"),
    )
)
chart.render("grouped_bar_advanced.html")

"""
堆叠条形图（进阶）
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"state": "California", "age": "Under 5", "population": 2704659},
    {"state": "California", "age": "5 to 13", "population": 4499890},
    {"state": "California", "age": "14 to 17", "population": 2159981},
    {"state": "California", "age": "18 to 24", "population": 3853788},
    {"state": "California", "age": "25 to 44", "population": 10604510},
    {"state": "Texas", "age": "Under 5", "population": 2027307},
    {"state": "Texas", "age": "5 to 13", "population": 3277946},
    {"state": "Texas", "age": "14 to 17", "population": 1420518},
    {"state": "Texas", "age": "18 to 24", "population": 2454721},
    {"state": "Texas", "age": "25 to 44", "population": 7017731},
    {"state": "New York", "age": "Under 5", "population": 1208495},
    {"state": "New York", "age": "5 to 13", "population": 2141490},
    {"state": "New York", "age": "14 to 17", "population": 1058031},
    {"state": "New York", "age": "18 to 24", "population": 1999120},
    {"state": "New York", "age": "25 to 44", "population": 5355235},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="state", y_field_name="population", color_field="age")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="堆叠条形图（进阶）"),
    )
)
chart.render("stacked_bar_advanced.html")

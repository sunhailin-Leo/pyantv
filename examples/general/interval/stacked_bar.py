"""
堆叠条形图
G2 文档链接: https://g2.antv.antgroup.com/examples/general/interval#stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"state": "WY", "age": "小于5岁", "population": 25635},
    {"state": "WY", "age": "5至13岁", "population": 1890},
    {"state": "WY", "age": "14至17岁", "population": 9314},
    {"state": "DC", "age": "小于5岁", "population": 30352},
    {"state": "DC", "age": "5至13岁", "population": 20439},
    {"state": "DC", "age": "14至17岁", "population": 10225},
    {"state": "VT", "age": "小于5岁", "population": 38253},
    {"state": "VT", "age": "5至13岁", "population": 42538},
    {"state": "VT", "age": "14至17岁", "population": 15757},
    {"state": "ND", "age": "小于5岁", "population": 51896},
    {"state": "ND", "age": "5至13岁", "population": 67358},
    {"state": "ND", "age": "14至17岁", "population": 18794},
    {"state": "AK", "age": "小于5岁", "population": 72083},
    {"state": "AK", "age": "5至13岁", "population": 85640},
    {"state": "AK", "age": "14至17岁", "population": 22153},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="state", y_field_name="population", color_field="age")
    .set_coordinate(coordinate_opts=opts.CoordinateTransposeOpts())
    .set_global_options(transform_opts=[opts.TransformStackYOpts()])
)
c.render("stacked_bar.html")

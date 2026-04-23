"""
列重复矩阵
G2 文档: https://g2.antv.antgroup.com/examples/composition/repeat/#column-repeat-matrix
"""
from pyantv import options as opts
from pyantv.charts import Point, RepeatMatrix

data = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
    {"sepal_length": 7.0, "sepal_width": 3.2, "petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
    {"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "petal_width": 1.5, "species": "versicolor"},
    {"sepal_length": 6.3, "sepal_width": 3.3, "petal_length": 6.0, "petal_width": 2.5, "species": "virginica"},
    {"sepal_length": 5.8, "sepal_width": 2.7, "petal_length": 5.1, "petal_width": 1.9, "species": "virginica"},
]

scatter = (
    Point()
    .set_encode(color_field="species")
)

chart = (
    RepeatMatrix()
    .set_data(data=data)
    .set_encode(x_field_name="sepal_length", y_field_name="sepal_width")
    .set_repeat_matrix_children(children=[scatter.options])
    .set_global_options(title_opts=opts.TitleOpts(title="列重复矩阵"))
)
chart.render("column_repeat_matrix.html")

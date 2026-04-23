"""
发散条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#diverging
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"age": "85+", "male": -0.4, "female": 0.6},
    {"age": "80-84", "male": -0.6, "female": 0.9},
    {"age": "75-79", "male": -1.0, "female": 1.3},
    {"age": "70-74", "male": -1.5, "female": 1.8},
    {"age": "65-69", "male": -2.2, "female": 2.5},
    {"age": "60-64", "male": -2.8, "female": 3.0},
    {"age": "55-59", "male": -3.4, "female": 3.5},
    {"age": "50-54", "male": -3.6, "female": 3.7},
    {"age": "45-49", "male": -3.5, "female": 3.6},
    {"age": "40-44", "male": -3.3, "female": 3.4},
    {"age": "35-39", "male": -3.2, "female": 3.3},
    {"age": "30-34", "male": -3.5, "female": 3.5},
]

male_data = [{"age": d["age"], "value": d["male"], "gender": "Male"} for d in data]
female_data = [{"age": d["age"], "value": d["female"], "gender": "Female"} for d in data]
chart_data = male_data + female_data

chart = (
    Interval()
    .set_data(data=chart_data)
    .set_encode(x_field_name="age", y_field_name="value", color_field="gender")
    .set_coordinate(coordinate_opts=opts.CoordinateTransposeOpts())
    .set_global_options(
        title_opts=opts.TitleOpts(title="发散条形图"),
    )
)
chart.render("diverging_bar.html")

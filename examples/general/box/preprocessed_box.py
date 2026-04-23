"""
预处理箱线图
G2 文档: https://g2.antv.antgroup.com/examples/general/box/#preprocessed-box
"""
from pyantv import options as opts
from pyantv.charts import Box

data = [
    {"x": "January", "low": 10, "q1": 20, "median": 30, "q3": 40, "high": 50},
    {"x": "February", "low": 15, "q1": 25, "median": 35, "q3": 45, "high": 55},
    {"x": "March", "low": 8, "q1": 18, "median": 28, "q3": 38, "high": 48},
    {"x": "April", "low": 12, "q1": 22, "median": 32, "q3": 42, "high": 52},
    {"x": "May", "low": 18, "q1": 28, "median": 38, "q3": 48, "high": 58},
    {"x": "June", "low": 20, "q1": 30, "median": 40, "q3": 50, "high": 60},
]

chart = (
    Box()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name=["low", "q1", "median", "q3", "high"])
    .set_global_options(
        title_opts=opts.TitleOpts(title="预处理箱线图"),
    )
)
chart.render("preprocessed_box.html")

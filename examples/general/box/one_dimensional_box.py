"""
一维箱线图
G2 文档: https://g2.antv.antgroup.com/examples/general/box/#one-dimensional-box
"""
from pyantv import options as opts
from pyantv.charts import Box

data = [
    {"x": "", "low": 10, "q1": 20, "median": 30, "q3": 40, "high": 50},
]

chart = (
    Box()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name=["low", "q1", "median", "q3", "high"])
    .set_global_options(
        title_opts=opts.TitleOpts(title="一维箱线图"),
        coordinate_opts=opts.CoordinateTransposeOpts(),
    )
)
chart.render("one_dimensional_box.html")

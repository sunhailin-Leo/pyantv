"""
无异常点箱线图
G2 文档: https://g2.antv.antgroup.com/examples/general/box/#no-outlier-box
"""
from pyantv import options as opts
from pyantv.charts import BoxPlot

data = [
    {"x": "January", "y": 18}, {"x": "January", "y": 22}, {"x": "January", "y": 25},
    {"x": "January", "y": 28}, {"x": "January", "y": 30}, {"x": "January", "y": 35},
    {"x": "February", "y": 20}, {"x": "February", "y": 24}, {"x": "February", "y": 27},
    {"x": "February", "y": 32}, {"x": "February", "y": 36}, {"x": "February", "y": 38},
    {"x": "March", "y": 15}, {"x": "March", "y": 19}, {"x": "March", "y": 23},
    {"x": "March", "y": 26}, {"x": "March", "y": 29}, {"x": "March", "y": 33},
]

chart = (
    BoxPlot()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="无异常点箱线图"),
    )
)
chart.render("no_outlier_box.html")

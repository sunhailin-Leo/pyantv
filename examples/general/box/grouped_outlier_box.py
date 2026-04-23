"""
带异常点分组箱线图
G2 文档: https://g2.antv.antgroup.com/examples/general/box/#grouped-outlier-box
"""
from pyantv import options as opts
from pyantv.charts import BoxPlot

data = [
    {"x": "January", "group": "A", "y": 5}, {"x": "January", "group": "A", "y": 18},
    {"x": "January", "group": "A", "y": 22}, {"x": "January", "group": "A", "y": 30},
    {"x": "January", "group": "A", "y": 35}, {"x": "January", "group": "A", "y": 55},
    {"x": "January", "group": "B", "y": 10}, {"x": "January", "group": "B", "y": 20},
    {"x": "January", "group": "B", "y": 28}, {"x": "January", "group": "B", "y": 32},
    {"x": "January", "group": "B", "y": 40}, {"x": "January", "group": "B", "y": 58},
    {"x": "February", "group": "A", "y": 8}, {"x": "February", "group": "A", "y": 15},
    {"x": "February", "group": "A", "y": 25}, {"x": "February", "group": "A", "y": 33},
    {"x": "February", "group": "A", "y": 38}, {"x": "February", "group": "A", "y": 52},
    {"x": "February", "group": "B", "y": 12}, {"x": "February", "group": "B", "y": 22},
    {"x": "February", "group": "B", "y": 30}, {"x": "February", "group": "B", "y": 36},
    {"x": "February", "group": "B", "y": 42}, {"x": "February", "group": "B", "y": 60},
]

chart = (
    BoxPlot()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="group")
    .set_global_options(
        title_opts=opts.TitleOpts(title="带异常点分组箱线图"),
        transform_opts=[opts.TransformDodgeXOpts()],
    )
)
chart.render("grouped_outlier_box.html")

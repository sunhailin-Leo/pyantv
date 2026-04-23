"""
极坐标下的层叠柱状图
G2 文档: https://g2.antv.antgroup.com/examples/general/rose/#polar-stacked-column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"month": "Jan", "type": "食品", "value": 85},
    {"month": "Jan", "type": "日用", "value": 65},
    {"month": "Jan", "type": "服饰", "value": 45},
    {"month": "Feb", "type": "食品", "value": 90},
    {"month": "Feb", "type": "日用", "value": 70},
    {"month": "Feb", "type": "服饰", "value": 50},
    {"month": "Mar", "type": "食品", "value": 100},
    {"month": "Mar", "type": "日用", "value": 80},
    {"month": "Mar", "type": "服饰", "value": 55},
    {"month": "Apr", "type": "食品", "value": 110},
    {"month": "Apr", "type": "日用", "value": 85},
    {"month": "Apr", "type": "服饰", "value": 60},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="极坐标下的层叠柱状图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinatePolarOpts(),
    )
)
chart.render("polar_stacked_column.html")

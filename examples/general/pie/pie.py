"""
饼图
G2 文档: https://g2.antv.antgroup.com/examples/general/pie/#pie
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"item": "事例一", "count": 40, "percent": 0.4},
    {"item": "事例二", "count": 21, "percent": 0.21},
    {"item": "事例三", "count": 17, "percent": 0.17},
    {"item": "事例四", "count": 13, "percent": 0.13},
    {"item": "事例五", "count": 9, "percent": 0.09},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(y_field_name="percent", color_field="item")
    .set_global_options(
        title_opts=opts.TitleOpts(title="饼图"),
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateThetaOpts(),
        label_opts=[opts.LabelOpts(text_opts="percent", position="outside")],
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=1),
    )
)
chart.render("pie.html")

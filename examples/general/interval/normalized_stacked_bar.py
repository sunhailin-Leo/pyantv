"""
归一化堆叠条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#normalized-stacked-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"year": "2019", "browser": "Chrome", "share": 63.7},
    {"year": "2019", "browser": "Safari", "share": 15.7},
    {"year": "2019", "browser": "Firefox", "share": 4.7},
    {"year": "2019", "browser": "Edge", "share": 4.2},
    {"year": "2019", "browser": "Other", "share": 11.7},
    {"year": "2020", "browser": "Chrome", "share": 66.3},
    {"year": "2020", "browser": "Safari", "share": 16.8},
    {"year": "2020", "browser": "Firefox", "share": 3.7},
    {"year": "2020", "browser": "Edge", "share": 3.4},
    {"year": "2020", "browser": "Other", "share": 9.8},
    {"year": "2021", "browser": "Chrome", "share": 64.9},
    {"year": "2021", "browser": "Safari", "share": 18.8},
    {"year": "2021", "browser": "Firefox", "share": 3.6},
    {"year": "2021", "browser": "Edge", "share": 3.9},
    {"year": "2021", "browser": "Other", "share": 8.8},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="share", color_field="browser")
    .set_global_options(
        transform_opts=[
            opts.TransformStackYOpts(),
            opts.TransformNormalizeYOpts(),
        ],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="归一化堆叠条形图"),
    )
)
chart.render("normalized_stacked_bar.html")

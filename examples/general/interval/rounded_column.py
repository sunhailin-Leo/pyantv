"""
圆角柱形图
G2 文档链接: https://g2.antv.antgroup.com/examples/general/interval#rounded-column
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"year": "2015", "value": 38},
    {"year": "2016", "value": 52},
    {"year": "2017", "value": 61},
    {"year": "2018", "value": 145},
    {"year": "2019", "value": 48},
    {"year": "2020", "value": 38},
    {"year": "2021", "value": 38},
    {"year": "2022", "value": 38},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_interval_style(
        base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(
            radius_top_left=20,
            radius_top_right=20
        )
    )
)
c.render("rounded_column.html")

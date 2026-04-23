"""
分组条形图
G2 文档链接: https://g2.antv.antgroup.com/examples/general/interval#grouped-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"label": "Mon.", "type": "series1", "value": 2800},
    {"label": "Mon.", "type": "series2", "value": 2260},
    {"label": "Tues.", "type": "series1", "value": 1800},
    {"label": "Tues.", "type": "series2", "value": 1300},
    {"label": "Wed.", "type": "series1", "value": 950},
    {"label": "Wed.", "type": "series2", "value": 900},
    {"label": "Thur.", "type": "series1", "value": 500},
    {"label": "Thur.", "type": "series2", "value": 390},
    {"label": "Fri.", "type": "series1", "value": 170},
    {"label": "Fri.", "type": "series2", "value": 100},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="label", y_field_name="value", color_field="type")
    .set_coordinate(coordinate_opts=opts.CoordinateTransposeOpts())
    .set_global_options(transform_opts=[opts.TransformDodgeXOpts(group_by="type")])
)
c.render("grouped_bar.html")

"""
缺失折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#missing-line
"""
from pyantv import options as opts
from pyantv.charts import Line
from pyantv.commons.utils import JsCode

data = [
    {"month": "Jan", "value": 120},
    {"month": "Feb", "value": 135},
    {"month": "Mar", "value": None},
    {"month": "Apr", "value": 160},
    {"month": "May", "value": None},
    {"month": "Jun", "value": 200},
    {"month": "Jul", "value": 210},
    {"month": "Aug", "value": None},
    {"month": "Sep", "value": 250},
    {"month": "Oct", "value": 270},
    {"month": "Nov", "value": 280},
    {"month": "Dec", "value": 300},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_line_style(is_defined=JsCode("(d) => d.value !== null && d.value !== undefined"))
    .set_global_options(title_opts=opts.TitleOpts(title="缺失折线图"))
)
chart.render("missing_line.html")

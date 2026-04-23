"""
数据缺失面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#missing-data-area
"""
from pyantv import options as opts
from pyantv.charts import Area
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
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value")
    .set_area_style(is_defined=JsCode("(d) => d.value !== null && d.value !== undefined"))
    .set_global_options(title_opts=opts.TitleOpts(title="数据缺失面积图"))
)
chart.render("missing_data_area.html")

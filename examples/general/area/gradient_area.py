"""
渐变色面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#gradient-area
"""
from pyantv import options as opts
from pyantv.charts import Area
from pyantv.commons.utils import JsCode

data = [
    {"year": "1991", "value": 3},
    {"year": "1992", "value": 4},
    {"year": "1993", "value": 3.5},
    {"year": "1994", "value": 5},
    {"year": "1995", "value": 4.9},
    {"year": "1996", "value": 6},
    {"year": "1997", "value": 7},
    {"year": "1998", "value": 9},
    {"year": "1999", "value": 13},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="渐变色面积图"),
        style_opts=opts.BaseChartStyleOpts(
            fill=JsCode("'l(270) 0:#ffffff 0.5:#7ec2f3 1:#1890ff'"),
        ),
    )
)
chart.render("gradient_area.html")

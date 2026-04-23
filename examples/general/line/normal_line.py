"""
普通折线图（多系列）
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#normal-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"month": "Jan", "city": "Tokyo", "temperature": 7},
    {"month": "Feb", "city": "Tokyo", "temperature": 6.9},
    {"month": "Mar", "city": "Tokyo", "temperature": 9.5},
    {"month": "Apr", "city": "Tokyo", "temperature": 14.5},
    {"month": "May", "city": "Tokyo", "temperature": 18.4},
    {"month": "Jun", "city": "Tokyo", "temperature": 21.5},
    {"month": "Jan", "city": "London", "temperature": 3.9},
    {"month": "Feb", "city": "London", "temperature": 4.2},
    {"month": "Mar", "city": "London", "temperature": 5.7},
    {"month": "Apr", "city": "London", "temperature": 8.5},
    {"month": "May", "city": "London", "temperature": 11.9},
    {"month": "Jun", "city": "London", "temperature": 15.2},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="temperature", color_field="city")
    .set_global_options(title_opts=opts.TitleOpts(title="普通折线图（多系列）"))
)
chart.render("normal_line.html")

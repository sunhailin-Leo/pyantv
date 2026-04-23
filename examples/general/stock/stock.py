"""
股票图
G2 文档: https://g2.antv.antgroup.com/examples/general/stock/#stock
"""
from pyantv import options as opts
from pyantv.charts import View, Line, Area

data = [
    {"date": "2023-01", "price": 150.2, "volume": 1200},
    {"date": "2023-02", "price": 155.8, "volume": 1350},
    {"date": "2023-03", "price": 148.5, "volume": 1100},
    {"date": "2023-04", "price": 162.3, "volume": 1450},
    {"date": "2023-05", "price": 170.1, "volume": 1680},
    {"date": "2023-06", "price": 165.4, "volume": 1520},
    {"date": "2023-07", "price": 178.9, "volume": 1890},
    {"date": "2023-08", "price": 172.6, "volume": 1750},
    {"date": "2023-09", "price": 185.3, "volume": 2100},
    {"date": "2023-10", "price": 180.7, "volume": 1950},
    {"date": "2023-11", "price": 192.4, "volume": 2300},
    {"date": "2023-12", "price": 198.6, "volume": 2500},
]

line = (
    Line()
    .set_encode(x_field_name="date", y_field_name="price")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(stroke="#5B8FF9", line_width=2),
    )
)

area = (
    Area()
    .set_encode(x_field_name="date", y_field_name="price")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.1),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[area.options, line.options])
    .set_global_options(title_opts=opts.TitleOpts(title="股票图"))
)
chart.render("stock.html")

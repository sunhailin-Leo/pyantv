"""
索引图
G2 文档: https://g2.antv.antgroup.com/examples/interaction/other/#index-chart
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01", "stock": "AAPL", "price": 300},
    {"date": "2020-02", "stock": "AAPL", "price": 310},
    {"date": "2020-03", "stock": "AAPL", "price": 280},
    {"date": "2020-04", "stock": "AAPL", "price": 320},
    {"date": "2020-01", "stock": "GOOG", "price": 1400},
    {"date": "2020-02", "stock": "GOOG", "price": 1450},
    {"date": "2020-03", "stock": "GOOG", "price": 1350},
    {"date": "2020-04", "stock": "GOOG", "price": 1500},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="price", color_field="stock")
    .set_global_options(
        title_opts=opts.TitleOpts(title="索引图"),
    )
)
chart.render("index_chart.html")

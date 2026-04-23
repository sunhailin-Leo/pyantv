"""
K线图
G2 文档: https://g2.antv.antgroup.com/examples/general/stock/#candlestick
"""
from pyantv import options as opts
from pyantv.charts import View, Range, Line

data = [
    {"date": "2023-01-02", "open": 150, "close": 155, "high": 158, "low": 148},
    {"date": "2023-01-03", "open": 155, "close": 152, "high": 157, "low": 150},
    {"date": "2023-01-04", "open": 152, "close": 160, "high": 162, "low": 151},
    {"date": "2023-01-05", "open": 160, "close": 158, "high": 163, "low": 156},
    {"date": "2023-01-06", "open": 158, "close": 165, "high": 167, "low": 157},
    {"date": "2023-01-09", "open": 165, "close": 162, "high": 168, "low": 160},
    {"date": "2023-01-10", "open": 162, "close": 170, "high": 172, "low": 161},
    {"date": "2023-01-11", "open": 170, "close": 168, "high": 173, "low": 166},
]

chart = (
    Range()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name=["open", "close"], color_field="date")
    .set_global_options(
        title_opts=opts.TitleOpts(title="K线图"),
    )
)
chart.render("candlestick.html")

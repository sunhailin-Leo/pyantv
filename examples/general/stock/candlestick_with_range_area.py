"""
K线图与范围区域图
G2 文档: https://g2.antv.antgroup.com/examples/general/stock/#candlestick-with-range-area
"""
from pyantv import options as opts
from pyantv.charts import View, Range, RangeY

data = [
    {"date": "01-02", "open": 150, "close": 155, "high": 158, "low": 148},
    {"date": "01-03", "open": 155, "close": 152, "high": 157, "low": 150},
    {"date": "01-04", "open": 152, "close": 160, "high": 162, "low": 151},
    {"date": "01-05", "open": 160, "close": 158, "high": 163, "low": 156},
    {"date": "01-06", "open": 158, "close": 165, "high": 167, "low": 157},
    {"date": "01-09", "open": 165, "close": 162, "high": 168, "low": 160},
    {"date": "01-10", "open": 162, "close": 170, "high": 172, "low": 161},
    {"date": "01-11", "open": 170, "close": 168, "high": 173, "low": 166},
]

candle = (
    Range()
    .set_encode(x_field_name="date", y_field_name=["open", "close"])
)

range_area = (
    RangeY()
    .set_encode(x_field_name="date", y_field_name=["low", "high"])
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.15),
    )
)

chart = (
    View()
    .set_data(data=data)
    .set_view_children(children=[range_area.options, candle.options])
    .set_global_options(title_opts=opts.TitleOpts(title="K线图与范围区域图"))
)
chart.render("candlestick_with_range_area.html")

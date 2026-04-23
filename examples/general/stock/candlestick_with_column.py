"""
K线图与柱状图
G2 文档: https://g2.antv.antgroup.com/examples/general/stock/#candlestick-with-column
"""
from pyantv import options as opts
from pyantv.charts import SpaceFlex, Range, Interval

data = [
    {"date": "01-02", "open": 150, "close": 155, "high": 158, "low": 148, "volume": 1200},
    {"date": "01-03", "open": 155, "close": 152, "high": 157, "low": 150, "volume": 980},
    {"date": "01-04", "open": 152, "close": 160, "high": 162, "low": 151, "volume": 1500},
    {"date": "01-05", "open": 160, "close": 158, "high": 163, "low": 156, "volume": 1100},
    {"date": "01-06", "open": 158, "close": 165, "high": 167, "low": 157, "volume": 1800},
    {"date": "01-09", "open": 165, "close": 162, "high": 168, "low": 160, "volume": 1300},
    {"date": "01-10", "open": 162, "close": 170, "high": 172, "low": 161, "volume": 2000},
    {"date": "01-11", "open": 170, "close": 168, "high": 173, "low": 166, "volume": 1600},
]

candle = (
    Range()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name=["open", "close"])
    .set_global_options(
        title_opts=opts.TitleOpts(title="K线图与柱状图"),
    )
)

volume = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="volume")
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(fill="#5B8FF9", fill_opacity=0.5),
    )
)

chart = (
    SpaceFlex()
    .set_space_flex_children(children=[candle.options, volume.options])
)
chart.render("candlestick_with_column.html")

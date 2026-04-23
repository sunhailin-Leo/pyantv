"""
天气预报动画
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#weather-forecast
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"day": "周一", "high": 25, "low": 18},
    {"day": "周二", "high": 28, "low": 20},
    {"day": "周三", "high": 22, "low": 15},
    {"day": "周四", "high": 30, "low": 22},
    {"day": "周五", "high": 27, "low": 19},
    {"day": "周六", "high": 24, "low": 16},
    {"day": "周日", "high": 26, "low": 18},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="day", y_field_name="high")
    .set_global_options(
        title_opts=opts.TitleOpts(title="天气预报动画"),
        animate_opts=opts.AnimateOpts(),
    )
)
chart.render("weather_forecast.html")

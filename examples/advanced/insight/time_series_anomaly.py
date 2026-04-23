"""
时序异常
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/insight/#time-series-anomaly
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01", "value": 100}, {"date": "2020-02", "value": 110},
    {"date": "2020-03", "value": 105}, {"date": "2020-04", "value": 300},
    {"date": "2020-05", "value": 115}, {"date": "2020-06", "value": 120},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="时序异常"),
    )
)
chart.render("time_series_anomaly.html")

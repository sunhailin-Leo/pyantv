"""
洞察标注算法的详细参数
G2 文档: https://g2.antv.antgroup.com/examples/intelligent/insight/#insight-params
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"date": "2020-01", "value": 100}, {"date": "2020-02", "value": 120},
    {"date": "2020-03", "value": 115}, {"date": "2020-04", "value": 130},
    {"date": "2020-05", "value": 125}, {"date": "2020-06", "value": 140},
    {"date": "2020-07", "value": 135}, {"date": "2020-08", "value": 150},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="date", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="洞察标注算法的详细参数"),
    )
)
chart.render("insight_params.html")

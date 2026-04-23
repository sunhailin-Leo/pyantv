"""
聚合折线图
G2 文档: https://g2.antv.antgroup.com/examples/general/line/#aggregated-line
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [
    {"quarter": "Q1", "region": "华东", "sales": 320},
    {"quarter": "Q1", "region": "华南", "sales": 280},
    {"quarter": "Q1", "region": "华北", "sales": 250},
    {"quarter": "Q2", "region": "华东", "sales": 380},
    {"quarter": "Q2", "region": "华南", "sales": 310},
    {"quarter": "Q2", "region": "华北", "sales": 290},
    {"quarter": "Q3", "region": "华东", "sales": 420},
    {"quarter": "Q3", "region": "华南", "sales": 350},
    {"quarter": "Q3", "region": "华北", "sales": 330},
    {"quarter": "Q4", "region": "华东", "sales": 480},
    {"quarter": "Q4", "region": "华南", "sales": 400},
    {"quarter": "Q4", "region": "华北", "sales": 370},
]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="quarter", y_field_name="sales", color_field="region")
    .set_global_options(title_opts=opts.TitleOpts(title="聚合折线图"))
)
chart.render("aggregated_line.html")

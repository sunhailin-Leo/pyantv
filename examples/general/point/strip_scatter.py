"""
带子散点图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#strip-scatter
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"species": "Adelie", "body_mass": 3750},
    {"species": "Adelie", "body_mass": 3800},
    {"species": "Adelie", "body_mass": 3250},
    {"species": "Adelie", "body_mass": 3450},
    {"species": "Adelie", "body_mass": 3650},
    {"species": "Chinstrap", "body_mass": 3500},
    {"species": "Chinstrap", "body_mass": 3800},
    {"species": "Chinstrap", "body_mass": 3775},
    {"species": "Chinstrap", "body_mass": 4150},
    {"species": "Chinstrap", "body_mass": 3950},
    {"species": "Gentoo", "body_mass": 4500},
    {"species": "Gentoo", "body_mass": 5200},
    {"species": "Gentoo", "body_mass": 5400},
    {"species": "Gentoo", "body_mass": 4750},
    {"species": "Gentoo", "body_mass": 5000},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(x_field_name="species", y_field_name="body_mass", color_field="species")
    .set_global_options(
        title_opts=opts.TitleOpts(title="带子散点图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.65),
    )
)
chart.render("strip_scatter.html")

"""
归一化堆叠面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#normalized-stacked-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"year": "2018", "type": "线上", "value": 320},
    {"year": "2018", "type": "线下", "value": 500},
    {"year": "2019", "type": "线上", "value": 450},
    {"year": "2019", "type": "线下", "value": 450},
    {"year": "2020", "type": "线上", "value": 580},
    {"year": "2020", "type": "线下", "value": 350},
    {"year": "2021", "type": "线上", "value": 650},
    {"year": "2021", "type": "线下", "value": 300},
    {"year": "2022", "type": "线上", "value": 720},
    {"year": "2022", "type": "线下", "value": 280},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="value", color_field="type")
    .set_global_options(
        title_opts=opts.TitleOpts(title="归一化堆叠面积图"),
        transform_opts=[opts.TransformStackYOpts(), opts.TransformNormalizeYOpts()],
    )
)
chart.render("normalized_stacked_area.html")

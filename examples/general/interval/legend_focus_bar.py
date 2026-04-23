"""
图例聚焦条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#legend-focus
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"year": "2019", "type": "线上", "sales": 320},
    {"year": "2019", "type": "线下", "sales": 280},
    {"year": "2020", "type": "线上", "sales": 450},
    {"year": "2020", "type": "线下", "sales": 200},
    {"year": "2021", "type": "线上", "sales": 580},
    {"year": "2021", "type": "线下", "sales": 180},
    {"year": "2022", "type": "线上", "sales": 650},
    {"year": "2022", "type": "线下", "sales": 160},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="year", y_field_name="sales", color_field="type")
    .set_global_options(
        transform_opts=[
            opts.TransformDodgeXOpts(),
        ],
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
        title_opts=opts.TitleOpts(title="图例聚焦条形图"),
    )
)
chart.render("legend_focus_bar.html")

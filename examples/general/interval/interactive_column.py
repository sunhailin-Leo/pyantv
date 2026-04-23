"""
可交互柱形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#interactive
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"genre": "Sports", "sold": 275},
    {"genre": "Strategy", "sold": 115},
    {"genre": "Action", "sold": 120},
    {"genre": "Shooter", "sold": 350},
    {"genre": "Other", "sold": 150},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="genre", y_field_name="sold", color_field="genre")
    .set_interaction(
        interaction_opts={"elementHighlight": {"background": True}},
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="可交互柱形图"),
    )
)
chart.render("interactive_column.html")

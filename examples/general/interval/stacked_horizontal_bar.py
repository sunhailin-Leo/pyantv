"""
堆叠水平条形图
G2 文档: https://g2.antv.antgroup.com/examples/general/interval/#stacked-horizontal-bar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"quarter": "Q1", "product": "产品A", "sales": 120},
    {"quarter": "Q1", "product": "产品B", "sales": 80},
    {"quarter": "Q1", "product": "产品C", "sales": 60},
    {"quarter": "Q2", "product": "产品A", "sales": 150},
    {"quarter": "Q2", "product": "产品B", "sales": 90},
    {"quarter": "Q2", "product": "产品C", "sales": 70},
    {"quarter": "Q3", "product": "产品A", "sales": 180},
    {"quarter": "Q3", "product": "产品B", "sales": 110},
    {"quarter": "Q3", "product": "产品C", "sales": 85},
    {"quarter": "Q4", "product": "产品A", "sales": 200},
    {"quarter": "Q4", "product": "产品B", "sales": 130},
    {"quarter": "Q4", "product": "产品C", "sales": 95},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="quarter", y_field_name="sales", color_field="product")
    .set_global_options(
        transform_opts=[opts.TransformStackYOpts()],
        coordinate_opts=opts.CoordinateTransposeOpts(),
        title_opts=opts.TitleOpts(title="堆叠水平条形图"),
    )
)
chart.render("stacked_horizontal_bar.html")

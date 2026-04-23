
"""
Ctrl/⌘+F 文本搜索
G2 文档: https://g2.antv.antgroup.com/examples/style/bindling/#text-search
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"product": "产品A", "sales": 120}, {"product": "产品B", "sales": 200},
    {"product": "产品C", "sales": 150}, {"product": "产品D", "sales": 80},
    {"product": "产品E", "sales": 180},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="product", y_field_name="sales", color_field="product")
    .set_global_options(
        title_opts=opts.TitleOpts(title="Ctrl/⌘+F 文本搜索"),
    )
)
chart.render("text_search.html")

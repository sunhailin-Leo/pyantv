"""
聚合气泡图
G2 文档: https://g2.antv.antgroup.com/examples/general/point/#aggregated-bubble
"""
from pyantv import options as opts
from pyantv.charts import Point

data = [
    {"category": "电子产品", "sub_category": "手机", "sales": 5200, "profit": 1200, "count": 350},
    {"category": "电子产品", "sub_category": "电脑", "sales": 4800, "profit": 900, "count": 200},
    {"category": "电子产品", "sub_category": "平板", "sales": 2200, "profit": 500, "count": 150},
    {"category": "服装", "sub_category": "上衣", "sales": 3500, "profit": 800, "count": 500},
    {"category": "服装", "sub_category": "裤子", "sales": 2800, "profit": 600, "count": 400},
    {"category": "服装", "sub_category": "鞋子", "sales": 1900, "profit": 350, "count": 300},
    {"category": "食品", "sub_category": "零食", "sales": 1500, "profit": 200, "count": 800},
    {"category": "食品", "sub_category": "饮料", "sales": 2100, "profit": 300, "count": 600},
    {"category": "家居", "sub_category": "家具", "sales": 3200, "profit": 700, "count": 100},
    {"category": "家居", "sub_category": "装饰", "sales": 1800, "profit": 400, "count": 250},
]

chart = (
    Point()
    .set_data(data=data)
    .set_encode(
        x_field_name="sales",
        y_field_name="profit",
        size_field="count",
        color_field="category",
    )
    .set_global_options(
        title_opts=opts.TitleOpts(title="聚合气泡图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.6),
        label_opts=[opts.LabelOpts(text_opts="sub_category", font_size=10)],
    )
)
chart.render("aggregated_bubble.html")

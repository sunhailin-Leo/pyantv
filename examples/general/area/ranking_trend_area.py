"""
排名趋势面积图
G2 文档: https://g2.antv.antgroup.com/examples/general/area/#ranking-trend-area
"""
from pyantv import options as opts
from pyantv.charts import Area

data = [
    {"month": "Jan", "brand": "品牌A", "rank": 1},
    {"month": "Feb", "brand": "品牌A", "rank": 2},
    {"month": "Mar", "brand": "品牌A", "rank": 1},
    {"month": "Apr", "brand": "品牌A", "rank": 3},
    {"month": "May", "brand": "品牌A", "rank": 2},
    {"month": "Jun", "brand": "品牌A", "rank": 1},
    {"month": "Jan", "brand": "品牌B", "rank": 3},
    {"month": "Feb", "brand": "品牌B", "rank": 1},
    {"month": "Mar", "brand": "品牌B", "rank": 2},
    {"month": "Apr", "brand": "品牌B", "rank": 1},
    {"month": "May", "brand": "品牌B", "rank": 3},
    {"month": "Jun", "brand": "品牌B", "rank": 2},
    {"month": "Jan", "brand": "品牌C", "rank": 2},
    {"month": "Feb", "brand": "品牌C", "rank": 3},
    {"month": "Mar", "brand": "品牌C", "rank": 3},
    {"month": "Apr", "brand": "品牌C", "rank": 2},
    {"month": "May", "brand": "品牌C", "rank": 1},
    {"month": "Jun", "brand": "品牌C", "rank": 3},
]

chart = (
    Area()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="rank", color_field="brand", shape_field="smooth")
    .set_global_options(
        title_opts=opts.TitleOpts(title="排名趋势面积图"),
        style_opts=opts.BaseChartStyleOpts(fill_opacity=0.3),
    )
)
chart.render("ranking_trend_area.html")

"""
旭日图自定义颜色通道
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst-custom-color
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "食品", "children": [
            {"name": "水果", "value": 80},
            {"name": "蔬菜", "value": 60},
        ]},
        {"name": "电子", "children": [
            {"name": "手机", "value": 120},
            {"name": "电脑", "value": 100},
        ]},
        {"name": "服饰", "children": [
            {"name": "男装", "value": 70},
            {"name": "女装", "value": 90},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图自定义颜色通道"),
    )
)
chart.render("sunburst_custom_color.html")

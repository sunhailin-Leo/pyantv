"""
旭日图带标签
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst-with-label
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "技术", "children": [
            {"name": "前端", "value": 120},
            {"name": "后端", "value": 100},
            {"name": "算法", "value": 80},
        ]},
        {"name": "产品", "children": [
            {"name": "设计", "value": 90},
            {"name": "运营", "value": 70},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图带标签"),
        label_opts=[opts.LabelOpts(text_opts="name", font_size=10)],
    )
)
chart.render("sunburst_with_label.html")

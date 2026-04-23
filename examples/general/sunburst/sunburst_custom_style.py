"""
旭日图自定义样式
G2 文档: https://g2.antv.antgroup.com/examples/general/sunburst/#sunburst-custom-style
"""
from pyantv import options as opts
from pyantv.charts import TreeMap

data = {
    "name": "root",
    "children": [
        {"name": "A", "children": [
            {"name": "A1", "value": 50},
            {"name": "A2", "value": 40},
        ]},
        {"name": "B", "children": [
            {"name": "B1", "value": 60},
            {"name": "B2", "value": 30},
        ]},
    ],
}

chart = (
    TreeMap()
    .set_data(data=data)
    .set_global_options(
        title_opts=opts.TitleOpts(title="旭日图自定义样式"),
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", line_width=2),
    )
)
chart.render("sunburst_custom_style.html")

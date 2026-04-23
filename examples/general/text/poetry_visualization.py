"""
诗词可视化
G2 文档: https://g2.antv.antgroup.com/examples/general/text/#poetry-visualization
"""
from pyantv import options as opts
from pyantv.charts import Text

data = [
    {"x": 0.5, "y": 0.85, "text": "静夜思", "size": 24},
    {"x": 0.5, "y": 0.7, "text": "李白", "size": 14},
    {"x": 0.5, "y": 0.55, "text": "床前明月光", "size": 18},
    {"x": 0.5, "y": 0.45, "text": "疑是地上霜", "size": 18},
    {"x": 0.5, "y": 0.35, "text": "举头望明月", "size": 18},
    {"x": 0.5, "y": 0.25, "text": "低头思故乡", "size": 18},
]

chart = (
    Text()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="诗词可视化"),
        style_opts=opts.BaseChartStyleOpts(text_align="center"),
    )
)
chart.render("poetry_visualization.html")

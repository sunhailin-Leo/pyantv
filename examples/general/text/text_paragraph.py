"""
文本段落
G2 文档: https://g2.antv.antgroup.com/examples/general/text/#text-paragraph
"""
from pyantv import options as opts
from pyantv.charts import Text

data = [
    {"x": 0.5, "y": 0.9, "text": "2023年度报告", "size": 24},
    {"x": 0.5, "y": 0.75, "text": "总收入: ¥1,234,567", "size": 18},
    {"x": 0.5, "y": 0.6, "text": "同比增长: 15.2%", "size": 16},
    {"x": 0.5, "y": 0.45, "text": "净利润: ¥456,789", "size": 16},
    {"x": 0.5, "y": 0.3, "text": "客户满意度: 95.8%", "size": 14},
]

chart = (
    Text()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="文本段落"),
        style_opts=opts.BaseChartStyleOpts(text_align="center"),
    )
)
chart.render("text_paragraph.html")

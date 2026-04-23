"""
带图片遮罩的词云图
G2 文档: https://g2.antv.antgroup.com/examples/general/wordcloud/#masked-wordcloud
"""
from pyantv import options as opts
from pyantv.charts import Wordcloud

data = [
    {"text": "数据可视化", "value": 100},
    {"text": "人工智能", "value": 90},
    {"text": "机器学习", "value": 85},
    {"text": "深度学习", "value": 80},
    {"text": "大数据", "value": 75},
    {"text": "云计算", "value": 70},
    {"text": "区块链", "value": 60},
    {"text": "物联网", "value": 55},
    {"text": "自然语言处理", "value": 50},
    {"text": "计算机视觉", "value": 48},
    {"text": "推荐系统", "value": 45},
    {"text": "知识图谱", "value": 42},
    {"text": "强化学习", "value": 38},
    {"text": "联邦学习", "value": 35},
    {"text": "边缘计算", "value": 30},
]

chart = (
    Wordcloud()
    .set_data(data=data)
    .set_encode(color_field="text")
    .set_global_options(
        title_opts=opts.TitleOpts(title="带图片遮罩的词云图"),
    )
)
chart.render("masked_wordcloud.html")

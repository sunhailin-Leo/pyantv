"""
英文字符词云图
G2 文档: https://g2.antv.antgroup.com/examples/general/wordcloud/#english-wordcloud
"""
from pyantv import options as opts
from pyantv.charts import Wordcloud

data = [
    {"text": "Python", "value": 100},
    {"text": "JavaScript", "value": 95},
    {"text": "Java", "value": 85},
    {"text": "TypeScript", "value": 80},
    {"text": "Go", "value": 70},
    {"text": "Rust", "value": 65},
    {"text": "C++", "value": 60},
    {"text": "Swift", "value": 55},
    {"text": "Kotlin", "value": 50},
    {"text": "Ruby", "value": 45},
    {"text": "PHP", "value": 40},
    {"text": "Scala", "value": 35},
    {"text": "Dart", "value": 30},
    {"text": "R", "value": 28},
    {"text": "Lua", "value": 25},
    {"text": "Perl", "value": 22},
    {"text": "Haskell", "value": 20},
    {"text": "Elixir", "value": 18},
    {"text": "Clojure", "value": 15},
    {"text": "Julia", "value": 12},
]

chart = (
    Wordcloud()
    .set_data(data=data)
    .set_encode(color_field="text")
    .set_global_options(
        title_opts=opts.TitleOpts(title="英文字符词云图"),
    )
)
chart.render("english_wordcloud.html")

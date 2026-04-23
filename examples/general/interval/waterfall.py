"""
瀑布图
G2 文档链接: https://g2.antv.antgroup.com/examples/general/interval#waterfall
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"type": "日用品", "money": 120},
    {"type": "伙食费", "money": 900},
    {"type": "交通费", "money": 200},
    {"type": "水电费", "money": 300},
    {"type": "房租", "money": 1200},
    {"type": "商场消费", "money": 1000},
    {"type": "应酬交际", "money": 2000},
]

c = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="type", y_field_name="money")
    .set_global_options(transform_opts=[
        opts.TransformStackYOpts(),
        opts.TransformDiffXOpts()
    ])
)
c.render("waterfall.html")

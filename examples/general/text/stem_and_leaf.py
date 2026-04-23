"""
茎叶图
G2 文档: https://g2.antv.antgroup.com/examples/general/text/#stem-and-leaf
"""
from pyantv import options as opts
from pyantv.charts import Text

raw_values = [12, 15, 18, 21, 23, 25, 27, 31, 33, 35, 38, 41, 43, 45, 48, 52, 55, 58]

data = []
for val in raw_values:
    stem = val // 10
    leaf = val % 10
    data.append({"x": stem, "y": leaf, "text": str(leaf)})

chart = (
    Text()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y")
    .set_global_options(
        title_opts=opts.TitleOpts(title="茎叶图"),
    )
)
chart.render("stem_and_leaf.html")

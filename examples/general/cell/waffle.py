"""
华夫饼图
G2 文档: https://g2.antv.antgroup.com/examples/general/cell/#waffle
"""
from pyantv import options as opts
from pyantv.charts import Cell

data = []
colors = ["#5B8FF9", "#61DDAA", "#65789B", "#F6BD16"]
categories = ["类别A", "类别B", "类别C", "类别D"]
counts = [30, 25, 25, 20]

index = 0
for i, (category, count) in enumerate(zip(categories, counts)):
    for _ in range(count):
        data.append({
            "x": index % 10,
            "y": index // 10,
            "category": category,
        })
        index += 1

chart = (
    Cell()
    .set_data(data=data)
    .set_encode(x_field_name="x", y_field_name="y", color_field="category")
    .set_global_options(
        title_opts=opts.TitleOpts(title="华夫饼图"),
        style_opts=opts.BaseChartStyleOpts(stroke="#fff", inset=2),
        axis_opts=False,
    )
)
chart.render("waffle.html")

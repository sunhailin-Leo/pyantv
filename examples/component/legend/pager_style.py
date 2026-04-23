"""
分页器样式
G2 文档: https://g2.antv.antgroup.com/examples/component/legend/#pager-style
"""
from pyantv import options as opts
from pyantv.charts import Line

data = []
for i in range(1, 13):
    for city in ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "南京"]:
        data.append({"month": f"{i}月", "city": city, "value": 20 + i * 3 + hash(city) % 10})

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="month", y_field_name="value", color_field="city")
    .set_global_options(
        title_opts=opts.TitleOpts(title="分页器样式"),
    )
)
chart.render("pager_style.html")

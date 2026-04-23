"""
股票实时K线
G2 文档: https://g2.antv.antgroup.com/examples/fun/scenario/#realtime-stock
"""
from pyantv import options as opts
from pyantv.charts import Line

import random
random.seed(42)
price = 100
data = []
for i in range(50):
    price += random.uniform(-3, 3)
    data.append({"time": f"10:{i:02d}", "price": round(price, 2)})

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="time", y_field_name="price")
    .set_global_options(
        title_opts=opts.TitleOpts(title="股票实时K线"),
    )
)
chart.render("realtime_stock.html")

"""
缩略轴
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#slider
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [{"day": f"第{i}天", "value": 20 + (i % 7) * 5} for i in range(60)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="day", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="缩略轴"),
        slider_opts=opts.SliderOpts(),
    )
)
chart.render("slider.html")

"""
滚轮缩放
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#wheel-zoom
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [{"day": i, "value": 20 + (i % 10) * 3} for i in range(100)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="day", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="滚轮缩放"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("wheel_zoom.html")

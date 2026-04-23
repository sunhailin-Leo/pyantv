"""
自定义样式
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#custom-style-scrollbar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"name": f"项目{i}", "value": 15 + i * 2} for i in range(25)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义样式"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("custom_style_scrollbar.html")

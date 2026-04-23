"""
滚动条
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#scrollbar
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"name": f"项目{i}", "value": 20 + i * 3} for i in range(30)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="滚动条"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("scrollbar.html")

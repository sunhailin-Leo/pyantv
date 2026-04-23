"""
自适应过滤
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#adaptive-filter
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"name": f"类别{i}", "value": 10 + i * 2} for i in range(40)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自适应过滤"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("adaptive_filter.html")

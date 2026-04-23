"""
Mark 层级自适应
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#mark-level-adaptive
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"name": f"产品{i}", "value": 10 + i * 2} for i in range(35)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="Mark 层级自适应"),
        scrollbar_opts=opts.ScrollBarOpts(),
    )
)
chart.render("mark_level_adaptive.html")

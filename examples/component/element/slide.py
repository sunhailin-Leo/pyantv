"""
滑动
G2 文档: https://g2.antv.antgroup.com/examples/interaction/element/#slide
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [{"name": f"项目{i}", "value": 20 + i * 3} for i in range(20)]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="name", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="滑动"),
        interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
    )
)
chart.render("slide.html")

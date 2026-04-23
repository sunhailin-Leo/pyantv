"""
自定义手柄图标形状
G2 文档: https://g2.antv.antgroup.com/examples/component/scrollbar/#custom-handle-icon
"""
from pyantv import options as opts
from pyantv.charts import Line

data = [{"day": i, "value": 30 + (i % 12) * 4} for i in range(50)]

chart = (
    Line()
    .set_data(data=data)
    .set_encode(x_field_name="day", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="自定义手柄图标形状"),
        slider_opts=opts.SliderOpts(),
    )
)
chart.render("custom_handle_icon.html")

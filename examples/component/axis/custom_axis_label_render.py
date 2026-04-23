"""
坐标轴标签自定义渲染
G2 文档: https://g2.antv.antgroup.com/examples/component/axis/#custom-axis-label-render
"""
from pyantv import options as opts
from pyantv.charts import Interval

data = [
    {"product": "产品A", "value": 120}, {"product": "产品B", "value": 150},
    {"product": "产品C", "value": 130}, {"product": "产品D", "value": 160},
]

chart = (
    Interval()
    .set_data(data=data)
    .set_encode(x_field_name="product", y_field_name="value")
    .set_global_options(
        title_opts=opts.TitleOpts(title="坐标轴标签自定义渲染"),
        axis_opts={
            "x": opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="产品"),
            ),
            "y": opts.AxisCfgOpts(
                axis_title_opts=opts.AxisTitleOpts(title="销量"),
            ),
        },
    )
)
chart.render("custom_axis_label_render.html")

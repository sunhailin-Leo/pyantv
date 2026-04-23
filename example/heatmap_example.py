import unittest

from pyantv import options as opts
from pyantv.charts import View, HeatMap, Point, Image
from pyantv.commons.utils import JsCode

from test import chart_base_test


# heatmap = (
#     HeatMap()
#     .set_data(data={
#         "transform": [
#             opts.CustomDataOpts(
#                 callback=JsCode("(data) => {const dv = new DataSet.View().source(data); dv.transform({type: 'kernel-smooth.density', fields: ['carat', 'price'], as: ['carat', 'price', 'density']}); return dv.rows;}")
#             )
#         ]
#     })
#     .set_encode(
#         x_field_name="carat",
#         y_field_name="price",
#         color_field="density",
#     )
#     .set_heatmap_style(
#         opacity=0.3,
#         gradient=[
#             [0, "white"],
#             [0.2, "blue"],
#             [0.4, "cyan"],
#             [0.6, "lime"],
#             [0.8, "yellow"],
#             [0.9, "red"],
#         ]
#     )
# )
#
# point = (
#     Point()
#     .set_encode(
#         x_field_name="carat",
#         y_field_name="price",
#     )
# )
#
#
# view = (
#     View(
#         render_opts=opts.RenderOpts(
#             is_auto_fit=True,
#         ),
#     )
#     .set_data(data=opts.FetchDataOpts(
#         value="https://assets.antv.antgroup.com/g2/diamond.json",
#     ))
#     .set_view_children(children=[
#         heatmap.get_options(),
#         point.get_options(),
#     ])
#     .set_scale(
#         x_scale_opts=opts.ScaleLinearOpts(
#             is_nice=True, domain_min=-0.5,
#         ),
#         y_scale_opts=opts.ScaleLinearOpts(
#             is_nice=True, domain_min=-2000,
#         ),
#         color_scale_opts=opts.ScaleLinearOpts(
#             is_nice=True,
#         ),
#
#     )
# )
# view.render("heatmap_example.html")

heatmap = (
    HeatMap()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g2/heatmap.json",
        )
    )
    .set_encode(
        x_field_name="g",
        y_field_name="l",
        color_field="tmp",
    )
    .set_global_options(
        tooltip_opts=False,
        style_opts=opts.BaseChartStyleOpts(
            opacity=0,
        ),
    )
)

image = Image().set_global_options(
    tooltip_opts=False,
    style_opts={
        "src": "https://gw.alipayobjects.com/zos/rmsportal/" "NeUTMwKtPcPxIFNTWZOZ.png",
        "x": "50%",
        "y": "50%",
        "width": "100%",
        "height": "100%",
    },
)


view = (
    View(
        render_opts=opts.RenderOpts(
            is_auto_fit=True,
            padding=0,
        ),
    )
    .set_view_children(
        children=[
            image.get_options(),
            heatmap.get_options(),
        ]
    )
    .set_global_options(
        axis_opts=False,
    )
)
view.render("heatmap_example.html")

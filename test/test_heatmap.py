import unittest

from pyantv import options as opts
from pyantv.charts import View, HeatMap, Image
from pyantv.globals import ChartType

from test import chart_base_test


class TestHeatMapChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_heatmap_base(self):
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
                "src": "https://gw.alipayobjects.com/zos/rmsportal/"
                "NeUTMwKtPcPxIFNTWZOZ.png",
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

        return view

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_heatmap_style(self):
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
                    opacity=0.5,
                ),
            )
            .set_heatmap_style(
                min_opacity=0.3,
                max_opacity=0.9,
            )
        )

        image = Image().set_global_options(
            tooltip_opts=False,
            style_opts={
                "src": "https://gw.alipayobjects.com/zos/rmsportal/"
                "NeUTMwKtPcPxIFNTWZOZ.png",
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

        return view

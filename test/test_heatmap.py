"""Heatmap 热力图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import View, HeatMap, Image
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


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

    def test_heatmap_options_validation(self):
        """验证 HeatMap 图表的 JSON 配置结构正确性。"""
        TEST_HEATMAP_DATA = [
            {"g": "A", "l": "1", "tmp": 10},
            {"g": "A", "l": "2", "tmp": 20},
            {"g": "B", "l": "1", "tmp": 30},
            {"g": "B", "l": "2", "tmp": 40},
        ]
        heatmap = (
            HeatMap()
            .set_data(data=TEST_HEATMAP_DATA)
            .set_encode(
                x_field_name="g",
                y_field_name="l",
                color_field="tmp",
            )
        )
        options = heatmap.options
        assert_chart_type(options, "heatmap")
        assert_encode_fields(options, x="g", y="l", color="tmp")
        assert_options_contains(
            options,
            {
                "type": "heatmap",
                "encode": {"x": "g", "y": "l", "color": "tmp"},
                "data": TEST_HEATMAP_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
                "encode.y",
                "encode.color",
            ],
        )

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

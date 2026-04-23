"""Rect 矩形图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import View, Rect, LineX
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


class TestRectChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_rect_base(self):
        rect = (
            Rect()
            .set_encode(
                x_field_name="IMDB Rating",
            )
            .set_scale(y_scale_opts=opts.ScaleLinearOpts(domain_max=1000))
            .set_global_options(
                transform_opts=[
                    opts.TransformBinXOpts(
                        channel_name="y",
                        channel_transform="count",
                        thresholds=9,
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(inset=1),
            )
        )

        line_x = (
            LineX()
            .set_encode(
                x_field_name="IMDB Rating",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupColorOpts(
                        channel_name="y",
                        channel_transform="mean",
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#F4664A",
                    stroke_opacity=1,
                    line_width=5,
                ),
            )
        )

        c = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/movies.json",
                    transform=[
                        opts.FilterDataTransformOpts(
                            callback=JsCode("(d) => d['IMDB Rating'] > 0")
                        )
                    ],
                )
            )
            .set_global_options(
                padding_left=50,
            )
            .set_view_children(
                children=[
                    rect.get_options(),
                    line_x.get_options(),
                ]
            )
        )

        return c

    def test_rect_options_validation(self):
        """验证 Rect 图表的 JSON 配置结构正确性。"""
        TEST_RECT_DATA = [
            {"IMDB Rating": 7.5},
            {"IMDB Rating": 8.0},
            {"IMDB Rating": 6.5},
            {"IMDB Rating": 9.0},
        ]
        rect = (
            Rect()
            .set_data(data=TEST_RECT_DATA)
            .set_encode(
                x_field_name="IMDB Rating",
            )
        )
        options = rect.options
        assert_chart_type(options, "rect")
        assert_encode_fields(options, x="IMDB Rating")
        assert_options_contains(
            options,
            {
                "type": "rect",
                "encode": {"x": "IMDB Rating"},
                "data": TEST_RECT_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
            ],
        )

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_rect_style(self):
        rect = (
            Rect()
            .set_encode(
                x_field_name="IMDB Rating",
            )
            .set_scale(y_scale_opts=opts.ScaleLinearOpts(domain_max=1000))
            .set_global_options(
                transform_opts=[
                    opts.TransformBinXOpts(
                        channel_name="y",
                        channel_transform="count",
                        thresholds=9,
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(inset=1),
            )
            .set_rect_style(
                base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(
                    radius=10,
                ),
            )
        )

        line_x = (
            LineX()
            .set_encode(
                x_field_name="IMDB Rating",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupColorOpts(
                        channel_name="y",
                        channel_transform="mean",
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#F4664A",
                    stroke_opacity=1,
                    line_width=5,
                ),
            )
        )

        c = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/movies.json",
                    transform=[
                        opts.FilterDataTransformOpts(
                            callback=JsCode("(d) => d['IMDB Rating'] > 0")
                        )
                    ],
                )
            )
            .set_global_options(
                padding_left=50,
            )
            .set_view_children(
                children=[
                    rect.get_options(),
                    line_x.get_options(),
                ]
            )
        )

        return c

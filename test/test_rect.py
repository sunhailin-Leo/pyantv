import unittest

from pyantv import options as opts
from pyantv.charts import View, Rect, LineX
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


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
            )
            .set_rect_style(
                base_style_opts=opts.BaseChartStyleOpts(inset=1),
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

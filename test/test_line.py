import unittest

from pyantv import options as opts
from pyantv.charts import View, Line, Point, LineX, LineY, Rect
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test

TEST_LINE_DATA = [
    {"year": "1991", "value": 3},
    {"year": "1992", "value": 4},
    {"year": "1993", "value": 3.5},
    {"year": "1994", "value": 5},
    {"year": "1995", "value": 4.9},
    {"year": "1996", "value": 6},
    {"year": "1997", "value": 7},
    {"year": "1998", "value": 9},
    {"year": "1999", "value": 13},
]


class TestLineChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_line_base(self):
        line = (
            Line()
            .set_global_options(
                label_opts=[
                    opts.LabelOpts(
                        text_opts="value",
                        style_opts=opts.BaseChartStyleOpts(dx=-10, dy=-12),
                    )
                ]
            )
        )

        point = Point().set_global_options(
            tooltip_opts=False,
            style_opts=opts.BaseChartStyleOpts(fill="white"),
        )

        c = (
            View()
            .set_data(data=TEST_LINE_DATA)
            .set_encode(x_field_name="year", y_field_name="value")
            .set_view_children(
                children=[
                    line.options,
                    point.options,
                ]
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(range_=[0, 1]),
                y_scale_opts=opts.ScaleLinearOpts(domain_min=0, is_nice=True),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_line_style(self):
        line = (
            Line()
            .set_line_style(
                is_connect=True,
                connect_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
                is_defined=True,
            )
            .set_global_options(
                label_opts=[
                    opts.LabelOpts(
                        text_opts="value",
                        style_opts=opts.BaseChartStyleOpts(dx=-10, dy=-12),
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#f00",
                ),
            )
        )

        point = Point().set_global_options(
            tooltip_opts=False,
            style_opts=opts.BaseChartStyleOpts(fill="white"),
        )

        c = (
            View()
            .set_data(data=TEST_LINE_DATA)
            .set_encode(x_field_name="year", y_field_name="value")
            .set_view_children(
                children=[
                    line.options,
                    point.options,
                ]
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(range_=[0, 1]),
                y_scale_opts=opts.ScaleLinearOpts(domain_min=0, is_nice=True),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_linex_base(self):
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
            )
            .set_global_options(
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
    def test_liney_base(self):
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

        line_y = (
            LineY()
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
            )
            .set_global_options(
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
                    line_y.get_options(),
                ]
            )
        )

        return c

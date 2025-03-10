import unittest

from pyantv import options as opts
from pyantv.charts import SpaceLayer, Interval
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class TestSpaceLayerChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SPACELAYER)
    def test_space_layer_base(self):
        interval_1 = (
            Interval()
            .set_encode(
                x_field_name="letter",
                y_field_name="frequency",
                color_field="letter",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformSortXOpts(
                        is_reverse=True,
                        by="y",
                    ),
                ],
            )
            .set_scale(
                color_scale_opts={
                    "palette": "cool",
                    "offset": JsCode("(t) => t * 0.8 + 0.1"),
                },
            )
        )

        interval_2 = (
            Interval()
            .set_encode(
                y_field_name="frequency",
                color_field="letter",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformStackYOpts(),
                ],
                coordinate_opts=opts.CoordinateThetaOpts(),
                legend_opts=False,
                width=300,
                height=300,
                x_=300,
                y_=50,
            )
            .set_scale(
                color_scale_opts={
                    "palette": "cool",
                    "offset": JsCode("(t) => t * 0.8 + 0.1"),
                },
            )
        )

        c = (
            SpaceLayer()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/bmw-prod/"
                    "fb9db6b7-23a5-4c23-bbef-c54a55fee580.csv",
                    format_="csv",
                )
            )
            .set_space_layer_children(
                children=[
                    interval_1.get_options(),
                    interval_2.get_options(),
                ]
            )
        )

        return c

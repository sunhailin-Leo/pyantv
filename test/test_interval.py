import unittest

from pyantv import options as opts
from pyantv.charts import Interval, Text, View
from pyantv.globals import ChartType

from test import chart_base_test

TEST_INTERVAL_DATA = [
    {"letter": "A", "frequency": 0.08167},
    {"letter": "B", "frequency": 0.01492},
    {"letter": "C", "frequency": 0.02782},
    {"letter": "D", "frequency": 0.04253},
    {"letter": "E", "frequency": 0.12702},
    {"letter": "F", "frequency": 0.02288},
    {"letter": "G", "frequency": 0.02015},
    {"letter": "H", "frequency": 0.06094},
    {"letter": "I", "frequency": 0.06966},
    {"letter": "J", "frequency": 0.00153},
    {"letter": "K", "frequency": 0.00772},
    {"letter": "L", "frequency": 0.04025},
    {"letter": "M", "frequency": 0.02406},
    {"letter": "N", "frequency": 0.06749},
    {"letter": "O", "frequency": 0.07507},
    {"letter": "P", "frequency": 0.01929},
    {"letter": "Q", "frequency": 0.00095},
    {"letter": "R", "frequency": 0.05987},
    {"letter": "S", "frequency": 0.06327},
    {"letter": "T", "frequency": 0.09056},
    {"letter": "U", "frequency": 0.02758},
    {"letter": "V", "frequency": 0.00978},
    {"letter": "W", "frequency": 0.0236},
    {"letter": "X", "frequency": 0.0015},
    {"letter": "Y", "frequency": 0.01974},
    {"letter": "Z", "frequency": 0.00074},
]


class TestIntervalChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.INTERVAL)
    def test_interval_base(self):
        c = (
            Interval()
            .set_data(data=TEST_INTERVAL_DATA)
            .set_encode(
                x_field_name="letter", y_field_name="frequency", shape_field="pyramid"
            )
            .set_interval_style(min_width=2)
        )

        return c

    @chart_base_test(chart_type=ChartType.INTERVAL)
    def test_interval_style(self):
        c = (
            Interval()
            .set_data(data=TEST_INTERVAL_DATA)
            .set_encode(
                x_field_name="letter", y_field_name="frequency", shape_field="pyramid"
            )
            .set_interval_style(
                min_width=10,
                max_width=20,
                base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(
                    radius=0.1,
                ),
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_interval_and_text(self):
        interval = (
            Interval()
            .set_encode(
                x_field_name="letter",
                y_field_name="frequency",
            )
            .set_global_options(
                axis_opts=opts.AxisOpts(
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_label_opts=opts.AxisLabelOpts(
                            label_formatter=".0%",
                        )
                    )
                )
            )
        )

        text = (
            Text()
            .set_encode(
                x_field_name="letter",
                y_field_name="frequency",
                ext_field={
                    "text": "frequency",
                },
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    fill="black",
                    dy=-5,
                ),
            )
            .set_text_style(
                text_align="center",
            )
        )

        c = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/bmw-prod/"
                    "fb9db6b7-23a5-4c23-bbef-c54a55fee580.csv"
                )
            )
            .set_view_children(
                children=[
                    interval.get_options(),
                    text.get_options(),
                ]
            )
        )

        return c

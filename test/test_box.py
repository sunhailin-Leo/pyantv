import unittest

from pyantv import options as opts
from pyantv.charts import Box
from pyantv.globals import ChartType

from test import chart_base_test

TEST_BOX_DATA = [
    {"x": "Oceania", "y": [1, 9, 16, 22, 24]},
    {"x": "East Europe", "y": [1, 5, 8, 12, 16]},
    {"x": "Australia", "y": [1, 8, 12, 19, 26]},
    {"x": "South America", "y": [2, 8, 12, 21, 28]},
    {"x": "North Africa", "y": [1, 8, 14, 18, 24]},
    {"x": "North America", "y": [3, 10, 17, 28, 30]},
    {"x": "West Europe", "y": [1, 7, 10, 17, 22]},
    {"x": "West Africa", "y": [1, 6, 8, 13, 16]},
]


class TestBoxChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BOX)
    def test_box_base(self):
        c = (
            Box()
            .set_data(data=TEST_BOX_DATA)
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="x",
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(
                    padding_inner=0.6,
                    padding_outer=0.3,
                ),
                y_scale_opts={"zero": True},
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(stroke="black"),
                legend_opts=False,
                tooltip_opts=opts.TooltipOpts(
                    items=[
                        opts.TooltipItemOpts(name="min", channel="y"),
                        opts.TooltipItemOpts(name="q1", channel="y1"),
                        opts.TooltipItemOpts(name="q2", channel="y2"),
                        opts.TooltipItemOpts(name="q3", channel="y3"),
                        opts.TooltipItemOpts(name="max", channel="y4"),
                    ]
                ),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.BOX)
    def test_box_style(self):
        c = (
            Box()
            .set_data(data=TEST_BOX_DATA)
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="x",
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(
                    padding_inner=0.6,
                    padding_outer=0.3,
                ),
                y_scale_opts={"zero": True},
            )
            .set_box_style(
                base_style_opts=opts.BaseChartStyleOpts(stroke="black"),
            )
            .set_global_options(
                legend_opts=False,
                tooltip_opts=opts.TooltipOpts(
                    items=[
                        opts.TooltipItemOpts(name="min", channel="y"),
                        opts.TooltipItemOpts(name="q1", channel="y1"),
                        opts.TooltipItemOpts(name="q2", channel="y2"),
                        opts.TooltipItemOpts(name="q3", channel="y3"),
                        opts.TooltipItemOpts(name="max", channel="y4"),
                    ]
                ),
            )
        )

        return c

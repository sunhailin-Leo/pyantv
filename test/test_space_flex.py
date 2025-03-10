import unittest

from pyantv import options as opts
from pyantv.charts import SpaceFlex, Interval, Cell
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class TestSpaceFlexChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SPACEFLEX)
    def test_space_flex_base(self):
        interval = (
            Interval()
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date).getUTCDate()"),
                y_field_name="temp_max",
                color_field="steelblue",
            )
            .set_global_options(
                padding_bottom=0,
                padding_right=300,
                transform_opts=[
                    opts.TransformGroupXOpts(
                        channel_name="y",
                        channel_transform="max",
                    ),
                ],
                axis_opts=opts.AxisOpts(x_axis_opts=False),
            )
        )

        sub_cell = (
            Cell()
            .set_global_options(
                padding_bottom=60,
                padding_right=0,
                transform_opts=[
                    opts.TransformGroupOpts(
                        channel_name="color",
                        channel_transform="max",
                    )
                ],
                style_opts=opts.BaseChartStyleOpts(inset=0.5),
                axis_opts=opts.AxisOpts(
                    x_axis_opts=opts.AxisCfgOpts(
                        axis_title_opts=opts.AxisTitleOpts(
                            title="Date",
                        ),
                    ),
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_title_opts=opts.AxisTitleOpts(
                            title="Month",
                        ),
                    ),
                ),
                legend_opts=opts.LegendCategoryOpts(
                    color_legend_opts=False,
                ),
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date).getUTCDate()"),
                y_field_name=JsCode("(d) => new Date(d.date).getUTCMonth()"),
                color_field="temp_max",
            )
            .set_scale(color_scale_opts={"palette": "gnBu"})
        )

        sub_interval = (
            Interval()
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date).getUTCMonth()"),
                y_field_name="temp_max",
                color_field="steelblue",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupXOpts(
                        channel_name="y",
                        channel_transform="max",
                    )
                ],
                coordinate_opts=opts.CoordinateTransposeOpts(),
                axis_opts=opts.AxisOpts(x_axis_opts=False),
            )
        )

        sub_space_flex = (
            SpaceFlex()
            .set_global_options(
                padding_bottom=60,
                ratio=[2, 1],
            )
            .set_space_flex_children(
                children=[sub_cell.get_options(), sub_interval.get_options()]
            )
        )

        c = (
            SpaceFlex()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/seattle-weather.json",
                )
            )
            .set_space_flex_children(
                children=[interval.get_options(), sub_space_flex.get_options()]
            )
            .set_global_options(
                ratio=[1, 2],
                direction="col",
                width=900,
            )
        )

        return c

"""Boxplot 箱形图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import BoxPlot
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)

TEST_BOXPLOT_DATA = [
    {"Expt": 1, "Speed": 850},
    {"Expt": 1, "Speed": 740},
    {"Expt": 2, "Speed": 900},
    {"Expt": 2, "Speed": 1070},
]


class TestBoxplotChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BOXPLOT)
    def test_boxplot_base(self):
        c = (
            BoxPlot()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/morley.json"
                )
            )
            .set_encode(
                x_field_name="Expt",
                y_field_name="Speed",
            )
            .set_global_options(inset=6, padding_left="60")
        )

        return c

    @chart_base_test(chart_type=ChartType.BOXPLOT)
    def test_boxplot_style(self):
        c = (
            BoxPlot()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/morley.json"
                )
            )
            .set_encode(
                x_field_name="Expt",
                y_field_name="Speed",
            )
            .set_boxplot_style(
                is_extend=True,
                point_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
                box_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
            )
            .set_global_options(inset=6, padding_left="60")
        )

        return c

    def test_boxplot_options_validation(self):
        """验证 Boxplot 图表的 JSON 配置结构正确性。"""
        boxplot = (
            BoxPlot()
            .set_data(data=TEST_BOXPLOT_DATA)
            .set_encode(
                x_field_name="Expt",
                y_field_name="Speed",
            )
        )
        options = boxplot.options
        assert_chart_type(options, "boxplot")
        assert_encode_fields(options, x="Expt", y="Speed")
        assert_options_contains(
            options,
            {
                "type": "boxplot",
                "encode": {"x": "Expt", "y": "Speed"},
                "data": TEST_BOXPLOT_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
                "encode.y",
            ],
        )

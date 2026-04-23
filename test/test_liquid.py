"""Liquid 水波图基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Liquid
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
)


class TestLiquidChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.LIQUID)
    def test_liquid_base(self):
        c = (
            Liquid(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
            )
            .set_data(data=0.3)
            .set_liquid_style(
                outline_border=4,
                outline_distance=8,
                wave_length=128,
            )
        )

        return c

    def test_liquid_options_validation(self):
        """验证 Liquid 图表的 JSON 配置结构正确性。"""
        liquid = Liquid().set_data(data=0.3)
        options = liquid.options
        assert_chart_type(options, "liquid")
        assert_options_contains(
            options,
            {
                "type": "liquid",
                "data": 0.3,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
            ],
        )

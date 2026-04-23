"""Beeswarm 蜂群图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import Beeswarm
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


TEST_BEESWARM_DATA = [
    {"value": 1, "category": "A"},
    {"value": 2, "category": "A"},
    {"value": 3, "category": "B"},
    {"value": 5, "category": "B"},
    {"value": 8, "category": "C"},
]


class TestBeeswarmChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BEESWARM)
    def test_beeswarm_base(self):
        """验证 Beeswarm 图表基础创建和类型设置。"""
        beeswarm = (
            Beeswarm(
                render_opts=opts.RenderOpts(is_auto_fit=True),
            )
            .set_data(data=TEST_BEESWARM_DATA)
            .set_encode(
                x_field_name="value",
                y_field_name="category",
            )
        )
        return beeswarm

    def test_beeswarm_type(self):
        """验证 Beeswarm 的 chart type 常量正确。"""
        beeswarm = Beeswarm()
        self.assertEqual(beeswarm.options.get("type"), "beeswarm")

    def test_beeswarm_encode(self):
        """验证 Beeswarm 的 encode 配置正确。"""
        beeswarm = (
            Beeswarm()
            .set_data(data=TEST_BEESWARM_DATA)
            .set_encode(
                x_field_name="value",
                y_field_name="category",
                size_field="value",
                color_field="category",
            )
        )
        options = beeswarm.options
        assert_chart_type(options, "beeswarm")
        assert_encode_fields(
            options,
            x="value",
            y="category",
            size="value",
            color="category",
        )

    def test_beeswarm_global_options(self):
        """验证 Beeswarm 支持 set_global_options。"""
        beeswarm = (
            Beeswarm()
            .set_data(data=TEST_BEESWARM_DATA)
            .set_encode(
                x_field_name="value",
                y_field_name="category",
            )
            .set_global_options(
                title_opts=opts.TitleOpts(title="Beeswarm Chart"),
                legend_opts=False,
            )
        )
        options = beeswarm.options
        assert_chart_type(options, "beeswarm")
        self.assertIn("title", options)

    def test_beeswarm_options_validation(self):
        """验证 Beeswarm 图表的 JSON 配置结构正确性。"""
        beeswarm = (
            Beeswarm()
            .set_data(data=TEST_BEESWARM_DATA)
            .set_encode(
                x_field_name="value",
                y_field_name="category",
            )
        )
        options = beeswarm.options
        assert_options_contains(
            options,
            {
                "type": "beeswarm",
                "data": TEST_BEESWARM_DATA,
                "encode": {"x": "value", "y": "category"},
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

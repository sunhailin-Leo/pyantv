"""Point 散点图基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Point
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


class TestPointChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.POINT)
    def test_point_base(self):
        point = (
            Point()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/basement_prod/"
                    "6b4aa721-b039-49b9-99d8-540b3f87d339.json",
                ),
            )
            .set_encode(
                x_field_name="height", y_field_name="weight", color_field="gender"
            )
        )

        return point

    def test_point_options_validation(self):
        """验证 Point 图表的 JSON 配置结构正确性。"""
        point = (
            Point()
            .set_data(
                data=[
                    {"height": 170, "weight": 60, "gender": "male"},
                    {"height": 160, "weight": 50, "gender": "female"},
                ]
            )
            .set_encode(
                x_field_name="height",
                y_field_name="weight",
                color_field="gender",
            )
        )

        options = point.options

        assert_chart_type(options, "point")
        assert_encode_fields(options, x="height", y="weight", color="gender")
        assert_options_contains(
            options,
            {
                "type": "point",
                "encode": {
                    "x": "height",
                    "y": "weight",
                    "color": "gender",
                },
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
                "encode.y",
                "encode.color",
            ],
        )

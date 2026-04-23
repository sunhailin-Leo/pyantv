"""Connector 连接器图基础功能测试。"""

import unittest

from pyantv.charts import Connector
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)

TEST_CONNECTOR_DATA = [
    {"from": "A", "to": "B", "value": 10},
    {"from": "B", "to": "C", "value": 20},
]


class TestConnectorChart(unittest.TestCase):

    def test_connector_base(self):
        """验证 Connector 图表基础创建和类型设置。"""
        connector = Connector()
        self.assertEqual(connector.options.get("type"), "connector")

    def test_connector_options_validation(self):
        """验证 Connector 图表的 JSON 配置结构正确性。"""
        connector = (
            Connector()
            .set_data(data=TEST_CONNECTOR_DATA)
            .set_encode(
                x_field_name="from",
                y_field_name="value",
            )
        )
        options = connector.options
        assert_chart_type(options, "connector")
        assert_encode_fields(options, x="from", y="value")
        assert_options_contains(
            options,
            {
                "type": "connector",
                "data": TEST_CONNECTOR_DATA,
                "encode": {"x": "from", "y": "value"},
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

"""Partition 分区图基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Partition
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
)


TEST_PARTITION_DATA = [
    {
        "name": "root",
        "children": [
            {"name": "A", "value": 10},
            {"name": "B", "value": 20},
            {
                "name": "C",
                "value": 30,
                "children": [
                    {"name": "C1", "value": 15},
                    {"name": "C2", "value": 15},
                ],
            },
        ],
    }
]


class TestPartitionChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.PARTITION)
    def test_partition_base(self):
        """验证 Partition 图表基础创建和类型设置。"""
        partition = (
            Partition(
                render_opts=opts.RenderOpts(is_auto_fit=True),
            )
            .set_data(data=TEST_PARTITION_DATA)
            .set_encode(value_field="value")
        )
        return partition

    def test_partition_type(self):
        """验证 Partition 的 chart type 常量正确。"""
        partition = Partition()
        self.assertEqual(partition.options.get("type"), "partition")

    def test_partition_layout(self):
        """验证 set_partition_layout 设置布局参数。"""
        partition = (
            Partition()
            .set_data(data=TEST_PARTITION_DATA)
            .set_encode(value_field="value")
            .set_partition_layout(fill_parent=True)
        )
        options = partition.options
        assert_chart_type(options, "partition")
        assert_options_contains(
            options,
            {
                "type": "partition",
                "layout": {"fillParent": True, "sort": None},
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "layout.fillParent",
            ],
        )

    def test_partition_layout_chain(self):
        """验证 set_partition_layout 返回 self 支持链式调用。"""
        partition = Partition()
        result = partition.set_partition_layout(fill_parent=False)
        self.assertIs(result, partition)

    def test_partition_style(self):
        """验证 set_partition_style 设置样式。"""
        partition = (
            Partition()
            .set_data(data=TEST_PARTITION_DATA)
            .set_encode(value_field="value")
            .set_partition_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    fill="red",
                    font_size=12,
                ),
            )
        )
        options = partition.options
        assert_chart_type(options, "partition")
        style = options.get("style", {})
        self.assertEqual(style.get("labelFill"), "red")
        self.assertEqual(style.get("labelFontSize"), 12)

    def test_partition_style_chain(self):
        """验证 set_partition_style 返回 self 支持链式调用。"""
        partition = Partition()
        result = partition.set_partition_style()
        self.assertIs(result, partition)

    def test_partition_global_options(self):
        """验证 Partition 支持 set_global_options。"""
        partition = (
            Partition()
            .set_data(data=TEST_PARTITION_DATA)
            .set_encode(value_field="value")
            .set_global_options(
                title_opts=opts.TitleOpts(title="Partition Chart"),
                legend_opts=False,
            )
        )
        options = partition.options
        assert_chart_type(options, "partition")
        self.assertIn("title", options)

    def test_partition_options_validation(self):
        """验证 Partition 图表的 JSON 配置结构正确性。"""
        partition = (
            Partition()
            .set_data(data=TEST_PARTITION_DATA)
            .set_encode(value_field="value")
            .set_partition_layout(fill_parent=True)
        )
        options = partition.options
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.value",
                "layout.fillParent",
            ],
        )

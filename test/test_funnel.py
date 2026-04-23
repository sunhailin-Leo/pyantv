"""Funnel 漏斗图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import Funnel
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


TEST_FUNNEL_DATA = [
    {"action": "浏览网站", "pv": 50000},
    {"action": "放入购物车", "pv": 35000},
    {"action": "生成订单", "pv": 25000},
    {"action": "支付订单", "pv": 15000},
    {"action": "完成交易", "pv": 8000},
]


class TestFunnelChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.INTERVAL)
    def test_funnel_base(self):
        """验证 Funnel 图表基础创建和渲染。"""
        funnel = (
            Funnel(render_opts=opts.RenderOpts(is_auto_fit=True))
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(
                x_field_name="action",
                y_field_name="pv",
                color_field="action",
            )
        )
        return funnel

    def test_funnel_type(self):
        """验证 Funnel 的底层 mark type 为 interval。"""
        funnel = Funnel()
        self.assertEqual(funnel.options.get("type"), "interval")

    def test_funnel_preset_transform(self):
        """验证构造时预置了 symmetryY transform。"""
        funnel = Funnel()
        transform = funnel.options.get("transform")
        self.assertIsNotNone(transform)
        self.assertIsInstance(transform, list)
        self.assertIn({"type": "symmetryY"}, transform)

    def test_funnel_preset_coordinate(self):
        """验证构造时预置了 transpose coordinate。"""
        funnel = Funnel()
        coordinate = funnel.options.get("coordinate")
        self.assertIsNotNone(coordinate)
        self.assertIn("transform", coordinate)
        self.assertIn({"type": "transpose"}, coordinate["transform"])

    def test_funnel_default_shape(self):
        """验证 set_encode 后默认 shape 为 funnel。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(x_field_name="action", y_field_name="pv")
        )
        encode = funnel.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "funnel")

    def test_funnel_explicit_shape_field(self):
        """验证用户显式传入 shape_field 时不被覆盖。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(
                x_field_name="action",
                y_field_name="pv",
                shape_field="pyramid",
            )
        )
        encode = funnel.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "pyramid")

    def test_funnel_set_funnel_shape_pyramid(self):
        """验证 set_funnel_shape 切换为 pyramid。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(x_field_name="action", y_field_name="pv")
            .set_funnel_shape("pyramid")
        )
        encode = funnel.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "pyramid")

    def test_funnel_set_funnel_shape_chain(self):
        """验证 set_funnel_shape 返回 self 支持链式调用。"""
        funnel = Funnel()
        result = funnel.set_funnel_shape("funnel")
        self.assertIs(result, funnel)

    def test_funnel_set_funnel_shape_before_encode(self):
        """验证先调用 set_funnel_shape 再调用 set_encode 时 shape 正确。"""
        funnel = (
            Funnel()
            .set_funnel_shape("pyramid")
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(x_field_name="action", y_field_name="pv")
        )
        encode = funnel.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "pyramid")

    def test_funnel_global_options(self):
        """验证 Funnel 支持 set_global_options。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(x_field_name="action", y_field_name="pv")
            .set_global_options(
                title_opts=opts.TitleOpts(title="Funnel Chart"),
                legend_opts=False,
            )
        )
        options = funnel.options
        self.assertEqual(options.get("type"), "interval")
        self.assertIn("title", options)

    def test_funnel_encode_color(self):
        """验证 set_encode 支持 color_field。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(
                x_field_name="action",
                y_field_name="pv",
                color_field="action",
            )
        )
        encode = funnel.options.get("encode", {})
        self.assertEqual(encode.get("color"), "action")
        self.assertEqual(encode.get("shape"), "funnel")

    def test_funnel_options_validation(self):
        """验证 Funnel 图表的 JSON 配置结构正确性。"""
        funnel = (
            Funnel()
            .set_data(data=TEST_FUNNEL_DATA)
            .set_encode(x_field_name="action", y_field_name="pv")
        )
        options = funnel.options
        assert_chart_type(options, "interval")
        assert_encode_fields(options, x="action", y="pv", shape="funnel")
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
                "encode.y",
                "encode.shape",
                "transform",
                "coordinate",
            ],
        )

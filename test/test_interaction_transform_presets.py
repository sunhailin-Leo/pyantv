"""交互与数据转换预设函数测试。"""

import unittest

from pyantv.charts import Line, Interval, Point
from pyantv.presets import (
    with_element_highlight,
    with_element_select,
    with_brush_highlight,
    with_brush_filter,
    with_fisheye,
    with_slider_filter,
    with_sort_by,
    with_stack,
    with_normalize,
    with_group,
    with_jitter,
)


class TestElementHighlight(unittest.TestCase):
    """验证元素高亮交互预设。"""

    def test_applies_interaction(self):
        """验证交互配置被设置。"""
        chart = Line()
        result = with_element_highlight(chart)
        self.assertIs(result, chart)
        interaction = chart.options.get("interaction")
        self.assertIsNotNone(interaction)
        self.assertIn("elementHighlight", interaction)

    def test_background_option(self):
        """验证背景选项。"""
        chart = Line()
        with_element_highlight(chart, background=True)
        interaction = chart.options.get("interaction")
        self.assertTrue(interaction["elementHighlight"]["background"])

    def test_default_no_background(self):
        """验证默认不显示背景。"""
        chart = Line()
        with_element_highlight(chart)
        interaction = chart.options.get("interaction")
        self.assertFalse(interaction["elementHighlight"]["background"])


class TestElementSelect(unittest.TestCase):
    """验证元素选中交互预设。"""

    def test_applies_interaction(self):
        """验证交互配置被设置。"""
        chart = Interval()
        result = with_element_select(chart)
        self.assertIs(result, chart)
        interaction = chart.options.get("interaction")
        self.assertIn("elementSelect", interaction)

    def test_background_option(self):
        """验证背景选项。"""
        chart = Interval()
        with_element_select(chart, background=True)
        interaction = chart.options.get("interaction")
        self.assertTrue(interaction["elementSelect"]["background"])


class TestBrushHighlight(unittest.TestCase):
    """验证框选高亮交互预设。"""

    def test_applies_interaction(self):
        """验证交互配置被设置。"""
        chart = Point()
        result = with_brush_highlight(chart)
        self.assertIs(result, chart)
        interaction = chart.options.get("interaction")
        self.assertIn("brushHighlight", interaction)
        self.assertTrue(interaction["brushHighlight"])


class TestBrushFilter(unittest.TestCase):
    """验证框选过滤交互预设。"""

    def test_applies_interaction(self):
        """验证交互配置被设置。"""
        chart = Point()
        result = with_brush_filter(chart)
        self.assertIs(result, chart)
        interaction = chart.options.get("interaction")
        self.assertIn("brushFilter", interaction)
        self.assertTrue(interaction["brushFilter"])


class TestFisheye(unittest.TestCase):
    """验证鱼眼放大镜交互预设。"""

    def test_applies_interaction(self):
        """验证交互配置被设置。"""
        chart = Point()
        result = with_fisheye(chart)
        self.assertIs(result, chart)
        interaction = chart.options.get("interaction")
        self.assertIn("fisheye", interaction)
        self.assertTrue(interaction["fisheye"])


class TestSliderFilter(unittest.TestCase):
    """验证滑块过滤交互预设。"""

    def test_x_axis_slider(self):
        """验证 x 轴滑块。"""
        chart = Line()
        result = with_slider_filter(chart, x_axis=True, y_axis=False)
        self.assertIs(result, chart)
        slider = chart.options.get("slider")
        self.assertIn("x", slider)

    def test_both_axis_slider(self):
        """验证双轴滑块。"""
        chart = Line()
        with_slider_filter(chart, x_axis=True, y_axis=True)
        slider = chart.options.get("slider")
        self.assertIn("x", slider)
        self.assertIn("y", slider)

    def test_y_axis_only(self):
        """验证仅 y 轴滑块。"""
        chart = Line()
        with_slider_filter(chart, x_axis=False, y_axis=True)
        slider = chart.options.get("slider")
        self.assertNotIn("x", slider)
        self.assertIn("y", slider)


class TestSortBy(unittest.TestCase):
    """验证排序数据转换预设。"""

    def test_ascending_sort(self):
        """验证升序排序。"""
        chart = Interval()
        result = with_sort_by(chart, field="value", order="ascending")
        self.assertIs(result, chart)
        transform = chart.options.get("transform")
        self.assertIsNotNone(transform)
        self.assertEqual(transform["type"], "sortX")
        self.assertFalse(transform["reverse"])

    def test_descending_sort(self):
        """验证降序排序。"""
        chart = Interval()
        with_sort_by(chart, field="value", order="descending")
        transform = chart.options.get("transform")
        self.assertTrue(transform["reverse"])


class TestStack(unittest.TestCase):
    """验证堆叠数据转换预设。"""

    def test_applies_stack(self):
        """验证堆叠转换。"""
        chart = Interval()
        result = with_stack(chart)
        self.assertIs(result, chart)
        transform = chart.options.get("transform")
        self.assertEqual(transform["type"], "stackY")


class TestNormalize(unittest.TestCase):
    """验证归一化数据转换预设。"""

    def test_applies_normalize(self):
        """验证归一化转换（stackY + normalizeY）。"""
        chart = Interval()
        result = with_normalize(chart)
        self.assertIs(result, chart)
        transform = chart.options.get("transform")
        self.assertIsInstance(transform, list)
        self.assertEqual(len(transform), 2)
        self.assertEqual(transform[0]["type"], "stackY")
        self.assertEqual(transform[1]["type"], "normalizeY")


class TestGroup(unittest.TestCase):
    """验证分组数据转换预设。"""

    def test_applies_group(self):
        """验证分组转换。"""
        chart = Interval()
        result = with_group(chart)
        self.assertIs(result, chart)
        transform = chart.options.get("transform")
        self.assertEqual(transform["type"], "dodgeX")


class TestJitter(unittest.TestCase):
    """验证抖动数据转换预设。"""

    def test_applies_jitter(self):
        """验证抖动转换。"""
        chart = Point()
        result = with_jitter(chart)
        self.assertIs(result, chart)
        transform = chart.options.get("transform")
        self.assertEqual(transform["type"], "jitterX")


class TestInteractionChaining(unittest.TestCase):
    """验证交互预设与其他功能的链式调用。"""

    def test_highlight_with_data(self):
        """验证交互预设与数据设置组合。"""
        chart = Line.from_data(
            data=[{"x": "A", "y": 1}, {"x": "B", "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        with_element_highlight(chart)
        self.assertEqual(chart.options.get("type"), "line")
        self.assertIn(
            "elementHighlight",
            chart.options.get("interaction", {}),
        )

    def test_transform_with_data(self):
        """验证转换预设与数据设置组合。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"x": "A", "y": 1, "g": "G1"},
                    {"x": "B", "y": 2, "g": "G2"},
                ]
            )
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="g",
            )
        )
        with_stack(chart)
        self.assertEqual(
            chart.options.get("transform", {}).get("type"),
            "stackY",
        )

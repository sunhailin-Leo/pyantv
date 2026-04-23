"""预设系统核心函数测试。"""

import unittest

from pyantv.charts import Line, Interval
from pyantv.presets import (
    with_dark_theme,
    with_classic_theme,
    with_academy_theme,
    with_smooth_animation,
    with_tooltip,
    with_auto_fit,
    with_legend_hidden,
    with_axis_hidden,
    with_labels,
    with_padding,
    with_transpose,
    with_polar,
)


class TestThemePresets(unittest.TestCase):
    """验证主题预设函数。"""

    def test_with_dark_theme(self):
        """验证暗色主题预设。"""
        chart = Line()
        result = with_dark_theme(chart)
        self.assertIs(result, chart)
        self.assertEqual(chart.render_options.get("theme"), "dark")

    def test_with_classic_theme(self):
        """验证经典主题预设。"""
        chart = Line()
        with_classic_theme(chart)
        self.assertEqual(chart.render_options.get("theme"), "classic")

    def test_with_academy_theme(self):
        """验证学术主题预设。"""
        chart = Line()
        with_academy_theme(chart)
        self.assertEqual(chart.render_options.get("theme"), "academy")


class TestAnimationPresets(unittest.TestCase):
    """验证动画预设函数。"""

    def test_with_smooth_animation(self):
        """验证平滑动画预设。"""
        chart = Line()
        result = with_smooth_animation(chart)
        self.assertIs(result, chart)
        animate = chart.options.get("animate", {})
        self.assertIsNotNone(animate)

    def test_with_smooth_animation_custom_duration(self):
        """验证自定义动画时长。"""
        chart = Line()
        with_smooth_animation(chart, duration=2000, easing="ease-out-cubic")
        animate = chart.options.get("animate", {})
        self.assertIsNotNone(animate)


class TestTooltipPresets(unittest.TestCase):
    """验证 tooltip 预设函数。"""

    def test_with_tooltip_shared(self):
        """验证共享 tooltip 预设。"""
        chart = Line()
        result = with_tooltip(chart, shared=True)
        self.assertIs(result, chart)
        tooltip = chart.options.get("tooltip", {})
        self.assertIsNotNone(tooltip)

    def test_with_tooltip_crosshairs(self):
        """验证十字准线 tooltip 预设。"""
        chart = Line()
        with_tooltip(chart, show_crosshairs=True)
        tooltip = chart.options.get("tooltip", {})
        self.assertIsNotNone(tooltip)


class TestLayoutPresets(unittest.TestCase):
    """验证布局预设函数。"""

    def test_with_auto_fit(self):
        """验证自适应预设。"""
        chart = Line()
        result = with_auto_fit(chart)
        self.assertIs(result, chart)
        self.assertIn("autoFit", chart.options)

    def test_with_legend_hidden(self):
        """验证隐藏图例预设。"""
        chart = Line()
        result = with_legend_hidden(chart)
        self.assertIs(result, chart)
        self.assertFalse(chart.options.get("legend"))

    def test_with_axis_hidden(self):
        """验证隐藏坐标轴预设。"""
        chart = Line()
        result = with_axis_hidden(chart)
        self.assertIs(result, chart)
        self.assertFalse(chart.options.get("axis"))

    def test_with_labels(self):
        """验证数据标签预设。"""
        chart = Interval()
        result = with_labels(chart, font_size=14, position="top")
        self.assertIs(result, chart)
        self.assertIn("labels", chart.options)

    def test_with_padding(self):
        """验证内边距预设。"""
        chart = Line()
        result = with_padding(chart, top=30, right=30, bottom=30, left=30)
        self.assertIs(result, chart)
        self.assertEqual(chart.options.get("paddingTop"), 30)
        self.assertEqual(chart.options.get("paddingRight"), 30)
        self.assertEqual(chart.options.get("paddingBottom"), 30)
        self.assertEqual(chart.options.get("paddingLeft"), 30)


class TestCoordinatePresets(unittest.TestCase):
    """验证坐标系预设函数。"""

    def test_with_transpose(self):
        """验证转置坐标系预设。"""
        chart = Interval()
        result = with_transpose(chart)
        self.assertIs(result, chart)
        coordinate = chart.options.get("coordinate", {})
        self.assertIsNotNone(coordinate)

    def test_with_polar(self):
        """验证极坐标系预设。"""
        chart = Interval()
        result = with_polar(chart)
        self.assertIs(result, chart)
        coordinate = chart.options.get("coordinate", {})
        self.assertIsNotNone(coordinate)


class TestPresetsChaining(unittest.TestCase):
    """验证预设函数支持链式组合。"""

    def test_multiple_presets(self):
        """验证多个预设函数组合使用。"""
        chart = Line.from_data(
            data=[{"x": 1, "y": 2}],
            x_field_name="x",
            y_field_name="y",
        )
        with_dark_theme(chart)
        with_auto_fit(chart)
        with_legend_hidden(chart)
        with_padding(chart, top=10, right=10, bottom=10, left=10)

        self.assertEqual(chart.render_options.get("theme"), "dark")
        self.assertIn("autoFit", chart.options)
        self.assertIn("legend", chart.options)
        self.assertIn("paddingTop", chart.options)

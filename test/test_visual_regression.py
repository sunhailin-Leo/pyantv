"""视觉回归测试。

使用 Playwright 截图 + Pillow 像素对比，验证渲染效果与基准图片一致。

运行前需要安装：
    pip install playwright Pillow
    playwright install chromium

首次运行需要先生成基准图片：
    UPDATE_BASELINES=1 pytest test/test_visual_regression.py -m slow

正常测试模式（对比基准图片）：
    pytest test/test_visual_regression.py -m slow
"""

import unittest

import pytest

from pyantv.charts import Line, Interval, Point, Area
from pyantv.globals import ThemeType
from pyantv.options import (
    CoordinateThetaOpts,
    TitleOpts,
    TransformStackYOpts,
)

try:
    from test.visual_helpers import assert_visual_match

    VISUAL_DEPS_AVAILABLE = True
except ImportError:
    VISUAL_DEPS_AVAILABLE = False


@pytest.mark.slow
@unittest.skipUnless(VISUAL_DEPS_AVAILABLE, "playwright or Pillow not installed")
class TestVisualRegression(unittest.TestCase):
    """视觉回归测试类。"""

    def test_visual_line_basic(self):
        """Line 基础折线图视觉回归。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                    {"year": "2022", "value": 150},
                    {"year": "2023", "value": 280},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        assert_visual_match(chart, "visual_line_basic")

    def test_visual_interval_basic(self):
        """Interval 基础柱状图视觉回归。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "value": 30},
                    {"category": "B", "value": 70},
                    {"category": "C", "value": 50},
                    {"category": "D", "value": 90},
                ]
            )
            .set_encode(x_field_name="category", y_field_name="value")
        )
        assert_visual_match(chart, "visual_interval_basic")

    def test_visual_point_basic(self):
        """Point 基础散点图视觉回归。"""
        chart = (
            Point()
            .set_data(
                data=[
                    {"x": 1, "y": 2},
                    {"x": 3, "y": 5},
                    {"x": 5, "y": 3},
                    {"x": 7, "y": 8},
                    {"x": 9, "y": 6},
                ]
            )
            .set_encode(x_field_name="x", y_field_name="y")
        )
        assert_visual_match(chart, "visual_point_basic")

    def test_visual_area_basic(self):
        """Area 基础面积图视觉回归。"""
        chart = (
            Area()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                    {"year": "2022", "value": 150},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        assert_visual_match(chart, "visual_area_basic")

    def test_visual_pie_chart(self):
        """饼图视觉回归。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "Category A", "count": 40},
                    {"item": "Category B", "count": 30},
                    {"item": "Category C", "count": 20},
                    {"item": "Category D", "count": 10},
                ]
            )
            .set_encode(y_field_name="count", color_field="item")
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts())
        )
        assert_visual_match(chart, "visual_pie_chart")

    def test_visual_stacked_bar(self):
        """堆叠柱状图视觉回归。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "type": "X", "value": 30},
                    {"category": "A", "type": "Y", "value": 20},
                    {"category": "B", "type": "X", "value": 50},
                    {"category": "B", "type": "Y", "value": 40},
                    {"category": "C", "type": "X", "value": 35},
                    {"category": "C", "type": "Y", "value": 25},
                ]
            )
            .set_encode(
                x_field_name="category",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
        )
        assert_visual_match(chart, "visual_stacked_bar")

    def test_visual_with_title(self):
        """带标题的图表视觉回归。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"x": "Jan", "y": 100},
                    {"x": "Feb", "y": 200},
                    {"x": "Mar", "y": 150},
                ]
            )
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(
                title_opts=TitleOpts(
                    title="Monthly Revenue",
                    subtitle="Q1 2024",
                )
            )
        )
        assert_visual_match(chart, "visual_with_title")

    def test_visual_dark_theme(self):
        """暗色主题图表视觉回归。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"x": "2020", "y": 100},
                    {"x": "2021", "y": 200},
                    {"x": "2022", "y": 150},
                ]
            )
            .set_encode(x_field_name="x", y_field_name="y")
            .set_theme(theme=ThemeType.DARK)
        )
        assert_visual_match(chart, "visual_dark_theme")

    def test_visual_donut_chart(self):
        """环形图视觉回归。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "A", "count": 40},
                    {"item": "B", "count": 30},
                    {"item": "C", "count": 20},
                ]
            )
            .set_encode(y_field_name="count", color_field="item")
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts(inner_radius=0.5))
        )
        assert_visual_match(chart, "visual_donut_chart")

    def test_visual_multi_series_line(self):
        """多系列折线图视觉回归。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"year": "2020", "category": "A", "value": 100},
                    {"year": "2020", "category": "B", "value": 80},
                    {"year": "2021", "category": "A", "value": 200},
                    {"year": "2021", "category": "B", "value": 150},
                    {"year": "2022", "category": "A", "value": 180},
                    {"year": "2022", "category": "B", "value": 220},
                ]
            )
            .set_encode(
                x_field_name="year",
                y_field_name="value",
                color_field="category",
            )
        )
        assert_visual_match(chart, "visual_multi_series_line")

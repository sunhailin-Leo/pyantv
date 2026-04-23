"""HTML 渲染 + DOM 结构验证测试。

使用 Playwright 验证 pyantv 渲染的 HTML 能被 G2 正确解析和渲染。

运行前需要安装：
    pip install playwright
    playwright install chromium

标记为 slow 测试，可通过 -m "not slow" 跳过：
    pytest test/ -m "not slow"
"""

import unittest

import pytest

from pyantv.charts import Line, Interval, Point, Area
from pyantv.options import (
    CoordinateThetaOpts,
    TitleOpts,
    TransformStackYOpts,
)

try:
    from test.render_helpers import validate_render

    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False


def _build_html(chart) -> str:
    """构建完整 HTML 字符串。"""
    return chart.render_embed()


@pytest.mark.slow
@unittest.skipUnless(PLAYWRIGHT_AVAILABLE, "playwright not installed")
class TestRenderValidation(unittest.TestCase):
    """HTML 渲染 + DOM 结构验证测试。"""

    def test_line_renders_canvas(self):
        """Line 图表渲染后应产生 canvas 元素。"""
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
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists, "Canvas should exist after render")
        self.assertGreater(result.canvas_width, 0, "Canvas width should be > 0")
        self.assertGreater(result.canvas_height, 0, "Canvas height should be > 0")

    def test_interval_renders_canvas(self):
        """Interval 柱状图渲染后应产生 canvas 元素。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "value": 30},
                    {"category": "B", "value": 70},
                    {"category": "C", "value": 50},
                ]
            )
            .set_encode(x_field_name="category", y_field_name="value")
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)
        self.assertTrue(result.container_exists, "Chart container div should exist")

    def test_point_renders_canvas(self):
        """Point 散点图渲染后应产生 canvas 元素。"""
        chart = (
            Point()
            .set_data(
                data=[
                    {"x": 1, "y": 2},
                    {"x": 3, "y": 4},
                    {"x": 5, "y": 6},
                ]
            )
            .set_encode(x_field_name="x", y_field_name="y")
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)

    def test_area_renders_canvas(self):
        """Area 面积图渲染后应产生 canvas 元素。"""
        chart = (
            Area()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)

    def test_pie_chart_renders_canvas(self):
        """饼图（Interval + stackY + theta）渲染后应产生 canvas 元素。"""
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
            .set_coordinate(coordinate_opts=CoordinateThetaOpts())
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)

    def test_no_js_errors(self):
        """渲染过程中不应产生 JS 控制台错误。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 3, "y": 4}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        html = _build_html(chart)
        result = validate_render(html)

        self.assertEqual(
            len(result.js_exceptions),
            0,
            f"JS exceptions found: {result.js_exceptions}",
        )

    def test_chart_instance_in_script(self):
        """渲染的 HTML 中应包含 G2.Chart 实例化代码。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(
            result.chart_instance_exists,
            "HTML should contain 'new G2.Chart' instantiation",
        )

    def test_container_div_exists(self):
        """渲染的 HTML 中应包含图表容器 div。"""
        chart = (
            Interval()
            .set_data(data=[{"x": "A", "y": 10}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(
            result.container_exists,
            f"Container div with id='{chart.chart_id}' should exist",
        )

    def test_chart_with_title_renders(self):
        """带 Title 的图表渲染后应正常产生 canvas。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 3, "y": 4}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(title_opts=TitleOpts(title="Test Chart", align="center"))
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)
        self.assertEqual(len(result.js_exceptions), 0)

    def test_full_pipeline_renders(self):
        """完整配置管线的图表渲染后应正常产生 canvas。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"month": "Jan", "type": "Sales", "value": 100},
                    {"month": "Jan", "type": "Profit", "value": 40},
                    {"month": "Feb", "type": "Sales", "value": 150},
                    {"month": "Feb", "type": "Profit", "value": 60},
                ]
            )
            .set_encode(
                x_field_name="month",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_global_options(
                title_opts=TitleOpts(title="Monthly Report"),
            )
            .set_legend(legend_opts=False)
            .set_tooltip(tooltip_opts=False)
        )
        html = _build_html(chart)
        result = validate_render(html, chart_id=chart.chart_id)

        self.assertTrue(result.canvas_exists)
        self.assertTrue(result.container_exists)
        self.assertEqual(len(result.js_exceptions), 0)

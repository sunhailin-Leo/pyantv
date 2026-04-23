"""预设系统扩展功能及批量导出测试。"""

import os
import unittest

from pyantv.charts import Line, Interval
from pyantv.presets import (
    with_tech_theme,
    with_business_theme,
    with_fresh_theme,
    format_number,
    format_percent,
    format_currency,
    format_date,
    batch_export_png,
    _TECH_THEME,
    _BUSINESS_THEME,
    _FRESH_THEME,
)
from pyantv.commons.utils import JsCode


class TestCustomThemes(unittest.TestCase):
    """验证自定义主题预设。"""

    def test_tech_theme_applies(self):
        """验证科技风主题应用。"""
        chart = Line()
        result = with_tech_theme(chart)
        self.assertIs(result, chart)
        self.assertEqual(chart.render_options.get("theme"), _TECH_THEME)

    def test_business_theme_applies(self):
        """验证商务风主题应用。"""
        chart = Line()
        result = with_business_theme(chart)
        self.assertIs(result, chart)
        self.assertEqual(chart.render_options.get("theme"), _BUSINESS_THEME)

    def test_fresh_theme_applies(self):
        """验证清新风主题应用。"""
        chart = Line()
        result = with_fresh_theme(chart)
        self.assertIs(result, chart)
        self.assertEqual(chart.render_options.get("theme"), _FRESH_THEME)

    def test_tech_theme_has_colors(self):
        """验证科技风主题包含颜色配置。"""
        self.assertIn("color", _TECH_THEME)
        self.assertEqual(len(_TECH_THEME["color"]), 6)

    def test_business_theme_has_colors(self):
        """验证商务风主题包含颜色配置。"""
        self.assertIn("color", _BUSINESS_THEME)
        self.assertEqual(len(_BUSINESS_THEME["color"]), 6)

    def test_fresh_theme_has_colors(self):
        """验证清新风主题包含颜色配置。"""
        self.assertIn("color", _FRESH_THEME)
        self.assertEqual(len(_FRESH_THEME["color"]), 6)

    def test_tech_theme_dark_background(self):
        """验证科技风主题使用深色背景。"""
        view_fill = _TECH_THEME.get("view", {}).get("viewFill", "")
        self.assertTrue(view_fill.startswith("#0"))

    def test_business_theme_white_background(self):
        """验证商务风主题使用白色背景。"""
        view_fill = _BUSINESS_THEME.get("view", {}).get("viewFill", "")
        self.assertEqual(view_fill, "#ffffff")


class TestFormatNumber(unittest.TestCase):
    """验证数值格式化预设。"""

    def test_returns_jscode(self):
        """验证返回 JsCode 对象。"""
        result = format_number()
        self.assertIsInstance(result, JsCode)

    def test_default_precision(self):
        """验证默认精度为 0。"""
        result = format_number()
        self.assertIn("minimumFractionDigits: 0", result.js_code)

    def test_custom_precision(self):
        """验证自定义精度。"""
        result = format_number(precision=2)
        self.assertIn("minimumFractionDigits: 2", result.js_code)
        self.assertIn("maximumFractionDigits: 2", result.js_code)

    def test_contains_locale_string(self):
        """验证使用 toLocaleString。"""
        result = format_number()
        self.assertIn("toLocaleString", result.js_code)


class TestFormatPercent(unittest.TestCase):
    """验证百分比格式化预设。"""

    def test_returns_jscode(self):
        """验证返回 JsCode 对象。"""
        result = format_percent()
        self.assertIsInstance(result, JsCode)

    def test_default_precision(self):
        """验证默认精度为 1。"""
        result = format_percent()
        self.assertIn("toFixed(1)", result.js_code)

    def test_custom_precision(self):
        """验证自定义精度。"""
        result = format_percent(precision=0)
        self.assertIn("toFixed(0)", result.js_code)

    def test_contains_percent_sign(self):
        """验证包含百分号。"""
        result = format_percent()
        self.assertIn("%", result.js_code)

    def test_multiplies_by_100(self):
        """验证乘以 100。"""
        result = format_percent()
        self.assertIn("* 100", result.js_code)


class TestFormatCurrency(unittest.TestCase):
    """验证货币格式化预设。"""

    def test_returns_jscode(self):
        """验证返回 JsCode 对象。"""
        result = format_currency()
        self.assertIsInstance(result, JsCode)

    def test_default_symbol(self):
        """验证默认货币符号为 $。"""
        result = format_currency()
        self.assertIn("$", result.js_code)

    def test_custom_symbol(self):
        """验证自定义货币符号。"""
        result = format_currency(symbol="¥")
        self.assertIn("¥", result.js_code)

    def test_default_precision(self):
        """验证默认精度为 2。"""
        result = format_currency()
        self.assertIn("minimumFractionDigits: 2", result.js_code)


class TestFormatDate(unittest.TestCase):
    """验证日期格式化预设。"""

    def test_returns_jscode(self):
        """验证返回 JsCode 对象。"""
        result = format_date()
        self.assertIsInstance(result, JsCode)

    def test_default_pattern(self):
        """验证默认日期格式。"""
        result = format_date()
        self.assertIn("YYYY-MM-DD", result.js_code)

    def test_custom_pattern(self):
        """验证自定义日期格式。"""
        result = format_date("YYYY/MM/DD HH:mm")
        self.assertIn("YYYY/MM/DD HH:mm", result.js_code)

    def test_contains_date_parsing(self):
        """验证包含日期解析逻辑。"""
        result = format_date()
        self.assertIn("new Date(d)", result.js_code)
        self.assertIn("getFullYear", result.js_code)
        self.assertIn("getMonth", result.js_code)

    def test_contains_replace_calls(self):
        """验证包含替换调用。"""
        result = format_date()
        self.assertIn(".replace('YYYY',Y)", result.js_code)
        self.assertIn(".replace('MM',M)", result.js_code)
        self.assertIn(".replace('DD',D)", result.js_code)


class TestBatchExportPng(unittest.TestCase):
    """验证批量导出工具函数（不实际调用 Playwright）。"""

    def test_function_exists(self):
        """验证 batch_export_png 函数存在。"""
        self.assertTrue(callable(batch_export_png))

    def test_importable_from_presets(self):
        """验证可从 presets 模块导入。"""
        from pyantv.presets import batch_export_png as func

        self.assertTrue(callable(func))


class TestThemeChaining(unittest.TestCase):
    """验证主题预设与其他功能的链式调用。"""

    def test_tech_theme_with_data(self):
        """验证科技风主题与数据设置组合。"""
        chart = Line.from_data(
            data=[{"x": "A", "y": 1}],
            x_field_name="x",
            y_field_name="y",
        )
        with_tech_theme(chart)
        self.assertEqual(chart.render_options.get("theme"), _TECH_THEME)
        self.assertEqual(chart.options.get("type"), "line")

    def test_formatter_with_labels(self):
        """验证格式化函数可用于标签配置。"""
        from pyantv import options as opts

        formatter = format_number(precision=1)
        chart = Interval().set_labels(label_opts=opts.LabelOpts(formatter=formatter))
        self.assertIn("labels", chart.options)


class TestBatchExportPngMocked(unittest.TestCase):
    """验证 batch_export_png 函数逻辑（mock export_png）。"""

    def test_tuple_input(self):
        """验证 tuple 输入格式 (chart, filename)。"""
        from unittest.mock import patch
        import tempfile

        chart1 = Line()
        chart2 = Interval()

        with patch("pyantv.render.export.export_png") as mock_export:
            with tempfile.TemporaryDirectory() as tmpdir:
                batch_export_png(
                    [(chart1, "line.png"), (chart2, "bar.png")],
                    output_dir=tmpdir,
                    width=800,
                    height=600,
                )
                self.assertEqual(mock_export.call_count, 2)
                first_call = mock_export.call_args_list[0]
                self.assertIs(first_call[0][0], chart1)
                self.assertEqual(
                    first_call[0][1],
                    os.path.join(tmpdir, "line.png"),
                )
                second_call = mock_export.call_args_list[1]
                self.assertIs(second_call[0][0], chart2)
                self.assertEqual(
                    second_call[0][1],
                    os.path.join(tmpdir, "bar.png"),
                )

    def test_non_tuple_input(self):
        """验证直接传入 chart 对象（自动命名）。"""
        from unittest.mock import patch
        import tempfile
        import os

        chart1 = Line()
        chart2 = Interval()

        with patch("pyantv.render.export.export_png") as mock_export:
            with tempfile.TemporaryDirectory() as tmpdir:
                batch_export_png(
                    [chart1, chart2],
                    output_dir=tmpdir,
                )
                self.assertEqual(mock_export.call_count, 2)
                first_call = mock_export.call_args_list[0]
                self.assertEqual(
                    first_call[0][1],
                    os.path.join(tmpdir, "chart_0.png"),
                )
                second_call = mock_export.call_args_list[1]
                self.assertEqual(
                    second_call[0][1],
                    os.path.join(tmpdir, "chart_1.png"),
                )

    def test_mixed_input(self):
        """验证混合输入（tuple + 非 tuple）。"""
        from unittest.mock import patch
        import tempfile

        chart1 = Line()
        chart2 = Interval()

        with patch("pyantv.render.export.export_png") as mock_export:
            with tempfile.TemporaryDirectory() as tmpdir:
                batch_export_png(
                    [(chart1, "named.png"), chart2],
                    output_dir=tmpdir,
                )
                self.assertEqual(mock_export.call_count, 2)
                first_path = mock_export.call_args_list[0][0][1]
                second_path = mock_export.call_args_list[1][0][1]
                self.assertTrue(first_path.endswith("named.png"))
                self.assertTrue(second_path.endswith("chart_1.png"))

    def test_creates_output_dir(self):
        """验证自动创建输出目录。"""
        from unittest.mock import patch
        import tempfile
        import os

        chart = Line()
        with patch("pyantv.render.export.export_png"):
            with tempfile.TemporaryDirectory() as tmpdir:
                nested_dir = os.path.join(tmpdir, "sub", "dir")
                batch_export_png(
                    [chart],
                    output_dir=nested_dir,
                )
                self.assertTrue(os.path.isdir(nested_dir))

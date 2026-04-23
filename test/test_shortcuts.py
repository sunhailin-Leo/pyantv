"""快捷方法（set_title、set_padding、set_size）测试。"""

import unittest

from pyantv.charts import Line, Interval


class TestTopLevelExports(unittest.TestCase):
    """验证顶层导出优化。"""

    def test_import_chart_event(self):
        """验证 ChartEvent 可从顶层导入。"""
        from pyantv import ChartEvent

        self.assertTrue(hasattr(ChartEvent, "CLICK"))
        self.assertTrue(hasattr(ChartEvent, "ELEMENT_CLICK"))

    def test_import_jscode(self):
        """验证 JsCode 可从顶层导入。"""
        from pyantv import JsCode

        js = JsCode("function() {}")
        self.assertIsNotNone(js)

    def test_import_presets_module(self):
        """验证 presets 模块可从顶层导入。"""
        from pyantv import presets

        self.assertTrue(hasattr(presets, "with_dark_theme"))
        self.assertTrue(hasattr(presets, "with_auto_fit"))
        self.assertTrue(hasattr(presets, "with_smooth_animation"))

    def test_import_presets_functions(self):
        """验证 presets 函数可直接导入。"""
        from pyantv.presets import (
            with_dark_theme,
            with_polar,
        )

        self.assertTrue(callable(with_dark_theme))
        self.assertTrue(callable(with_polar))


class TestSetTitle(unittest.TestCase):
    """验证 set_title 快捷方法。"""

    def test_set_title_text(self):
        """验证设置标题文本。"""
        chart = Line().set_title("销售趋势")
        title = chart.options.get("title", {})
        self.assertEqual(title.get("title"), "销售趋势")

    def test_set_title_with_subtitle(self):
        """验证设置标题和副标题。"""
        chart = Line().set_title("主标题", subtitle="副标题")
        title = chart.options.get("title", {})
        self.assertEqual(title.get("title"), "主标题")
        self.assertEqual(title.get("subtitle"), "副标题")

    def test_set_title_with_align(self):
        """验证设置标题对齐方式。"""
        chart = Line().set_title("标题", align="center")
        title = chart.options.get("title", {})
        self.assertEqual(title.get("align"), "center")

    def test_set_title_returns_self(self):
        """验证 set_title 返回 self 支持链式调用。"""
        chart = Line()
        result = chart.set_title("标题")
        self.assertIs(result, chart)

    def test_set_title_chaining(self):
        """验证 set_title 可与其他方法链式调用。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_title("趋势图")
        )
        self.assertEqual(chart.options.get("title", {}).get("title"), "趋势图")


class TestSetPadding(unittest.TestCase):
    """验证 set_padding 快捷方法。"""

    def test_set_padding_all(self):
        """验证设置四边内边距。"""
        chart = Line().set_padding(top=10, right=20, bottom=30, left=40)
        self.assertEqual(chart.options.get("paddingTop"), 10)
        self.assertEqual(chart.options.get("paddingRight"), 20)
        self.assertEqual(chart.options.get("paddingBottom"), 30)
        self.assertEqual(chart.options.get("paddingLeft"), 40)

    def test_set_padding_partial(self):
        """验证只设置部分内边距。"""
        chart = Line().set_padding(top=10, bottom=20)
        self.assertEqual(chart.options.get("paddingTop"), 10)
        self.assertEqual(chart.options.get("paddingBottom"), 20)

    def test_set_padding_returns_self(self):
        """验证 set_padding 返回 self。"""
        chart = Line()
        result = chart.set_padding(top=10)
        self.assertIs(result, chart)


class TestSetSize(unittest.TestCase):
    """验证 set_size 快捷方法。"""

    def test_set_size_width_height(self):
        """验证设置宽高。"""
        chart = Line().set_size(width=800, height=600)
        self.assertEqual(chart.options.get("width"), 800)
        self.assertEqual(chart.options.get("height"), 600)

    def test_set_size_auto_fit(self):
        """验证设置自适应。"""
        chart = Line().set_size(is_auto_fit=True)
        self.assertIn("autoFit", chart.options)

    def test_set_size_returns_self(self):
        """验证 set_size 返回 self。"""
        chart = Line()
        result = chart.set_size(width=800)
        self.assertIs(result, chart)


class TestShortcutChaining(unittest.TestCase):
    """验证快捷方法组合链式调用。"""

    def test_full_chain(self):
        """验证完整链式调用。"""
        chart = (
            Line()
            .set_data(data=[{"x": "A", "y": 3}, {"x": "B", "y": 5}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_title("趋势图", subtitle="2024")
            .set_padding(top=20, bottom=20)
            .set_size(width=800, height=600)
            .set_theme(theme="dark")
        )
        self.assertEqual(chart.options.get("title", {}).get("title"), "趋势图")
        self.assertEqual(chart.options.get("paddingTop"), 20)
        self.assertEqual(chart.options.get("width"), 800)
        self.assertEqual(chart.render_options.get("theme"), "dark")

    def test_from_data_with_shortcuts(self):
        """验证 from_data 与快捷方法组合。"""
        chart = (
            Line.from_data(
                data=[{"x": "A", "y": 3}],
                x_field_name="x",
                y_field_name="y",
            )
            .set_title("快捷图表")
            .set_size(is_auto_fit=True)
        )
        self.assertIsInstance(chart, Line)
        self.assertEqual(chart.options.get("title", {}).get("title"), "快捷图表")

    def test_interval_shortcuts(self):
        """验证 Interval 也继承快捷方法。"""
        chart = Interval().set_title("柱状图").set_padding(top=10)
        self.assertEqual(chart.options.get("title", {}).get("title"), "柱状图")
        self.assertEqual(chart.options.get("paddingTop"), 10)

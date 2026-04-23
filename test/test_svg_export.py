"""测试 SVG 导出功能。"""

import unittest
from unittest.mock import patch

import sys


class TestSVGExport(unittest.TestCase):
    """测试 SVG 导出相关功能。"""

    def test_export_svg_without_playwright_raises_import_error(self):
        """测试没有 playwright 时 export_svg 抛出 ImportError。"""
        with patch.dict(
            "sys.modules", {"playwright": None, "playwright.sync_api": None}
        ):
            # 清除已导入的模块
            if "pyantv.render.export" in sys.modules:
                del sys.modules["pyantv.render.export"]

            # 重新导入模块
            from pyantv.render.export import export_svg

            # 创建一个简单的图表对象
            class MockChart:
                def render_embed(self):
                    return "<html><body>test</body></html>"

            chart = MockChart()

            with self.assertRaises(ImportError) as context:
                export_svg(chart, "test.svg")

            self.assertIn("Playwright is required", str(context.exception))

    def test_save_as_svg_method_exists(self):
        """测试 Line 实例有 save_as_svg 方法。"""
        from pyantv import Line

        line = Line()
        self.assertTrue(hasattr(line, "save_as_svg"))
        self.assertTrue(callable(getattr(line, "save_as_svg")))

    def test_save_as_svg_without_playwright_raises(self):
        """测试没有 playwright 时 save_as_svg 抛出 ImportError。"""
        with patch.dict(
            "sys.modules", {"playwright": None, "playwright.sync_api": None}
        ):
            # 清除已导入的模块
            if "pyantv.render.export" in sys.modules:
                del sys.modules["pyantv.render.export"]
            if "pyantv.charts.base" in sys.modules:
                del sys.modules["pyantv.charts.base"]

            # 重新导入模块
            from pyantv import Line

            line = Line()

            with self.assertRaises(ImportError) as context:
                line.save_as_svg("test.svg")

            self.assertIn("Playwright is required", str(context.exception))

    def test_export_svg_importable(self):
        """测试 export_svg 可以正常导入。"""
        from pyantv.render.export import export_svg

        self.assertIsNotNone(export_svg)
        self.assertTrue(callable(export_svg))

    def test_export_png_with_mock_playwright(self):
        """测试 export_png 核心逻辑（mock Playwright）。"""
        import sys
        import tempfile
        import os
        from unittest.mock import MagicMock, patch

        # 清除已缓存的模块
        for mod in list(sys.modules):
            if "pyantv.render.export" in mod:
                del sys.modules[mod]

        mock_page = MagicMock()
        mock_browser = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_pw = MagicMock()
        mock_pw.chromium.launch.return_value = mock_browser

        mock_sync_pw = MagicMock()
        mock_sync_pw.__enter__ = MagicMock(return_value=mock_pw)
        mock_sync_pw.__exit__ = MagicMock(return_value=False)

        mock_sync_playwright = MagicMock(return_value=mock_sync_pw)

        mock_module = MagicMock()
        mock_module.sync_playwright = mock_sync_playwright

        with patch.dict(
            "sys.modules",
            {
                "playwright": MagicMock(),
                "playwright.sync_api": mock_module,
            },
        ):
            # 重新导入
            if "pyantv.render.export" in sys.modules:
                del sys.modules["pyantv.render.export"]
            from pyantv.render.export import export_png

            class MockChart:
                def render_embed(self):
                    return "<html><body>chart</body></html>"

            with tempfile.TemporaryDirectory() as tmpdir:
                out = os.path.join(tmpdir, "test.png")
                export_png(MockChart(), out)

            mock_page.goto.assert_called_once()
            mock_page.wait_for_timeout.assert_called_once_with(2000)
            mock_page.screenshot.assert_called_once()
            mock_browser.close.assert_called_once()

    def test_export_svg_with_mock_playwright_svg_found(self):
        """测试 export_svg 找到 SVG 元素的逻辑。"""
        import sys
        import tempfile
        import os
        from unittest.mock import MagicMock, patch

        for mod in list(sys.modules):
            if "pyantv.render.export" in mod:
                del sys.modules[mod]

        mock_page = MagicMock()
        mock_page.evaluate.return_value = "<svg>test</svg>"
        mock_browser = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_pw = MagicMock()
        mock_pw.chromium.launch.return_value = mock_browser

        mock_sync_pw = MagicMock()
        mock_sync_pw.__enter__ = MagicMock(return_value=mock_pw)
        mock_sync_pw.__exit__ = MagicMock(return_value=False)

        mock_sync_playwright = MagicMock(return_value=mock_sync_pw)

        mock_module = MagicMock()
        mock_module.sync_playwright = mock_sync_playwright

        with patch.dict(
            "sys.modules",
            {
                "playwright": MagicMock(),
                "playwright.sync_api": mock_module,
            },
        ):
            if "pyantv.render.export" in sys.modules:
                del sys.modules["pyantv.render.export"]
            from pyantv.render.export import export_svg

            class MockChart:
                def render_embed(self):
                    return "<html><body>chart</body></html>"

            with tempfile.TemporaryDirectory() as tmpdir:
                out = os.path.join(tmpdir, "test.svg")
                export_svg(MockChart(), out)
                # 验证 SVG 文件被写入
                with open(out, "r") as f:
                    content = f.read()
                self.assertEqual(content, "<svg>test</svg>")

    def test_export_svg_with_mock_playwright_no_svg(self):
        """测试 export_svg 未找到 SVG 元素的回退逻辑。"""
        import sys
        import tempfile
        import os
        from unittest.mock import MagicMock, patch

        for mod in list(sys.modules):
            if "pyantv.render.export" in mod:
                del sys.modules[mod]

        mock_page = MagicMock()
        mock_page.evaluate.return_value = None  # 没有 SVG
        mock_browser = MagicMock()
        mock_browser.new_page.return_value = mock_page
        mock_pw = MagicMock()
        mock_pw.chromium.launch.return_value = mock_browser

        mock_sync_pw = MagicMock()
        mock_sync_pw.__enter__ = MagicMock(return_value=mock_pw)
        mock_sync_pw.__exit__ = MagicMock(return_value=False)

        mock_sync_playwright = MagicMock(return_value=mock_sync_pw)

        mock_module = MagicMock()
        mock_module.sync_playwright = mock_sync_playwright

        with patch.dict(
            "sys.modules",
            {
                "playwright": MagicMock(),
                "playwright.sync_api": mock_module,
            },
        ):
            if "pyantv.render.export" in sys.modules:
                del sys.modules["pyantv.render.export"]
            from pyantv.render.export import export_svg

            class MockChart:
                def render_embed(self):
                    return "<html><body>chart</body></html>"

            with tempfile.TemporaryDirectory() as tmpdir:
                out = os.path.join(tmpdir, "test.svg")
                with self.assertRaises(ValueError):
                    export_svg(MockChart(), out)

    def test_save_as_svg_calls_export_svg(self):
        """测试 save_as_svg 方法正确调用 export_svg 函数。"""
        from unittest.mock import MagicMock
        from pyantv import Line
        import pyantv.render.export as export_mod

        line = Line()
        line.set_data(data=[{"x": 1, "y": 2}])
        line.set_encode(x_field_name="x", y_field_name="y")

        original = export_mod.export_svg
        mock_fn = MagicMock()
        export_mod.export_svg = mock_fn
        try:
            line.save_as_svg("output.svg", width=800, height=600)
            mock_fn.assert_called_once_with(
                line, path="output.svg", width=800, height=600
            )
        finally:
            export_mod.export_svg = original

    def test_save_as_svg_default_params(self):
        """测试 save_as_svg 方法使用默认参数。"""
        from unittest.mock import MagicMock
        from pyantv import Line
        import pyantv.render.export as export_mod

        line = Line()

        original = export_mod.export_svg
        mock_fn = MagicMock()
        export_mod.export_svg = mock_fn
        try:
            line.save_as_svg()
            mock_fn.assert_called_once_with(
                line, path="chart.svg", width=1200, height=800
            )
        finally:
            export_mod.export_svg = original


if __name__ == "__main__":
    unittest.main()

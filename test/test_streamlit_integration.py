"""Streamlit 集成组件测试。"""

import unittest
from unittest.mock import MagicMock, patch


class TestStreamlitIntegration(unittest.TestCase):
    """测试 pyantv.web.streamlit 模块的 Streamlit 集成功能。"""

    def test_st_pyantv_without_streamlit_raises_import_error(self):
        from pyantv.web.streamlit import st_pyantv

        mock_chart = MagicMock()
        with patch.dict(
            "sys.modules",
            {
                "streamlit": None,
                "streamlit.components": None,
                "streamlit.components.v1": None,
            },
        ):
            with self.assertRaises(ImportError) as ctx:
                st_pyantv(mock_chart)
            self.assertIn("Streamlit is required", str(ctx.exception))
            self.assertIn("pip install streamlit", str(ctx.exception))

    def test_st_pyantv_calls_render_embed(self):
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"

        mock_html_fn = MagicMock()
        mock_v1 = MagicMock()
        mock_v1.html = mock_html_fn
        mock_components = MagicMock()
        mock_components.v1 = mock_v1
        mock_st = MagicMock()
        mock_st.components = mock_components

        import sys

        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k.startswith("streamlit")
        }
        sys.modules["streamlit"] = mock_st
        sys.modules["streamlit.components"] = mock_components
        sys.modules["streamlit.components.v1"] = mock_v1
        try:
            from pyantv.web import streamlit as st_mod
            import importlib

            importlib.reload(st_mod)
            st_mod.st_pyantv(mock_chart, height=400)
            mock_chart.render_embed.assert_called_once()
            mock_html_fn.assert_called_once_with(
                "<html>chart</html>",
                height=400,
                width=None,
                scrolling=False,
            )
        finally:
            for k in list(sys.modules):
                if k.startswith("streamlit"):
                    sys.modules.pop(k, None)
            sys.modules.update({k: v for k, v in saved.items() if v is not None})

    def test_st_pyantv_custom_width(self):
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html></html>"

        mock_html_fn = MagicMock()
        mock_v1 = MagicMock()
        mock_v1.html = mock_html_fn
        mock_components = MagicMock()
        mock_components.v1 = mock_v1
        mock_st = MagicMock()
        mock_st.components = mock_components

        import sys

        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k.startswith("streamlit")
        }
        sys.modules["streamlit"] = mock_st
        sys.modules["streamlit.components"] = mock_components
        sys.modules["streamlit.components.v1"] = mock_v1
        try:
            from pyantv.web import streamlit as st_mod
            import importlib

            importlib.reload(st_mod)
            st_mod.st_pyantv(mock_chart, height=600, width=800)
            call_kwargs = mock_html_fn.call_args[1]
            self.assertEqual(call_kwargs["height"], 600)
            self.assertEqual(call_kwargs["width"], 800)
        finally:
            for k in list(sys.modules):
                if k.startswith("streamlit"):
                    sys.modules.pop(k, None)
            sys.modules.update({k: v for k, v in saved.items() if v is not None})

    def test_st_pyantv_importable_from_web(self):
        from pyantv.web import st_pyantv

        self.assertTrue(callable(st_pyantv))


class TestExportPng(unittest.TestCase):
    """测试 pyantv.render.export 模块的导出功能。"""

    def test_export_png_without_playwright_raises_import_error(self):
        from pyantv.render.export import export_png

        mock_chart = MagicMock()
        with patch.dict(
            "sys.modules",
            {
                "playwright": None,
                "playwright.sync_api": None,
            },
        ):
            with self.assertRaises(ImportError) as ctx:
                export_png(mock_chart, "test.png")
            self.assertIn("Playwright is required", str(ctx.exception))

    def test_save_as_image_method_exists(self):
        from pyantv import Line

        line = Line()
        self.assertTrue(hasattr(line, "save_as_image"))
        self.assertTrue(callable(line.save_as_image))

    def test_save_as_image_without_playwright_raises(self):
        from pyantv import Line

        line = Line().set_data(data=[{"x": 1, "y": 2}])
        with patch.dict(
            "sys.modules",
            {
                "playwright": None,
                "playwright.sync_api": None,
            },
        ):
            with self.assertRaises(ImportError):
                line.save_as_image("test.png")

    def test_export_png_importable(self):
        from pyantv.render.export import export_png

        self.assertTrue(callable(export_png))


if __name__ == "__main__":
    unittest.main()

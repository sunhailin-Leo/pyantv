"""补充 notebook.py 和 base.py 覆盖率的单元测试。

覆盖目标行：
- notebook.py L48-59: is_notebook() 各 IPython shell 分支
- notebook.py L103: build_iframe_html theme_line 非默认分支
- notebook.py L108: build_iframe_html render_opts_line 分支
- base.py L219-224: _repr_html_ notebook 环境下的渲染逻辑
- base.py L273-274: render_widget 调用
"""

import unittest
from unittest.mock import MagicMock, patch


class TestIsNotebookBranches(unittest.TestCase):
    """is_notebook() 各 IPython shell 类型分支测试。"""

    def test_zmq_interactive_shell_returns_true(self):
        """覆盖 L52: ZMQInteractiveShell 返回 True。"""
        mock_shell = MagicMock()
        type(mock_shell).__name__ = "ZMQInteractiveShell"

        with patch(
            "pyantv.render.notebook.get_ipython",
            create=True,
        ) as mock_get:
            mock_get.return_value = mock_shell
            # 需要重新 import 以使 patch 生效
            with patch.dict(
                "sys.modules",
                {"IPython": MagicMock(get_ipython=mock_get)},
            ):
                from pyantv.render.notebook import is_notebook

                result = is_notebook()
                self.assertTrue(result)

    def test_terminal_interactive_shell_returns_false(self):
        """覆盖 L54: TerminalInteractiveShell 返回 False。"""
        mock_shell = MagicMock()
        type(mock_shell).__name__ = "TerminalInteractiveShell"

        mock_ipython = MagicMock()
        mock_ipython.get_ipython = MagicMock(return_value=mock_shell)

        with patch.dict(
            "sys.modules",
            {"IPython": mock_ipython},
        ):
            from importlib import reload

            import pyantv.render.notebook as nb_mod

            reload(nb_mod)
            result = nb_mod.is_notebook()
            self.assertFalse(result)

    def test_google_colab_shell_returns_true(self):
        """覆盖 L56-57: Google Colab shell 返回 True。"""
        # 创建一个真实的类，使 str(type(shell)) 包含 'google.colab'
        ColabShell = type(
            "google.colab._shell.Shell", (), {}
        )
        mock_shell = ColabShell()

        mock_ipython = MagicMock()
        mock_ipython.get_ipython = MagicMock(return_value=mock_shell)

        with patch.dict(
            "sys.modules",
            {"IPython": mock_ipython},
        ):
            from importlib import reload

            import pyantv.render.notebook as nb_mod

            reload(nb_mod)
            result = nb_mod.is_notebook()
            self.assertTrue(result)

    def test_shell_none_returns_false(self):
        """覆盖 L49: shell is None 分支。"""
        mock_ipython = MagicMock()
        mock_ipython.get_ipython = MagicMock(return_value=None)

        with patch.dict(
            "sys.modules",
            {"IPython": mock_ipython},
        ):
            from importlib import reload

            import pyantv.render.notebook as nb_mod

            reload(nb_mod)
            result = nb_mod.is_notebook()
            self.assertFalse(result)

    def test_unknown_shell_returns_false(self):
        """覆盖 L58: 未知 shell 类型返回 False。"""
        mock_shell = MagicMock()
        type(mock_shell).__name__ = "CustomShell"
        # 确保 type 字符串中不包含 google.colab
        mock_shell.__class__ = type("CustomShell", (), {})

        mock_ipython = MagicMock()
        mock_ipython.get_ipython = MagicMock(return_value=mock_shell)

        with patch.dict(
            "sys.modules",
            {"IPython": mock_ipython},
        ):
            from importlib import reload

            import pyantv.render.notebook as nb_mod

            reload(nb_mod)
            result = nb_mod.is_notebook()
            self.assertFalse(result)

    def test_import_error_returns_false(self):
        """覆盖 L59: ImportError 分支。"""
        with patch.dict(
            "sys.modules",
            {"IPython": None},
        ):
            from importlib import reload

            import pyantv.render.notebook as nb_mod

            reload(nb_mod)
            result = nb_mod.is_notebook()
            self.assertFalse(result)


class TestBuildIframeHtmlCoverage(unittest.TestCase):
    """build_iframe_html 覆盖率补充测试。"""

    def test_theme_non_default(self):
        """覆盖 L103: theme != 'default' 时生成 theme_line。"""
        from pyantv.render.notebook import (
            _NOTEBOOK_CONFIG,
            build_iframe_html,
            notebook_config,
        )

        original_theme = _NOTEBOOK_CONFIG["theme"]
        notebook_config(theme="dark")
        try:
            result = build_iframe_html(
                chart_options_json='{"type": "line"}',
                js_links=[],
                css_links=[],
            )
            self.assertIn("dark", result)
        finally:
            notebook_config(theme=original_theme)

    def test_render_options_json(self):
        """覆盖 L108: render_options_json 非空时生成 render_opts_line。"""
        from pyantv.render.notebook import build_iframe_html

        result = build_iframe_html(
            chart_options_json='{"type": "line"}',
            js_links=[],
            css_links=[],
            render_options_json='{"renderer": "svg"}',
        )
        self.assertIn("svg", result)


class TestReprHtmlInNotebook(unittest.TestCase):
    """base.py _repr_html_ 在 notebook 环境下的测试。"""

    @patch("pyantv.render.notebook.is_notebook", return_value=True)
    def test_repr_html_returns_html_in_notebook(self, mock_is_nb):
        """覆盖 L219-224: _repr_html_ notebook 环境下返回 HTML。"""
        from pyantv.charts import Line

        chart = (
            Line()
            .set_data(data=[{"x": "A", "y": 10}, {"x": "B", "y": 20}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        result = chart._repr_html_()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertIn("iframe", result)


class TestRenderWidget(unittest.TestCase):
    """base.py render_widget 的测试。"""

    def test_render_widget_calls_widget_module(self):
        """覆盖 L273-274: render_widget 调用。"""
        from pyantv.charts import Line

        chart = (
            Line()
            .set_data(data=[{"x": "A", "y": 10}, {"x": "B", "y": 20}])
            .set_encode(x_field_name="x", y_field_name="y")
        )

        mock_widget = MagicMock()
        with patch(
            "pyantv.web.widget.render_widget",
            return_value=mock_widget,
        ) as mock_rw:
            result = chart.render_widget(
                width="100%", height="500px"
            )
            mock_rw.assert_called_once_with(
                chart, width="100%", height="500px"
            )
            self.assertEqual(result, mock_widget)

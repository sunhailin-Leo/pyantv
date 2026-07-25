"""Plotly Dash 集成组件测试。

镜像 ``test_streamlit_integration.py`` 的纯 mock 范式：CI / test 依赖组不安装
``dash``，故全程用 ``sys.modules`` 注入 mock 模块，并在 finally 还原，避免污染
其他测试。
"""

import importlib
import sys
import unittest
from unittest.mock import MagicMock, patch

from pyantv import Line
from pyantv.web import dash as dash_mod


def _inject_mock_dash():
    """向 sys.modules 注入一个 mock ``dash`` 模块并返回关键 mock 对象。

    :returns: ``(mock_dash, mock_iframe)`` 元组。
    """
    mock_iframe = MagicMock(name="dash.html.Iframe_instance")
    mock_html = MagicMock(name="dash.html")
    mock_html.Iframe = MagicMock(name="dash.html.Iframe_cls", return_value=mock_iframe)
    mock_dash = MagicMock(name="dash")
    mock_dash.html = mock_html
    saved = {
        k: sys.modules.pop(k, None)
        for k in list(sys.modules)
        if k == "dash" or k.startswith("dash.")
    }
    sys.modules["dash"] = mock_dash
    importlib.reload(dash_mod)
    return mock_dash, mock_iframe, saved


def _restore_dash(saved):
    """还原 sys.modules 中被 mock 注入占位的 ``dash`` 相关模块。

    :param saved: 注入时返回的 saved 映射。
    """
    for k in list(sys.modules):
        if k == "dash" or k.startswith("dash."):
            sys.modules.pop(k, None)
    sys.modules.update({k: v for k, v in saved.items() if v is not None})
    importlib.reload(dash_mod)


class TestDashIntegration(unittest.TestCase):
    """测试 pyantv.web.dash 模块的 Plotly Dash 集成功能。"""

    def test_to_dash_without_dash_raises_import_error(self):
        """M-LAZY-IMPORT: 未安装 dash 时抛带安装提示的 ImportError。"""
        mock_chart = MagicMock()
        with patch.dict("sys.modules", {"dash": None}):
            with self.assertRaises(ImportError) as ctx:
                dash_mod.to_dash(mock_chart)
            self.assertIn("Dash is required", str(ctx.exception))
            self.assertIn("pip install dash", str(ctx.exception))

    def test_to_dash_calls_render_embed_and_uses_srcdoc_camelcase(self):
        """M-RENDER-EMBED-CALLED + M-SRCDOC-KWARG。

        调 render_embed 且以 srcDoc= kwarg 构造 Iframe；用真实 Line 保证
        srcDoc 内容是真实渲染输出。
        """
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        mock_dash, mock_iframe, saved = _inject_mock_dash()
        try:
            dash_mod.to_dash(line)
            # Iframe 构造器被调用一次
            self.assertEqual(mock_dash.html.Iframe.call_count, 1)
            kwargs = mock_dash.html.Iframe.call_args[1]
            # 关键字参数名必须是 camelCase 的 srcDoc
            self.assertIn("srcDoc", kwargs)
            # Iframe 收到的 srcDoc 恰为 render_embed() 的返回值
            self.assertEqual(kwargs["srcDoc"], line.render_embed())
            self.assertNotIn("srcdoc", kwargs)
        finally:
            _restore_dash(saved)

    def test_to_dash_calls_chart_render_embed_once(self):
        """M-RENDER-EMBED-CALLED: mock chart 调用后 render_embed 恰被调用一次。

        对齐 test_streamlit_integration.py 的镜像范式（显式 assert_called_once）。
        """
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"
        mock_dash, _, saved = _inject_mock_dash()
        try:
            dash_mod.to_dash(mock_chart)
            mock_chart.render_embed.assert_called_once()
        finally:
            _restore_dash(saved)

    def test_to_dash_srcdoc_contains_antv_g2_options(self):
        """M-RENDER: srcDoc 内容含 AntV G2 初始化标记 new G2.Chart 与 .options(。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        mock_dash, _, saved = _inject_mock_dash()
        try:
            dash_mod.to_dash(line)
            src_doc = mock_dash.html.Iframe.call_args[1]["srcDoc"]
            self.assertIsInstance(src_doc, str)
            self.assertIn("new G2.Chart", src_doc)
            self.assertIn(".options(", src_doc)
        finally:
            _restore_dash(saved)

    def test_to_dash_width_height_propagated_to_style(self):
        """S-WIDTH-HEIGHT: width/height 透传到 Iframe 的 style 字典。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"
        mock_dash, _, saved = _inject_mock_dash()
        try:
            dash_mod.to_dash(mock_chart, width="100%", height="600px")
            kwargs = mock_dash.html.Iframe.call_args[1]
            self.assertIsNotNone(kwargs.get("style"))
            self.assertEqual(kwargs["style"].get("width"), "100%")
            self.assertEqual(kwargs["style"].get("height"), "600px")
        finally:
            _restore_dash(saved)

    def test_to_dash_style_merge_with_width_height_override(self):
        """S-STYLE-MERGE: style 与 width/height 合并；后者覆盖前者同名字段，且不突变入参。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"
        user_style = {"border": "1px solid", "width": "50%"}
        mock_dash, _, saved = _inject_mock_dash()
        try:
            dash_mod.to_dash(
                mock_chart, width="100%", height="400px", style=user_style
            )
            kwargs = mock_dash.html.Iframe.call_args[1]
            style = kwargs["style"]
            # 保留 style 中的非冲突字段
            self.assertEqual(style.get("border"), "1px solid")
            # width 被 width 参数覆盖
            self.assertEqual(style.get("width"), "100%")
            self.assertEqual(style.get("height"), "400px")
            # 入参 dict 未被原地修改
            self.assertEqual(user_style["width"], "50%")
        finally:
            _restore_dash(saved)

    def test_to_dash_importable_from_web(self):
        """M-EXPORT: 可从 pyantv.web 导入且可调用。"""
        from pyantv.web import to_dash

        self.assertTrue(callable(to_dash))


if __name__ == "__main__":
    unittest.main()

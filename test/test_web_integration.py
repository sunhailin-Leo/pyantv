"""Web 集成（Widget、Integrations）测试。"""

import unittest
from unittest.mock import MagicMock, patch

from pyantv.web import integrations


class TestWebIntegration(unittest.TestCase):
    """测试 pyantv.web.integrations 模块的 Web 框架集成功能。"""

    def test_render_chart_to_html_returns_string(self):
        """测试 render_chart_to_html 返回 HTML 字符串。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>test</html>"

        result = integrations.render_chart_to_html(mock_chart)

        self.assertIsInstance(result, str)
        self.assertEqual(result, "<html>test</html>")
        mock_chart.render_embed.assert_called_once_with(
            template_name="simple_chart.html"
        )

    def test_render_chart_to_html_calls_chart_render_embed(self):
        """验证 render_chart_to_html 调用了 chart.render_embed()。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>content</html>"

        integrations.render_chart_to_html(mock_chart, template_name="custom.html")

        mock_chart.render_embed.assert_called_once_with(template_name="custom.html")

    def test_make_response_without_flask_raises_import_error(self):
        """测试 make_response 在没有 Flask 时抛出 ImportError。"""
        mock_chart = MagicMock()

        with patch.dict("sys.modules", {"flask": None}):
            with self.assertRaises(ImportError) as context:
                integrations.make_response(mock_chart)

            self.assertIn("Flask is required", str(context.exception))
            self.assertIn("pip install flask", str(context.exception))

    def test_make_response_creates_flask_response(self):
        """测试 make_response 创建 Flask Response 对象。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"

        mock_response_cls = MagicMock()
        mock_flask = MagicMock()
        mock_flask.Response = mock_response_cls

        with patch.dict("sys.modules", {"flask": mock_flask}):
            integrations.make_response(mock_chart)

        mock_response_cls.assert_called_once()

    def test_make_response_with_custom_headers(self):
        """测试 make_response 支持自定义 HTTP 响应头。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"

        mock_response_cls = MagicMock()
        mock_flask = MagicMock()
        mock_flask.Response = mock_response_cls

        custom_headers = {"X-Custom-Header": "test-value"}
        with patch.dict("sys.modules", {"flask": mock_flask}):
            integrations.make_response(mock_chart, headers=custom_headers)

        call_kwargs = mock_response_cls.call_args[1]
        self.assertIn("X-Custom-Header", call_kwargs["headers"])

    def test_make_response_with_custom_status(self):
        """测试 make_response 支持自定义 HTTP 状态码。"""
        mock_chart = MagicMock()
        mock_chart.render_embed.return_value = "<html>chart</html>"

        mock_response_cls = MagicMock()
        mock_flask = MagicMock()
        mock_flask.Response = mock_response_cls

        with patch.dict("sys.modules", {"flask": mock_flask}):
            integrations.make_response(mock_chart, status=201)

        call_kwargs = mock_response_cls.call_args[1]
        self.assertEqual(call_kwargs["status"], 201)


if __name__ == "__main__":
    unittest.main()

"""测试 pyantv.web.widget 模块。"""

import sys
import unittest
from unittest.mock import MagicMock

from pyantv.charts import Line


class TestWidget(unittest.TestCase):
    """测试 Widget 相关功能。"""

    def test_render_widget_without_ipywidgets_raises(self):
        """测试没有 ipywidgets 时抛出 ImportError。"""
        # 保存当前 ipywidgets 模块状态
        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k.startswith("ipywidgets")
        }

        try:
            # 确保 ipywidgets 不在 sys.modules 中
            if "ipywidgets" in sys.modules:
                del sys.modules["ipywidgets"]

            from pyantv.web.widget import render_widget

            chart = Line()
            with self.assertRaises(ImportError) as context:
                render_widget(chart)

            self.assertIn("ipywidgets is required", str(context.exception))
        finally:
            # 恢复 ipywidgets 模块
            for k in list(sys.modules):
                if k.startswith("ipywidgets"):
                    sys.modules.pop(k, None)
            sys.modules.update({k: v for k, v in saved.items() if v is not None})

    def test_render_widget_method_exists(self):
        """测试 Line 实例有 render_widget 方法。"""
        chart = Line()
        self.assertTrue(hasattr(chart, "render_widget"))
        self.assertTrue(callable(chart.render_widget))

    def test_chart_widget_init(self):
        """测试 ChartWidget 初始化正确。"""
        # 模拟 ipywidgets
        mock_ipywidgets = MagicMock()
        mock_ipywidgets.HTML = MagicMock()
        mock_ipywidgets.Layout = MagicMock()

        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k.startswith("ipywidgets")
        }

        try:
            sys.modules["ipywidgets"] = mock_ipywidgets

            from pyantv.web.widget import ChartWidget

            chart = Line()
            widget = ChartWidget(chart, width="80%", height="600px")

            self.assertEqual(widget._chart, chart)
            self.assertEqual(widget._width, "80%")
            self.assertEqual(widget._height, "600px")
            self.assertIsNone(widget._widget)
        finally:
            # 恢复 ipywidgets 模块
            for k in list(sys.modules):
                if k.startswith("ipywidgets"):
                    sys.modules.pop(k, None)
            sys.modules.update({k: v for k, v in saved.items() if v is not None})

    def test_chart_widget_update(self):
        """测试 ChartWidget.update() 更新数据。"""
        mock_ipywidgets = MagicMock()
        mock_ipywidgets.HTML = MagicMock()
        mock_ipywidgets.Layout = MagicMock()

        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k.startswith("ipywidgets")
        }

        try:
            sys.modules["ipywidgets"] = mock_ipywidgets

            from pyantv.web.widget import ChartWidget

            chart = Line()
            widget = ChartWidget(chart)

            # 先显示 widget
            widget.show()

            # 模拟 chart 的方法
            chart.set_data = MagicMock()
            chart.render_embed = MagicMock(return_value="<div>updated</div>")

            # 更新数据
            data = [["A", 10], ["B", 20]]
            widget.update(data=data)

            # 验证 set_data 被调用
            chart.set_data.assert_called_once_with(data=data)

            # 验证 widget.value 被更新
            self.assertEqual(widget._widget.value, "<div>updated</div>")
        finally:
            # 恢复 ipywidgets 模块
            for k in list(sys.modules):
                if k.startswith("ipywidgets"):
                    sys.modules.pop(k, None)
            sys.modules.update({k: v for k, v in saved.items() if v is not None})


if __name__ == "__main__":
    unittest.main()

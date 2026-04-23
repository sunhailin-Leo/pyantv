"""测试 pyantv.web.widget 模块。"""

import sys
import unittest
from unittest.mock import MagicMock

from pyantv.charts import Line


class TestWidget(unittest.TestCase):
    """测试 Widget 相关功能。"""

    def test_render_widget_without_ipywidgets_raises(self):
        """测试没有 ipywidgets 时抛出 ImportError。

        CI 上 `--extra all` 会安装 ipywidgets，仅靠 `del sys.modules['ipywidgets']`
        无法阻止 `import ipywidgets` 重新成功。这里用 `sys.modules['ipywidgets'] = None`
        强制让后续 import 触发 ImportError，从而真实覆盖 widget 模块的兜底分支。
        """
        # 保存当前 ipywidgets 相关模块状态
        saved = {
            k: sys.modules.pop(k, None)
            for k in list(sys.modules)
            if k == "ipywidgets" or k.startswith("ipywidgets.")
        }
        # 同时把 widget 自身从缓存里清掉，避免它已经在别处 import 过 ipywidgets
        widget_module_saved = sys.modules.pop("pyantv.web.widget", None)

        try:
            # 将 ipywidgets 设为 None，Python 在 import 时会立即抛 ImportError
            sys.modules["ipywidgets"] = None

            from pyantv.web.widget import render_widget

            chart = Line()
            with self.assertRaises(ImportError) as context:
                render_widget(chart)

            self.assertIn("ipywidgets is required", str(context.exception))
        finally:
            # 清理本测试植入的 None 占位
            sys.modules.pop("ipywidgets", None)
            # 还原原本的 ipywidgets 相关模块
            sys.modules.update({k: v for k, v in saved.items() if v is not None})
            # 还原 widget 模块缓存
            if widget_module_saved is not None:
                sys.modules["pyantv.web.widget"] = widget_module_saved
            else:
                sys.modules.pop("pyantv.web.widget", None)

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

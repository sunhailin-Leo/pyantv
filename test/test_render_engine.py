"""渲染引擎模板与输出测试。"""

import copy
import unittest

from pyantv.commons.utils import OrderedSet, PLACEHOLDER
from pyantv.datasets import EXTRA, FILENAMES
from pyantv.render.display import Javascript


class _FakeChart:
    """用于测试 RenderEngine.generate_js_link 的最小化 chart 桩。"""

    def __init__(self):
        self.js_host = ""
        self.js_dependencies = OrderedSet()
        self.dependencies = []
        self.css_libs = []


class TestGenerateJsLink(unittest.TestCase):

    def setUp(self):
        self._orig_filenames = copy.deepcopy(FILENAMES)
        self._orig_extra = copy.deepcopy(EXTRA)

    def tearDown(self):
        FILENAMES.clear()
        FILENAMES.update(self._orig_filenames)
        EXTRA.clear()
        EXTRA.update(self._orig_extra)

    def test_unknown_dependency_skipped(self):
        """未知依赖应被跳过，不出现在 dependencies 中。"""
        from pyantv.render.engine import RenderEngine

        chart = _FakeChart()
        chart.js_dependencies.add("__zzz_truly_nonexistent__")

        RenderEngine.generate_js_link(chart)

        self.assertEqual(chart.dependencies, [])
        self.assertEqual(chart.css_libs, [])

    def test_unknown_dependency_calls_warn(self):
        """未知依赖应调用 warnings.warn。"""
        import warnings as _warnings_mod
        from pyantv.render.engine import RenderEngine

        chart = _FakeChart()
        chart.js_dependencies.add("__zzz_unique_warn_test__")

        original_warn = _warnings_mod.warn
        called_with = []

        def spy_warn(*args, **kwargs):
            called_with.append(args)
            original_warn(*args, **kwargs)

        _warnings_mod.warn = spy_warn
        try:
            RenderEngine.generate_js_link(chart)
        finally:
            _warnings_mod.warn = original_warn

        self.assertTrue(len(called_with) > 0, "warnings.warn was not called")
        self.assertIn("__zzz_unique_warn_test__", str(called_with[0]))

    def test_known_dependency_resolved(self):
        """已知依赖应正确解析为链接。"""
        from pyantv.render.engine import RenderEngine

        chart = _FakeChart()
        chart.js_dependencies.add("antv@G2")

        RenderEngine.generate_js_link(chart)

        self.assertTrue(len(chart.dependencies) > 0)


class TestJavascriptLoadContents(unittest.TestCase):

    def test_load_invalid_host_graceful(self):
        """无法连接的主机应优雅处理，不崩溃。"""
        js = Javascript(lib=["https://invalid.host.test/fake.js"])

        result = js.load_javascript_contents()

        self.assertIs(result, js)
        self.assertEqual(js.javascript_contents, {})


class TestPlaceholderConstant(unittest.TestCase):

    def test_placeholder_value(self):
        """PLACEHOLDER 常量值正确。"""
        self.assertEqual(PLACEHOLDER, "--x_x--0_0--")

    def test_jscode_uses_placeholder(self):
        """JsCode 使用 PLACEHOLDER 常量包裹代码。"""
        from pyantv.commons.utils import JsCode

        code = JsCode("fn()")
        self.assertTrue(code.js_code.startswith(PLACEHOLDER))
        self.assertTrue(code.js_code.endswith(PLACEHOLDER))

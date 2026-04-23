"""插件系统（Rough、Lottie、Renderer）测试。"""

import unittest

from pyantv import Line


class TestPluginSystem(unittest.TestCase):
    """测试插件系统（use_renderer、use_rough、use_lottie）。"""

    def test_use_renderer_canvas(self):
        """测试 use_renderer("canvas") 设置 renderer 选项。"""
        chart = Line()
        result = chart.use_renderer("canvas")

        options = chart.get_options()
        self.assertEqual(options["renderer"], "canvas")
        self.assertEqual(result, chart)

    def test_use_renderer_svg(self):
        """测试 use_renderer("svg") 设置 renderer 选项。"""
        chart = Line()
        result = chart.use_renderer("svg")

        options = chart.get_options()
        self.assertEqual(options["renderer"], "svg")
        self.assertEqual(result, chart)

    def test_use_renderer_webgl(self):
        """测试 use_renderer("webgl") 设置 renderer 选项。"""
        chart = Line()
        result = chart.use_renderer("webgl")

        options = chart.get_options()
        self.assertEqual(options["renderer"], "webgl")
        self.assertEqual(result, chart)

    def test_use_renderer_invalid_raises_value_error(self):
        """测试 use_renderer("invalid") 抛出 ValueError。"""
        chart = Line()

        with self.assertRaises(ValueError) as context:
            chart.use_renderer("invalid")

        self.assertIn("Unsupported renderer", str(context.exception))
        self.assertIn("invalid", str(context.exception))

    def test_use_rough_default_parameters(self):
        """测试 use_rough() 默认参数设置 rough 选项并添加依赖。"""
        chart = Line()
        result = chart.use_rough()

        options = chart.get_options()
        self.assertIn("rough", options)
        self.assertEqual(options["rough"]["roughness"], 1.5)
        self.assertEqual(options["rough"]["bowing"], 1.0)
        self.assertEqual(result, chart)

    def test_use_rough_custom_parameters(self):
        """测试 use_rough(roughness=2.0, bowing=0.5) 自定义参数。"""
        chart = Line()
        result = chart.use_rough(roughness=2.0, bowing=0.5)

        options = chart.get_options()
        self.assertEqual(options["rough"]["roughness"], 2.0)
        self.assertEqual(options["rough"]["bowing"], 0.5)
        self.assertEqual(result, chart)

    def test_use_rough_adds_dependency(self):
        """测试 use_rough 添加正确的依赖。"""
        chart = Line()
        chart.use_rough()

        dependencies = chart.js_dependencies.items
        self.assertIn("antv@G-Rough", dependencies)

    def test_use_lottie_default_parameters(self):
        """测试 use_lottie() 默认参数设置 lottie 选项并添加依赖。"""
        chart = Line()
        result = chart.use_lottie()

        options = chart.get_options()
        self.assertIn("lottie", options)
        self.assertEqual(options["lottie"]["autoplay"], True)
        self.assertEqual(result, chart)

    def test_use_lottie_custom_parameters(self):
        """测试 use_lottie(autoplay=False) 自定义参数。"""
        chart = Line()
        result = chart.use_lottie(autoplay=False)

        options = chart.get_options()
        self.assertEqual(options["lottie"]["autoplay"], False)
        self.assertEqual(result, chart)

    def test_use_lottie_adds_dependency(self):
        """测试 use_lottie 添加正确的依赖。"""
        chart = Line()
        chart.use_lottie()

        dependencies = chart.js_dependencies.items
        self.assertIn("antv@G-Lottie", dependencies)

    def test_plugin_chain_call(self):
        """测试插件链式调用。"""
        chart = (
            Line()
            .use_renderer("svg")
            .use_rough(roughness=2.0)
            .use_lottie(autoplay=False)
        )

        options = chart.get_options()
        self.assertEqual(options["renderer"], "svg")
        self.assertEqual(options["rough"]["roughness"], 2.0)
        self.assertEqual(options["lottie"]["autoplay"], False)

    def test_js_dependencies_contains_rough(self):
        """验证 js_dependencies 包含正确的 rough 依赖名。"""
        chart = Line()
        chart.use_rough()

        dependencies = chart.js_dependencies.items
        self.assertIn("antv@G-Rough", dependencies)

    def test_js_dependencies_contains_lottie(self):
        """验证 js_dependencies 包含正确的 lottie 依赖名。"""
        chart = Line()
        chart.use_lottie()

        dependencies = chart.js_dependencies.items
        self.assertIn("antv@G-Lottie", dependencies)

    def test_multiple_plugins_add_dependencies(self):
        """测试多个插件同时使用时依赖都正确添加。"""
        chart = Line()
        chart.use_rough().use_lottie()

        dependencies = chart.js_dependencies.items
        self.assertIn("antv@G-Rough", dependencies)
        self.assertIn("antv@G-Lottie", dependencies)

    def test_use_renderer_chain_with_data(self):
        """测试 use_renderer 与数据设置的链式调用。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .use_renderer("webgl")
        )

        options = chart.get_options()
        self.assertEqual(options["renderer"], "webgl")
        self.assertEqual(options["encode"]["x"], "x")

    def test_plugin_options_persistence(self):
        """测试插件选项在后续调用中保持不变。"""
        chart = Line()
        chart.use_rough(roughness=3.0)

        options = chart.get_options()
        self.assertEqual(options["rough"]["roughness"], 3.0)

        chart.set_data(data=[{"x": 1, "y": 2}])
        options_after = chart.get_options()
        self.assertEqual(options_after["rough"]["roughness"], 3.0)


if __name__ == "__main__":
    unittest.main()

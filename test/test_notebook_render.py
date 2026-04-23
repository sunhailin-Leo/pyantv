"""Notebook 渲染引擎测试。"""

import unittest


class TestNotebookRender(unittest.TestCase):
    def test_notebook_module_importable(self):
        from pyantv.render.notebook import (
            build_iframe_html,
            is_notebook,
            notebook_config,
        )

        self.assertTrue(callable(build_iframe_html))
        self.assertTrue(callable(is_notebook))
        self.assertTrue(callable(notebook_config))

    def test_is_notebook_returns_bool(self):
        from pyantv.render.notebook import is_notebook

        result = is_notebook()
        self.assertIsInstance(result, bool)

    def test_is_notebook_false_in_test(self):
        from pyantv.render.notebook import is_notebook

        # 在 pytest 运行时不应检测为 notebook 环境
        self.assertFalse(is_notebook())

    def test_build_iframe_html_returns_string(self):
        from pyantv.render.notebook import build_iframe_html

        result = build_iframe_html(
            chart_options_json='{"type": "line"}',
            js_links=["https://cdn.jsdelivr.net/npm/@antv/g2/dist/g2.min.js"],
            css_links=[],
        )
        self.assertIsInstance(result, str)

    def test_build_iframe_html_contains_iframe(self):
        from pyantv.render.notebook import build_iframe_html

        result = build_iframe_html(
            chart_options_json='{"type": "line"}',
            js_links=["https://cdn.jsdelivr.net/npm/@antv/g2/dist/g2.min.js"],
            css_links=[],
        )
        self.assertIn("<iframe", result)
        self.assertIn("srcdoc=", result)

    def test_build_iframe_html_custom_size(self):
        from pyantv.render.notebook import build_iframe_html

        result = build_iframe_html(
            chart_options_json="{}",
            js_links=[],
            css_links=[],
            width="800px",
            height="600px",
        )
        self.assertIn("800px", result)
        self.assertIn("600px", result)

    def test_notebook_config_updates(self):
        from pyantv.render.notebook import notebook_config, _NOTEBOOK_CONFIG

        original_width = _NOTEBOOK_CONFIG["width"]
        notebook_config(width="80%", height="300px", theme="dark")
        self.assertEqual(_NOTEBOOK_CONFIG["width"], "80%")
        self.assertEqual(_NOTEBOOK_CONFIG["height"], "300px")
        self.assertEqual(_NOTEBOOK_CONFIG["theme"], "dark")
        # 恢复
        notebook_config(width=original_width, height="400px", theme="default")

    def test_repr_html_exists_on_chart(self):
        from pyantv.charts import Line

        chart = Line()
        self.assertTrue(hasattr(chart, "_repr_html_"))

    def test_repr_html_returns_none_outside_notebook(self):
        from pyantv.charts import Line

        chart = (
            Line()
            .set_data(data=[{"x": "A", "y": 10}, {"x": "B", "y": 20}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        result = chart._repr_html_()
        # 在非 notebook 环境应返回 None
        self.assertIsNone(result)

    def test_render_init_exports(self):
        from pyantv.render import build_iframe_html, is_notebook, notebook_config

        self.assertTrue(callable(build_iframe_html))
        self.assertTrue(callable(is_notebook))
        self.assertTrue(callable(notebook_config))

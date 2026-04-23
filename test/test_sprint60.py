"""Sprint 60 新增功能的测试：字段校验、配置校验、导出/导入、模板缓存、联动。"""

import warnings
import unittest

from pyantv import Line, Interval
from pyantv.charts.composition_charts.view import View


class TestFieldValidation(unittest.TestCase):
    """Sprint 60-1: set_encode 字段名校验与智能建议。"""

    def test_warning_on_unknown_field(self):
        chart = Line()
        chart.set_data(data=[{"year": "2020", "value": 3}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="yera")
            self.assertTrue(len(caught) >= 1)
            message = str(caught[0].message)
            self.assertIn("yera", message)
            self.assertIn("x_field_name", message)

    def test_suggestion_included_in_warning(self):
        chart = Line()
        chart.set_data(data=[{"year": "2020", "value": 3}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="yera")
            message = str(caught[0].message)
            self.assertIn("Did you mean", message)
            self.assertIn("'year'", message)

    def test_no_warning_on_valid_field(self):
        chart = Line()
        chart.set_data(data=[{"year": "2020", "value": 3}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="year", y_field_name="value")
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 0)

    def test_no_warning_without_data(self):
        chart = Line()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="nonexistent")
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 0)

    def test_no_warning_on_non_dict_data(self):
        chart = Line()
        chart.options["data"] = [1, 2, 3]
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="x")
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 0)

    def test_no_warning_on_empty_data(self):
        chart = Line()
        chart.options["data"] = []
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="x")
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 0)

    def test_no_suggestion_for_totally_different_field(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name="zzzzzzz_nothing_close")
            message = str(caught[0].message)
            self.assertIn("not found in data keys", message)
            self.assertNotIn("Did you mean", message)

    def test_skip_validation_for_non_string(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(x_field_name=["x", "y"])
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 0)

    def test_validate_multiple_fields(self):
        chart = Line()
        chart.set_data(data=[{"date": "2020", "amount": 100}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.set_encode(
                x_field_name="dat",
                y_field_name="ammount",
                color_field="colour",
            )
            field_warnings = [w for w in caught if "set_encode()" in str(w.message)]
            self.assertEqual(len(field_warnings), 3)


class TestRenderValidation(unittest.TestCase):
    """Sprint 60-2: 渲染前配置校验 Warning 机制。"""

    def test_warning_no_data(self):
        chart = Line()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.render_embed()
            data_warnings = [w for w in caught if "no data set" in str(w.message)]
            self.assertTrue(len(data_warnings) >= 1)

    def test_warning_no_encode(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.render_embed()
            encode_warnings = [w for w in caught if "no encode set" in str(w.message)]
            self.assertTrue(len(encode_warnings) >= 1)

    def test_no_warning_when_configured(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            chart.render_embed()
            no_data_or_encode = "no data set", "no encode set"
            config_warnings = [
                w for w in caught if any(s in str(w.message) for s in no_data_or_encode)
            ]
            self.assertEqual(len(config_warnings), 0)


class TestExportImportConfig(unittest.TestCase):
    """Sprint 60-3: 配置导出/导入。"""

    def test_export_config_structure(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        config = chart.export_config()
        self.assertIn("chart_class", config)
        self.assertIn("options", config)
        self.assertIn("render_options", config)
        self.assertIn("init_options", config)
        self.assertIn("Line", config["chart_class"])

    def test_from_config_restores_options(self):
        chart = Line()
        chart.set_data(data=[{"x": 1, "y": 2}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        config = chart.export_config()

        restored = Line.from_config(config)
        self.assertEqual(
            restored.get_options().get("encode"),
            chart.get_options().get("encode"),
        )

    def test_from_config_empty(self):
        restored = Line.from_config({})
        self.assertIsInstance(restored, Line)

    def test_roundtrip_with_theme(self):
        chart = Interval()
        chart.set_data(data=[{"cat": "A", "val": 10}])
        chart.set_encode(x_field_name="cat", y_field_name="val")
        chart.set_theme("dark")
        config = chart.export_config()

        restored = Interval.from_config(config)
        self.assertEqual(
            restored.get_options().get("data"),
            chart.get_options().get("data"),
        )


class TestTemplateCaching(unittest.TestCase):
    """Sprint 60-4: 模板缓存。"""

    def test_template_cache_reuse(self):
        from pyantv.render.engine import RenderEngine

        engine = RenderEngine()
        tpl1 = engine._get_template("simple_chart.html")
        tpl2 = engine._get_template("simple_chart.html")
        self.assertIs(tpl1, tpl2)

    def test_different_templates_cached_separately(self):
        from pyantv.render.engine import RenderEngine

        engine = RenderEngine()
        tpl1 = engine._get_template("simple_chart.html")
        tpl2 = engine._get_template("nb_jupyter_notebook.html")
        self.assertIsNot(tpl1, tpl2)


class TestViewLinkage(unittest.TestCase):
    """Sprint 60-6: 图表联动。"""

    def test_link_tooltip_default(self):
        view = View()
        result = view.link_tooltip()
        self.assertIs(result, view)
        interaction = view.options.get("interaction", {})
        self.assertEqual(interaction["tooltip"], {"shared": True})

    def test_link_tooltip_not_shared(self):
        view = View()
        view.link_tooltip(shared=False)
        interaction = view.options.get("interaction", {})
        self.assertEqual(interaction["tooltip"], {"shared": False})

    def test_link_brush_default(self):
        view = View()
        result = view.link_brush()
        self.assertIs(result, view)
        interaction = view.options.get("interaction", {})
        self.assertEqual(
            interaction["brushHighlight"],
            {"series": True, "type": "rect"},
        )

    def test_link_brush_x(self):
        view = View()
        view.link_brush(brush_type="x")
        interaction = view.options.get("interaction", {})
        self.assertEqual(interaction["brushHighlight"]["type"], "x")

    def test_link_brush_y(self):
        view = View()
        view.link_brush(brush_type="y", shared=False)
        interaction = view.options.get("interaction", {})
        self.assertEqual(interaction["brushHighlight"]["type"], "y")
        self.assertFalse(interaction["brushHighlight"]["series"])

    def test_link_brush_invalid_type(self):
        view = View()
        with self.assertRaises(ValueError) as ctx:
            view.link_brush(brush_type="circle")
        self.assertIn("circle", str(ctx.exception))

    def test_link_tooltip_with_existing_bool_interaction(self):
        view = View()
        view.options["interaction"] = True
        view.link_tooltip()
        interaction = view.options.get("interaction", {})
        self.assertIsInstance(interaction, dict)
        self.assertIn("tooltip", interaction)

    def test_link_brush_with_existing_bool_interaction(self):
        view = View()
        view.options["interaction"] = False
        view.link_brush()
        interaction = view.options.get("interaction", {})
        self.assertIsInstance(interaction, dict)
        self.assertIn("brushHighlight", interaction)

    def test_combined_tooltip_and_brush(self):
        view = View()
        view.link_tooltip().link_brush(brush_type="x")
        interaction = view.options.get("interaction", {})
        self.assertIn("tooltip", interaction)
        self.assertIn("brushHighlight", interaction)


class TestSelfReturnType(unittest.TestCase):
    """Sprint 60-5: 方法链返回类型。"""

    def test_set_methods_return_self(self):
        chart = Line()
        data = [{"x": 1, "y": 2}]
        self.assertIs(chart.set_data(data=data), chart)
        self.assertIs(chart.set_encode(x_field_name="x"), chart)
        self.assertIs(chart.set_scale(), chart)
        self.assertIs(chart.set_theme("dark"), chart)
        self.assertIs(chart.set_transform(), chart)
        self.assertIs(chart.set_coordinate(), chart)
        self.assertIs(chart.set_interaction(), chart)
        self.assertIs(chart.set_animate(), chart)
        self.assertIs(chart.set_style(), chart)
        self.assertIs(chart.set_labels(), chart)
        self.assertIs(chart.set_tooltip(), chart)
        self.assertIs(chart.set_axis(), chart)
        self.assertIs(chart.set_legend(), chart)
        self.assertIs(chart.set_annotations(), chart)
        self.assertIs(chart.set_global_options(), chart)
        self.assertIs(chart.set_events(), chart)
        self.assertIs(chart.set_title("title"), chart)
        self.assertIs(chart.set_padding(top=10), chart)
        self.assertIs(chart.set_size(width=800), chart)

    def test_full_chain(self):
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_theme("dark")
            .set_style({"fill": "red"})
            .set_title("Test")
            .set_size(width=800, height=600)
        )
        self.assertIsInstance(chart, Line)


if __name__ == "__main__":
    unittest.main()

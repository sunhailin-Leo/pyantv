"""Text 文本图表专属测试。"""

import unittest
from pyantv.charts import Text
from pyantv.globals import ChartType
from test import chart_base_test


class TestTextChart(unittest.TestCase):
    @chart_base_test(chart_type=ChartType.TEXT)
    def test_text_base(self):
        return Text().set_text_style(font_size=20)

    def test_text_chart_type(self):
        chart = Text()
        self.assertEqual(chart.options["type"], ChartType.TEXT)

    def test_text_with_font_size(self):
        chart = Text().set_text_style(font_size=24)
        options = chart.get_options()
        self.assertIn("style", options)
        self.assertEqual(options["style"]["fontSize"], 24)

    def test_text_with_font_family(self):
        chart = Text().set_text_style(font_family="Arial")
        options = chart.get_options()
        self.assertIn("style", options)
        self.assertEqual(options["style"]["fontFamily"], "Arial")

    def test_text_with_multiple_styles(self):
        chart = Text().set_text_style(
            font_size=18, font_family="Helvetica", font_weight="bold"
        )
        options = chart.get_options()
        self.assertIn("style", options)
        self.assertEqual(options["style"]["fontSize"], 18)
        self.assertEqual(options["style"]["fontFamily"], "Helvetica")
        self.assertEqual(options["style"]["fontWeight"], "bold")

    def test_text_options_not_empty(self):
        chart = Text().set_text_style(font_size=16)
        self.assertTrue(len(chart.dump_options()) > 0)

"""Theme 主题系统测试。"""

import unittest

from pyantv.charts import Line
from pyantv.globals import ThemeType


class TestTheme(unittest.TestCase):

    def test_theme_type_constants(self):
        """验证预设主题常量值正确。"""
        self.assertEqual(ThemeType.CLASSIC, "classic")
        self.assertEqual(ThemeType.DARK, "dark")
        self.assertEqual(ThemeType.ACADEMY, "academy")

    def test_set_theme_with_string(self):
        """验证 set_theme 使用字符串主题名称。"""
        line = Line().set_theme(theme=ThemeType.DARK)
        self.assertEqual(line.render_options.get("theme"), "dark")

    def test_set_theme_with_dict(self):
        """验证 set_theme 使用自定义主题字典。"""
        custom_theme = {
            "color": ["#1f77b4", "#ff7f0e", "#2ca02c"],
            "backgroundColor": "#f5f5f5",
        }
        line = Line().set_theme(theme=custom_theme)
        self.assertEqual(line.render_options.get("theme"), custom_theme)

    def test_set_theme_chaining(self):
        """验证 set_theme 支持链式调用。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_theme(theme=ThemeType.DARK)
        )
        self.assertEqual(line.render_options.get("theme"), "dark")
        self.assertEqual(line.options.get("type"), "line")

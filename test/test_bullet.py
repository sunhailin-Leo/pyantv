"""Bullet 子弹图基础功能及样式参数测试。"""

import unittest

from pyantv.charts.basic_charts.bullet import Bullet
from pyantv.charts.composition_charts.space_layer import SpaceLayer


SAMPLE_DATA = [
    {"title": "Revenue", "ranges": 300, "actual": 270, "target": 250},
    {"title": "Profit", "ranges": 30, "actual": 23, "target": 26},
]


class TestBulletBasic(unittest.TestCase):
    """验证 Bullet 基本功能。"""

    def test_inherits_space_layer(self):
        """验证 Bullet 继承自 SpaceLayer。"""
        chart = Bullet()
        self.assertIsInstance(chart, SpaceLayer)

    def test_default_type_is_spacelayer(self):
        """验证 Bullet 底层 type 为 spaceLayer。"""
        chart = Bullet()
        self.assertEqual(chart.options.get("type"), "spaceLayer")

    def test_set_bullet_data_two_layers(self):
        """验证 set_bullet_data 不传 target_field 时生成 2 层。"""
        chart = Bullet().set_bullet_data(
            data=SAMPLE_DATA,
            title_field="title",
            range_field="ranges",
            measure_field="actual",
        )
        children = chart.options.get("children", [])
        self.assertEqual(len(children), 2)

    def test_set_bullet_data_three_layers(self):
        """验证 set_bullet_data 传 target_field 时生成 3 层。"""
        chart = Bullet().set_bullet_data(
            data=SAMPLE_DATA,
            title_field="title",
            range_field="ranges",
            measure_field="actual",
            target_field="target",
        )
        children = chart.options.get("children", [])
        self.assertEqual(len(children), 3)

    def test_children_are_interval_type(self):
        """验证子图表都是 interval 类型。"""
        chart = Bullet().set_bullet_data(
            data=SAMPLE_DATA,
            title_field="title",
            range_field="ranges",
            measure_field="actual",
            target_field="target",
        )
        children = chart.options.get("children", [])
        for child in children:
            self.assertEqual(child.get("type"), "interval")

    def test_children_have_data(self):
        """验证子图表都包含数据。"""
        chart = Bullet().set_bullet_data(
            data=SAMPLE_DATA,
            title_field="title",
            range_field="ranges",
            measure_field="actual",
        )
        children = chart.options.get("children", [])
        for child in children:
            self.assertEqual(child.get("data"), SAMPLE_DATA)


class TestBulletChaining(unittest.TestCase):
    """验证 Bullet 链式调用。"""

    def test_set_bullet_data_returns_self(self):
        """验证 set_bullet_data 返回 self。"""
        chart = Bullet()
        result = chart.set_bullet_data(
            data=SAMPLE_DATA,
            title_field="title",
            range_field="ranges",
            measure_field="actual",
        )
        self.assertIs(result, chart)

    def test_set_bullet_style_returns_self(self):
        """验证 set_bullet_style 返回 self。"""
        chart = Bullet()
        result = chart.set_bullet_style(range_fill="#ccc")
        self.assertIs(result, chart)

    def test_full_chain(self):
        """验证完整链式调用。"""
        chart = (
            Bullet()
            .set_bullet_style(
                range_fill="#ddd",
                measure_fill="#1890ff",
                target_fill="#52c41a",
            )
            .set_bullet_data(
                data=SAMPLE_DATA,
                title_field="title",
                range_field="ranges",
                measure_field="actual",
                target_field="target",
            )
        )
        children = chart.options.get("children", [])
        self.assertEqual(len(children), 3)


class TestBulletStyle(unittest.TestCase):
    """验证 Bullet 样式配置。"""

    def test_custom_range_fill(self):
        """验证自定义 range 填充色。"""
        chart = (
            Bullet()
            .set_bullet_style(range_fill="#ccc")
            .set_bullet_data(
                data=SAMPLE_DATA,
                title_field="title",
                range_field="ranges",
                measure_field="actual",
            )
        )
        children = chart.options.get("children", [])
        range_style = children[0].get("style", {})
        self.assertEqual(range_style.get("fill"), "#ccc")

    def test_no_transpose(self):
        """验证 transpose=False 时不转置坐标系。"""
        chart = (
            Bullet()
            .set_bullet_style(transpose=False)
            .set_bullet_data(
                data=SAMPLE_DATA,
                title_field="title",
                range_field="ranges",
                measure_field="actual",
            )
        )
        children = chart.options.get("children", [])
        for child in children:
            self.assertNotIn("coordinate", child)


class TestBulletStyleExtended(unittest.TestCase):
    """验证 set_bullet_style 的所有可选参数分支。"""

    def test_measure_max_width(self):
        """验证 measure_max_width 参数。"""
        chart = Bullet()
        result = chart.set_bullet_style(measure_max_width=30)
        self.assertIs(result, chart)
        self.assertEqual(chart._measure_max_width, 30)

    def test_target_min_width(self):
        """验证 target_min_width 参数。"""
        chart = Bullet()
        result = chart.set_bullet_style(target_min_width=5)
        self.assertIs(result, chart)
        self.assertEqual(chart._target_min_width, 5)

    def test_transpose(self):
        """验证 transpose 参数。"""
        chart = Bullet()
        result = chart.set_bullet_style(transpose=True)
        self.assertIs(result, chart)
        self.assertTrue(chart._transpose)

    def test_all_extended_params_together(self):
        """验证同时设置所有扩展参数。"""
        chart = Bullet()
        chart.set_bullet_style(
            measure_max_width=25,
            target_min_width=3,
            transpose=True,
            hide_y_axis=True,
        )
        self.assertEqual(chart._measure_max_width, 25)
        self.assertEqual(chart._target_min_width, 3)
        self.assertTrue(chart._transpose)
        self.assertTrue(chart._hide_y_axis)


class TestBulletImport(unittest.TestCase):
    """验证 Bullet 可以从顶层导入。"""

    def test_import_from_pyantv(self):
        """验证 from pyantv import Bullet 可用。"""
        from pyantv import Bullet as B

        chart = B()
        self.assertEqual(chart.options.get("type"), "spaceLayer")

    def test_import_from_charts(self):
        """验证 from pyantv.charts import Bullet 可用。"""
        from pyantv.charts import Bullet as B

        chart = B()
        self.assertEqual(chart.options.get("type"), "spaceLayer")

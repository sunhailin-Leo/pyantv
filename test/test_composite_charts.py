"""组合图表（SpaceFlex、SpaceLayer 等）测试。"""

import unittest

from pyantv.charts import View, SpaceFlex, SpaceLayer, Interval
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_chart_type,
    ANY,
)


class TestViewAddChild(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_view_add_child(self):
        """测试 View 可以通过 add_child 添加子图表。"""
        child_chart = Interval().set_encode(
            x_field_name="date",
            y_field_name="value",
        )

        view = View().add_child(child_chart)

        options = view.options
        assert_chart_type(options, "view")
        assert_options_contains(
            options,
            {
                "type": "view",
                "children": ANY,
            },
        )
        self.assertEqual(len(options["children"]), 1)
        self.assertEqual(options["children"][0]["encode"]["x"], "date")
        self.assertEqual(options["children"][0]["encode"]["y"], "value")

        return view

    def test_view_add_child_chaining(self):
        """测试 add_child 支持链式调用。"""
        child1 = Interval().set_encode(x_field_name="x1", y_field_name="y1")
        child2 = Interval().set_encode(x_field_name="x2", y_field_name="y2")
        child3 = Interval().set_encode(x_field_name="x3", y_field_name="y3")

        view = View().add_child(child1).add_child(child2).add_child(child3)

        options = view.options
        self.assertEqual(len(options["children"]), 3)

    def test_view_add_child_preserves_options(self):
        """测试 add_child 后子图表的 options 正确保存。"""
        child = (
            Interval()
            .set_encode(
                x_field_name="date",
                y_field_name="temp",
                color_field="category",
            )
            .set_global_options(
                padding_top=10,
                padding_bottom=20,
            )
        )

        view = View().add_child(child)

        child_options = view.options["children"][0]
        self.assertEqual(child_options["encode"]["x"], "date")
        self.assertEqual(child_options["encode"]["y"], "temp")
        self.assertEqual(child_options["encode"]["color"], "category")
        self.assertIn("paddingTop", child_options)
        self.assertIn("paddingBottom", child_options)

    def test_view_add_child_multiple(self):
        """测试可以添加多个子图表。"""
        children = [
            Interval().set_encode(x_field_name=f"x{i}", y_field_name=f"y{i}")
            for i in range(5)
        ]

        view = View()
        for child in children:
            view.add_child(child)

        self.assertEqual(len(view.options["children"]), 5)

    def test_view_add_child_returns_self(self):
        """测试 add_child 返回自身。"""
        child = Interval().set_encode(x_field_name="x", y_field_name="y")
        view = View()

        result = view.add_child(child)

        self.assertIs(result, view)

    def test_view_add_child_nested(self):
        """测试支持嵌套组合图表。"""
        inner_child1 = Interval().set_encode(x_field_name="x1", y_field_name="y1")
        inner_child2 = Interval().set_encode(x_field_name="x2", y_field_name="y2")

        inner_view = View().add_child(inner_child1).add_child(inner_child2)

        outer_child = Interval().set_encode(x_field_name="x3", y_field_name="y3")

        outer_view = View().add_child(inner_view).add_child(outer_child)

        self.assertEqual(len(outer_view.options["children"]), 2)
        self.assertEqual(len(outer_view.options["children"][0]["children"]), 2)


class TestSpaceFlexAddChild(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SPACEFLEX)
    def test_space_flex_add_child(self):
        """测试 SpaceFlex 可以通过 add_child 添加子图表。"""
        child_chart = Interval().set_encode(
            x_field_name="date",
            y_field_name="value",
        )

        space_flex = SpaceFlex().add_child(child_chart)

        options = space_flex.options
        assert_chart_type(options, "spaceFlex")
        assert_options_contains(
            options,
            {
                "type": "spaceFlex",
                "children": ANY,
            },
        )
        self.assertEqual(len(options["children"]), 1)

        return space_flex

    def test_space_flex_add_child_chaining(self):
        """测试 SpaceFlex 的 add_child 支持链式调用。"""
        child1 = Interval().set_encode(x_field_name="x1", y_field_name="y1")
        child2 = Interval().set_encode(x_field_name="x2", y_field_name="y2")

        space_flex = SpaceFlex().add_child(child1).add_child(child2)

        options = space_flex.options
        self.assertEqual(len(options["children"]), 2)

    def test_space_flex_add_child_returns_self(self):
        """测试 SpaceFlex 的 add_child 返回自身。"""
        child = Interval().set_encode(x_field_name="x", y_field_name="y")
        space_flex = SpaceFlex()

        result = space_flex.add_child(child)

        self.assertIs(result, space_flex)


class TestSpaceLayerAddChild(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SPACELAYER)
    def test_space_layer_add_child(self):
        """测试 SpaceLayer 可以通过 add_child 添加子图表。"""
        child_chart = Interval().set_encode(
            x_field_name="date",
            y_field_name="value",
        )

        space_layer = SpaceLayer().add_child(child_chart)

        options = space_layer.options
        assert_chart_type(options, "spaceLayer")
        assert_options_contains(
            options,
            {
                "type": "spaceLayer",
                "children": ANY,
            },
        )
        self.assertEqual(len(options["children"]), 1)

        return space_layer

    def test_space_layer_add_child_chaining(self):
        """测试 SpaceLayer 的 add_child 支持链式调用。"""
        child1 = Interval().set_encode(x_field_name="x1", y_field_name="y1")
        child2 = Interval().set_encode(x_field_name="x2", y_field_name="y2")

        space_layer = SpaceLayer().add_child(child1).add_child(child2)

        options = space_layer.options
        self.assertEqual(len(options["children"]), 2)

    def test_space_layer_add_child_returns_self(self):
        """测试 SpaceLayer 的 add_child 返回自身。"""
        child = Interval().set_encode(x_field_name="x", y_field_name="y")
        space_layer = SpaceLayer()

        result = space_layer.add_child(child)

        self.assertIs(result, space_layer)


if __name__ == "__main__":
    unittest.main()

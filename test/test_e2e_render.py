"""端到端渲染验证测试。

验证图表从构建到 JSON 序列化输出的完整链路正确性，
包括 options 清理、JSON 序列化、JsCode 处理等。
"""

import json
import unittest

from pyantv.charts import Line, Interval
from pyantv.commons.utils import JsCode
from pyantv.options import (
    AnimateOpts,
    AnimatePropertiesOpts,
    CoordinatePolarOpts,
    ScaleLinearOpts,
    TitleOpts,
    TransformStackYOpts,
)


class TestE2ERender(unittest.TestCase):
    """端到端渲染验证测试类。"""

    def test_get_options_removes_none_values(self):
        """验证 get_options() 正确移除 None 值键。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        cleaned = line.get_options()
        for key, value in cleaned.items():
            self.assertIsNotNone(value, f"Key '{key}' should not be None after cleaning")

    def test_dump_options_valid_json(self):
        """验证 dump_options() 输出合法的 JSON 字符串。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        json_str = line.dump_options()
        parsed = json.loads(json_str)
        self.assertIsInstance(parsed, dict)
        self.assertEqual(parsed["type"], "line")
        self.assertEqual(parsed["data"], [{"x": 1, "y": 2}])
        self.assertEqual(parsed["encode"]["x"], "x")
        self.assertEqual(parsed["encode"]["y"], "y")

    def test_dump_options_jscode_serialization(self):
        """验证 JsCode 在 JSON 序列化后占位符被正确替换。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(
                x_field_name=JsCode("(d) => d.date"),
                y_field_name="y",
            )
        )
        json_str = line.dump_options()
        self.assertNotIn("--x_x--0_0--", json_str)
        self.assertIn("(d) => d.date", json_str)

    def test_dump_options_nested_opts_serialization(self):
        """验证嵌套 BasicOpts 对象在 JSON 序列化后被正确展开。"""
        enter = AnimatePropertiesOpts(type_="fadeIn", duration=500)
        animate = AnimateOpts(enter_opts=enter)
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(animate_opts=animate)
        )
        json_str = line.dump_options()
        parsed = json.loads(json_str)
        anim = parsed.get("animate")
        self.assertIsNotNone(anim)
        self.assertEqual(anim["enter"]["type"], "fadeIn")
        self.assertEqual(anim["enter"]["duration"], 500)

    def test_dump_options_transform_serialization(self):
        """验证 Transform 配置在 JSON 序列化后正确输出。"""
        interval = (
            Interval()
            .set_data(data=[{"x": "A", "y": 10}, {"x": "B", "y": 20}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(transform_opts=[TransformStackYOpts()])
        )
        json_str = interval.dump_options()
        parsed = json.loads(json_str)
        transform = parsed.get("transform")
        self.assertIsNotNone(transform)
        self.assertIsInstance(transform, list)
        self.assertEqual(transform[0]["type"], "stackY")

    def test_dump_options_coordinate_serialization(self):
        """验证 Coordinate 配置在 JSON 序列化后正确输出。"""
        interval = (
            Interval()
            .set_data(data=[{"x": "A", "y": 10}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(
                coordinate_opts=CoordinatePolarOpts(inner_radius=0.3, outer_radius=0.9)
            )
        )
        json_str = interval.dump_options()
        parsed = json.loads(json_str)
        coord = parsed.get("coordinate")
        self.assertIsNotNone(coord)
        self.assertEqual(coord["type"], "polar")
        self.assertEqual(coord["innerRadius"], 0.3)
        self.assertEqual(coord["outerRadius"], 0.9)

    def test_dump_options_title_serialization(self):
        """验证 Title 配置在 JSON 序列化后正确输出。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(
                title_opts=TitleOpts(
                    title="My Chart", subtitle="Description", align="center"
                )
            )
        )
        json_str = line.dump_options()
        parsed = json.loads(json_str)
        title = parsed.get("title")
        self.assertIsNotNone(title)
        self.assertEqual(title["title"], "My Chart")
        self.assertEqual(title["subtitle"], "Description")
        self.assertEqual(title["align"], "center")

    def test_full_pipeline_line_chart(self):
        """验证 Line 图表完整构建→序列化→解析链路。"""
        data = [
            {"year": "2020", "value": 100},
            {"year": "2021", "value": 200},
            {"year": "2022", "value": 150},
        ]
        line = (
            Line()
            .set_data(data=data)
            .set_encode(x_field_name="year", y_field_name="value")
            .set_scale(x_scale_opts=ScaleLinearOpts())
            .set_global_options(
                title_opts=TitleOpts(title="Revenue Trend"),
                animate_opts=AnimateOpts(
                    enter_opts=AnimatePropertiesOpts(type_="fadeIn", duration=800)
                ),
            )
        )
        json_str = line.dump_options()
        parsed = json.loads(json_str)

        self.assertEqual(parsed["type"], "line")
        self.assertEqual(parsed["data"], data)
        self.assertEqual(parsed["encode"]["x"], "year")
        self.assertEqual(parsed["encode"]["y"], "value")
        self.assertIn("scale", parsed)
        self.assertEqual(parsed["title"]["title"], "Revenue Trend")
        self.assertEqual(parsed["animate"]["enter"]["type"], "fadeIn")
        self.assertEqual(parsed["animate"]["enter"]["duration"], 800)

    def test_full_pipeline_interval_chart(self):
        """验证 Interval 图表完整构建→序列化→解析链路。"""
        data = [{"category": "A", "value": 30}, {"category": "B", "value": 70}]
        interval = (
            Interval()
            .set_data(data=data)
            .set_encode(
                x_field_name="category",
                y_field_name="value",
                color_field="category",
            )
            .set_global_options(
                coordinate_opts=CoordinatePolarOpts(inner_radius=0.5),
                transform_opts=[TransformStackYOpts()],
            )
        )
        json_str = interval.dump_options()
        parsed = json.loads(json_str)

        self.assertEqual(parsed["type"], "interval")
        self.assertEqual(parsed["data"], data)
        self.assertEqual(parsed["encode"]["x"], "category")
        self.assertEqual(parsed["encode"]["color"], "category")
        self.assertEqual(parsed["coordinate"]["type"], "polar")
        self.assertEqual(parsed["coordinate"]["innerRadius"], 0.5)
        self.assertEqual(parsed["transform"][0]["type"], "stackY")

    def test_prepare_render_populates_json_contents(self):
        """验证 _prepare_render 正确填充 json_contents。"""
        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )
        line._prepare_render()
        self.assertIsNotNone(line.json_contents)
        parsed = json.loads(line.json_contents)
        self.assertEqual(parsed["type"], "line")

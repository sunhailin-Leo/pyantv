"""标注系统（LineAnnotation、RegionAnnotation、TextAnnotation）测试。"""

import unittest

from pyantv.options import LineAnnotationOpts, RegionAnnotationOpts, TextAnnotationOpts
from pyantv.charts import Line


class TestAnnotations(unittest.TestCase):

    def test_line_annotation_y(self):
        """测试 LineAnnotationOpts(y=100) 生成正确的 opts。"""
        obj = LineAnnotationOpts(y=100)
        self.assertEqual(
            obj.opts,
            {
                "type": "lineY",
                "data": [100],
            },
        )

    def test_line_annotation_x(self):
        """测试 LineAnnotationOpts(x="2024-01") 生成正确的 opts。"""
        obj = LineAnnotationOpts(x="2024-01")
        self.assertEqual(
            obj.opts,
            {
                "type": "lineX",
                "data": ["2024-01"],
            },
        )

    def test_line_annotation_with_text(self):
        """测试带 text 参数的 LineAnnotationOpts。"""
        obj = LineAnnotationOpts(y=100, text="目标值")
        self.assertEqual(
            obj.opts,
            {
                "type": "lineY",
                "data": [100],
                "labels": [{"text": "目标值"}],
            },
        )

    def test_region_annotation(self):
        """测试 RegionAnnotationOpts 生成正确的 opts。"""
        obj = RegionAnnotationOpts(x_start=10, x_end=20)
        self.assertEqual(
            obj.opts,
            {
                "type": "range",
                "data": [{"xStart": 10, "xEnd": 20}],
            },
        )

    def test_region_annotation_with_fill(self):
        """测试带 fill 和 fill_opacity 的 RegionAnnotationOpts。"""
        obj = RegionAnnotationOpts(y_start=0, y_end=100, fill="red", fill_opacity=0.3)
        self.assertEqual(
            obj.opts,
            {
                "type": "range",
                "data": [{"yStart": 0, "yEnd": 100}],
                "style": {"fill": "red", "fillOpacity": 0.3},
            },
        )

    def test_text_annotation(self):
        """测试 TextAnnotationOpts 生成正确的 opts。"""
        obj = TextAnnotationOpts(x=50, y=50, text="标注文本")
        self.assertEqual(
            obj.opts,
            {
                "type": "text",
                "data": [{"x": 50, "y": 50}],
                "encode": {"text": "标注文本"},
            },
        )

    def test_set_annotations_adds_children(self):
        """测试 chart.set_annotations() 正确添加 children。"""
        chart = Line()
        annotation = LineAnnotationOpts(y=100)
        chart.set_annotations([annotation])
        self.assertIn("children", chart.options)
        self.assertEqual(len(chart.options["children"]), 1)
        self.assertEqual(chart.options["children"][0]["type"], "lineY")

    def test_set_annotations_chain_call(self):
        """测试链式调用返回 self。"""
        chart = Line()
        result = chart.set_annotations([LineAnnotationOpts(y=100)])
        self.assertIs(result, chart)

    def test_set_annotations_multiple(self):
        """测试多个标注。"""
        chart = Line()
        annotations = [
            LineAnnotationOpts(y=100),
            RegionAnnotationOpts(x_start=10, x_end=20),
            TextAnnotationOpts(x=50, y=50, text="标注"),
        ]
        chart.set_annotations(annotations)
        self.assertEqual(len(chart.options["children"]), 3)

    def test_set_annotations_none(self):
        """测试传入 None 不报错。"""
        chart = Line()
        chart.set_annotations(None)
        self.assertNotIn("children", chart.options)

    def test_set_annotations_dict(self):
        """测试传入 dict 列表。"""
        chart = Line()
        dict_annotations = [{"type": "lineY", "data": [100]}]
        chart.set_annotations(dict_annotations)
        self.assertEqual(len(chart.options["children"]), 1)
        self.assertEqual(chart.options["children"][0]["type"], "lineY")

    def test_set_annotations_preserves_existing_children(self):
        """测试不覆盖已有 children。"""
        chart = Line()
        chart.options.update(children=[{"type": "existing"}])
        chart.set_annotations([LineAnnotationOpts(y=100)])
        self.assertEqual(len(chart.options["children"]), 2)
        self.assertEqual(chart.options["children"][0]["type"], "existing")
        self.assertEqual(chart.options["children"][1]["type"], "lineY")


if __name__ == "__main__":
    unittest.main()

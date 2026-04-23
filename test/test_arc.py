"""Arc 弧形图基础功能测试。"""

import json
import os
import unittest

from pyantv.charts import Arc
from pyantv.globals import ChartType


class TestArcChart(unittest.TestCase):

    def test_arc_base(self):
        """Arc 基础渲染：创建实例、设置数据、渲染 HTML。"""
        chart = Arc()
        chart.set_data(
            data=[
                {"source": "A", "target": "B", "value": 10},
            ]
        )
        chart.set_encode(x_field_name="source", y_field_name="target")
        html_path = "test_arc_output.html"
        chart.render(html_path)
        self.assertTrue(os.path.exists(html_path))
        with open(html_path, "r") as f:
            content = f.read()
        self.assertIn("arc", content)
        os.remove(html_path)

    def test_arc_options_validation(self):
        """Arc JSON 配置校验：type 字段正确、ChartType 常量正确。"""
        chart = Arc()
        self.assertEqual(chart.options["type"], "arc")
        self.assertEqual(ChartType.ARC, "arc")

        chart.set_data(data=[{"source": "A", "target": "B", "value": 10}])
        chart.set_encode(x_field_name="source", y_field_name="target")
        options_json = json.dumps(chart.options)
        self.assertIn('"type": "arc"', options_json)

    def test_arc_empty_data(self):
        """Arc 空数据处理：空列表不应导致异常。"""
        chart = Arc()
        chart.set_data(data=[])
        chart.set_encode(x_field_name="source", y_field_name="target")
        html_path = "test_arc_empty.html"
        chart.render(html_path)
        self.assertTrue(os.path.exists(html_path))
        os.remove(html_path)

    def test_arc_method_chain(self):
        """Arc 方法链：set_data / set_encode / set_global_options 返回 self。"""
        chart = Arc()
        result_data = chart.set_data(
            data=[
                {"source": "A", "target": "B", "value": 10},
            ]
        )
        self.assertIs(result_data, chart)

        result_encode = chart.set_encode(x_field_name="source", y_field_name="target")
        self.assertIs(result_encode, chart)

        result_opts = chart.set_global_options()
        self.assertIs(result_opts, chart)

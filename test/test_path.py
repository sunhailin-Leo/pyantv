"""Path 路径图基础功能测试。"""

import json
import os
import unittest

from pyantv.charts import Path
from pyantv.globals import ChartType


class TestPathChart(unittest.TestCase):

    def test_path_base(self):
        """Path 基础渲染：创建实例、设置数据、渲染 HTML。"""
        chart = Path()
        chart.set_data(data=[{"x": 0, "y": 0}, {"x": 1, "y": 1}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        html_path = "test_path_output.html"
        chart.render(html_path)
        self.assertTrue(os.path.exists(html_path))
        with open(html_path, "r") as f:
            content = f.read()
        self.assertIn("path", content)
        os.remove(html_path)

    def test_path_options_validation(self):
        """Path JSON 配置校验：type 字段正确、ChartType 常量正确。"""
        chart = Path()
        self.assertEqual(chart.options["type"], "path")
        self.assertEqual(ChartType.PATH, "path")

        chart.set_data(data=[{"x": 0, "y": 0}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        options_json = json.dumps(chart.options)
        self.assertIn('"type": "path"', options_json)

    def test_path_empty_data(self):
        """Path 空数据处理：空列表不应导致异常。"""
        chart = Path()
        chart.set_data(data=[])
        chart.set_encode(x_field_name="x", y_field_name="y")
        html_path = "test_path_empty.html"
        chart.render(html_path)
        self.assertTrue(os.path.exists(html_path))
        os.remove(html_path)

    def test_path_method_chain(self):
        """Path 方法链：set_data / set_encode / set_global_options 返回 self。"""
        chart = Path()
        result_data = chart.set_data(data=[{"x": 0, "y": 0}])
        self.assertIs(result_data, chart)

        result_encode = chart.set_encode(x_field_name="x", y_field_name="y")
        self.assertIs(result_encode, chart)

        result_opts = chart.set_global_options()
        self.assertIs(result_opts, chart)

        # 命名空间不冲突
        from pathlib import Path as StdPath

        self.assertIsNotNone(StdPath)

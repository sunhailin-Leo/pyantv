"""Interval3D 柱状图专属测试。"""

import unittest
from pyantv import options as opts
from pyantv.charts import Interval3D
from pyantv.globals import ChartType
from test import chart_base_test


class TestInterval3DChart(unittest.TestCase):
    @chart_base_test(chart_type=ChartType.INTERVAL3D)
    def test_interval3d_base(self):
        return (
            Interval3D()
            .set_data(data=[{"x": "A", "y": 10, "z": 1}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
        )

    def test_interval3d_chart_type(self):
        chart = Interval3D()
        self.assertEqual(chart.options["type"], ChartType.INTERVAL3D)

    def test_interval3d_with_color_encode(self):
        chart = (
            Interval3D()
            .set_data(data=[{"x": "A", "y": 10, "z": 1}])
            .set_encode(
                x_field_name="x", y_field_name="y", z_field_name="z", color_field="x"
            )
        )
        options = chart.get_options()
        self.assertIn("encode", options)

    def test_interval3d_with_title(self):
        chart = (
            Interval3D()
            .set_data(data=[{"x": "A", "y": 10, "z": 1}])
            .set_global_options(title_opts=opts.TitleOpts(title="3D Bar"))
        )
        options = chart.get_options()
        self.assertIn("title", options)

    def test_interval3d_options_not_empty(self):
        chart = (
            Interval3D()
            .set_data(data=[{"x": "A", "y": 10, "z": 1}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
        )
        self.assertTrue(len(chart.dump_options()) > 0)

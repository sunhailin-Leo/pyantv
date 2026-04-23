"""Point3D 散点图专属测试。"""

import unittest
from pyantv import options as opts
from pyantv.charts import Point3D
from pyantv.globals import ChartType
from test import chart_base_test


class TestPoint3DChart(unittest.TestCase):
    @chart_base_test(chart_type=ChartType.POINT3D)
    def test_point3d_base(self):
        return (
            Point3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}, {"x": 2, "y": 3, "z": 4}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
        )

    def test_point3d_chart_type(self):
        chart = Point3D()
        self.assertEqual(chart.options["type"], ChartType.POINT3D)

    def test_point3d_with_color_encode(self):
        chart = (
            Point3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_encode(
                x_field_name="x", y_field_name="y", z_field_name="z", color_field="x"
            )
        )
        options = chart.get_options()
        self.assertIn("encode", options)

    def test_point3d_with_title(self):
        chart = (
            Point3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_global_options(title_opts=opts.TitleOpts(title="3D Point"))
        )
        options = chart.get_options()
        self.assertIn("title", options)

    def test_point3d_options_not_empty(self):
        chart = (
            Point3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
        )
        self.assertTrue(len(chart.dump_options()) > 0)

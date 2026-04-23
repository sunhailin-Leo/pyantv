"""3D 图表（Point3D、Line3D、Interval3D）基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv import Point3D, Line3D, Interval3D


class Test3DCharts(unittest.TestCase):
    """测试 3D 图表类（Point3D、Line3D、Interval3D）。"""

    def test_point3d_import(self):
        """测试 Point3D 可以成功导入。"""
        point3d = Point3D()
        self.assertIsNotNone(point3d)

    def test_line3d_import(self):
        """测试 Line3D 可以成功导入。"""
        line3d = Line3D()
        self.assertIsNotNone(line3d)

    def test_interval3d_import(self):
        """测试 Interval3D 可以成功导入。"""
        interval3d = Interval3D()
        self.assertIsNotNone(interval3d)

    def test_point3d_type_validation(self):
        """测试 Point3D 的类型验证。"""
        point3d = Point3D()
        options = point3d.get_options()
        self.assertEqual(options["type"], "point3D")

    def test_line3d_type_validation(self):
        """测试 Line3D 的类型验证。"""
        line3d = Line3D()
        options = line3d.get_options()
        self.assertEqual(options["type"], "line3D")

    def test_interval3d_type_validation(self):
        """测试 Interval3D 的类型验证。"""
        interval3d = Interval3D()
        options = interval3d.get_options()
        self.assertEqual(options["type"], "interval3D")

    def test_point3d_z_axis_encode(self):
        """测试 Point3D 的 z 轴编码设置。"""
        point3d = Point3D()
        point3d.set_encode(x_field_name="x", y_field_name="y", z_field_name="z")

        options = point3d.get_options()
        self.assertEqual(options["encode"]["x"], "x")
        self.assertEqual(options["encode"]["y"], "y")
        self.assertEqual(options["encode"]["z"], "z")

    def test_line3d_z_axis_encode(self):
        """测试 Line3D 的 z 轴编码设置。"""
        line3d = Line3D()
        line3d.set_encode(x_field_name="x", y_field_name="y", z_field_name="z")

        options = line3d.get_options()
        self.assertEqual(options["encode"]["x"], "x")
        self.assertEqual(options["encode"]["y"], "y")
        self.assertEqual(options["encode"]["z"], "z")

    def test_interval3d_z_axis_encode(self):
        """测试 Interval3D 的 z 轴编码设置。"""
        interval3d = Interval3D()
        interval3d.set_encode(x_field_name="x", y_field_name="y", z_field_name="z")

        options = interval3d.get_options()
        self.assertEqual(options["encode"]["x"], "x")
        self.assertEqual(options["encode"]["y"], "y")
        self.assertEqual(options["encode"]["z"], "z")

    def test_point3d_set_data_chain(self):
        """测试 Point3D 的 set_data 链式调用。"""
        point3d = Point3D()
        result = point3d.set_data(data=[{"x": 1, "y": 2, "z": 3}])

        self.assertEqual(result, point3d)

    def test_line3d_set_data_chain(self):
        """测试 Line3D 的 set_data 链式调用。"""
        line3d = Line3D()
        result = line3d.set_data(data=[{"x": 1, "y": 2, "z": 3}])

        self.assertEqual(result, line3d)

    def test_interval3d_set_data_chain(self):
        """测试 Interval3D 的 set_data 链式调用。"""
        interval3d = Interval3D()
        result = interval3d.set_data(data=[{"x": 1, "y": 2, "z": 3}])

        self.assertEqual(result, interval3d)

    def test_point3d_coordinate_setting(self):
        """测试 Point3D 的坐标系设置。"""
        point3d = Point3D()
        coordinate_opts = opts.CoordinateCartesian3DOpts()
        point3d.set_coordinate(coordinate_opts)

        options = point3d.get_options()
        self.assertIn("coordinate", options)

    def test_line3d_coordinate_setting(self):
        """测试 Line3D 的坐标系设置。"""
        line3d = Line3D()
        coordinate_opts = opts.CoordinateCartesian3DOpts()
        line3d.set_coordinate(coordinate_opts)

        options = line3d.get_options()
        self.assertIn("coordinate", options)

    def test_interval3d_coordinate_setting(self):
        """测试 Interval3D 的坐标系设置。"""
        interval3d = Interval3D()
        coordinate_opts = opts.CoordinateCartesian3DOpts()
        interval3d.set_coordinate(coordinate_opts)

        options = interval3d.get_options()
        self.assertIn("coordinate", options)

    def test_point3d_full_chain(self):
        """测试 Point3D 的完整链式调用。"""
        point3d = (
            Point3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
            .set_coordinate(opts.CoordinateCartesian3DOpts())
        )

        options = point3d.get_options()
        self.assertEqual(options["type"], "point3D")
        self.assertEqual(options["encode"]["z"], "z")
        self.assertIn("coordinate", options)

    def test_line3d_full_chain(self):
        """测试 Line3D 的完整链式调用。"""
        line3d = (
            Line3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
            .set_coordinate(opts.CoordinateCartesian3DOpts())
        )

        options = line3d.get_options()
        self.assertEqual(options["type"], "line3D")
        self.assertEqual(options["encode"]["z"], "z")
        self.assertIn("coordinate", options)

    def test_interval3d_full_chain(self):
        """测试 Interval3D 的完整链式调用。"""
        interval3d = (
            Interval3D()
            .set_data(data=[{"x": 1, "y": 2, "z": 3}])
            .set_encode(x_field_name="x", y_field_name="y", z_field_name="z")
            .set_coordinate(opts.CoordinateCartesian3DOpts())
        )

        options = interval3d.get_options()
        self.assertEqual(options["type"], "interval3D")
        self.assertEqual(options["encode"]["z"], "z")
        self.assertIn("coordinate", options)


if __name__ == "__main__":
    unittest.main()

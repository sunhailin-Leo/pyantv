"""from_dataframe 快捷构建方法及异常分支测试。"""

import unittest

import pandas as pd

from pyantv.charts import Line, Interval, Point, Funnel


class TestFromDataframeBasic(unittest.TestCase):
    """验证 from_dataframe() 基本功能。"""

    def test_line_from_dataframe(self):
        """验证 Line.from_dataframe 创建正确的图表。"""
        df = pd.DataFrame({"year": ["2020", "2021"], "value": [3, 4]})
        chart = Line.from_dataframe(df, x_field_name="year", y_field_name="value")
        self.assertIsInstance(chart, Line)
        self.assertEqual(chart.options.get("type"), "line")
        data = chart.options.get("data")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["year"], "2020")
        self.assertEqual(data[0]["value"], 3)

    def test_interval_from_dataframe(self):
        """验证 Interval.from_dataframe 创建正确的图表。"""
        df = pd.DataFrame({"month": ["Jan", "Feb"], "sales": [100, 200]})
        chart = Interval.from_dataframe(df, x_field_name="month", y_field_name="sales")
        self.assertIsInstance(chart, Interval)
        self.assertEqual(chart.options.get("type"), "interval")

    def test_encode_fields_set(self):
        """验证编码字段正确设置。"""
        df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
        chart = Line.from_dataframe(df, x_field_name="x", y_field_name="y")
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "x")
        self.assertEqual(encode.get("y"), "y")


class TestFromDataframeAutoInfer(unittest.TestCase):
    """验证 from_dataframe() 自动推断编码字段。"""

    def test_infer_categorical_x_numeric_y(self):
        """验证自动推断：字符串列 → x，数值列 → y。"""
        df = pd.DataFrame({"category": ["A", "B", "C"], "value": [10, 20, 30]})
        chart = Line.from_dataframe(df)
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "category")
        self.assertEqual(encode.get("y"), "value")

    def test_infer_two_numeric_columns(self):
        """验证自动推断：两个数值列时，第一个 → x，第二个 → y。"""
        df = pd.DataFrame({"col_a": [1, 2, 3], "col_b": [4, 5, 6]})
        chart = Point.from_dataframe(df)
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "col_a")
        self.assertEqual(encode.get("y"), "col_b")

    def test_infer_with_explicit_x(self):
        """验证显式指定 x 时，y 自动推断为第一个数值列。"""
        df = pd.DataFrame({"name": ["A", "B"], "score": [90, 80], "age": [20, 30]})
        chart = Line.from_dataframe(df, x_field_name="name")
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "name")
        self.assertEqual(encode.get("y"), "score")

    def test_infer_with_explicit_y(self):
        """验证显式指定 y 时，x 自动推断为第一个分类列。"""
        df = pd.DataFrame({"name": ["A", "B"], "score": [90, 80]})
        chart = Line.from_dataframe(df, y_field_name="score")
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("x"), "name")
        self.assertEqual(encode.get("y"), "score")


class TestFromDataframeNaN(unittest.TestCase):
    """验证 from_dataframe() 对 NaN 的处理。"""

    def test_nan_converted_to_none(self):
        """验证 NaN 值被转换为 None。"""
        df = pd.DataFrame({"x": ["A", "B"], "y": [1.0, float("nan")]})
        chart = Line.from_dataframe(df, x_field_name="x", y_field_name="y")
        data = chart.options.get("data")
        self.assertIsNone(data[1]["y"])


class TestFromDataframeColorField(unittest.TestCase):
    """验证 from_dataframe() 的额外编码字段。"""

    def test_color_field(self):
        """验证 color_field 正确传递。"""
        df = pd.DataFrame({"x": ["A", "B"], "y": [1, 2], "group": ["G1", "G2"]})
        chart = Line.from_dataframe(
            df, x_field_name="x", y_field_name="y", color_field="group"
        )
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("color"), "group")


class TestFromDataframeErrors(unittest.TestCase):
    """验证 from_dataframe() 的错误处理。"""

    def test_non_dataframe_raises_type_error(self):
        """验证传入非 DataFrame 时抛出 TypeError。"""
        with self.assertRaises(TypeError):
            Line.from_dataframe([{"x": 1, "y": 2}])

    def test_dict_raises_type_error(self):
        """验证传入字典时抛出 TypeError。"""
        with self.assertRaises(TypeError):
            Line.from_dataframe({"x": [1], "y": [2]})


class TestFromDataframeSubclass(unittest.TestCase):
    """验证子类正确继承 from_dataframe()。"""

    def test_funnel_from_dataframe(self):
        """验证 Funnel.from_dataframe 调用子类重写的 set_encode。"""
        df = pd.DataFrame({"stage": ["A", "B"], "value": [100, 50]})
        chart = Funnel.from_dataframe(df, x_field_name="stage", y_field_name="value")
        self.assertIsInstance(chart, Funnel)
        encode = chart.options.get("encode", {})
        self.assertEqual(encode.get("shape"), "funnel")


class TestFromDataframeChaining(unittest.TestCase):
    """验证 from_dataframe() 返回值支持链式调用。"""

    def test_chain_set_theme(self):
        """验证 from_dataframe 后可以继续链式调用。"""
        df = pd.DataFrame({"x": ["A", "B"], "y": [1, 2]})
        chart = Line.from_dataframe(df, x_field_name="x", y_field_name="y").set_theme(
            theme="dark"
        )
        self.assertEqual(chart.render_options.get("theme"), "dark")


class TestFromDataframePandasMissing(unittest.TestCase):
    """验证 pandas 未安装时 from_dataframe 抛出 ImportError。"""

    def test_raises_import_error_without_pandas(self):
        """验证 pandas 不可用时抛出 ImportError。"""
        from unittest.mock import patch

        # 直接 mock builtins.__import__ 拦截 pandas 导入
        original_import = (
            __builtins__.__import__
            if hasattr(__builtins__, "__import__")
            else __import__
        )

        def mock_import(name, *args, **kwargs):
            if name == "pandas":
                raise ImportError("No module named 'pandas'")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            with self.assertRaises(ImportError) as ctx:
                Line.from_dataframe("not_a_dataframe")
            self.assertIn("pandas", str(ctx.exception))

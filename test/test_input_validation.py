"""输入校验和友好错误消息测试。"""

import unittest

from pyantv import Line
from pyantv import options as opts


class TestSetDataValidation(unittest.TestCase):
    """测试 set_data() 的输入校验。"""

    def test_valid_list_data(self):
        line = Line().set_data(data=[{"x": 1, "y": 2}])
        self.assertEqual(line.get_options()["data"], [{"x": 1, "y": 2}])

    def test_valid_dict_data(self):
        line = Line().set_data(data={"type": "inline", "value": []})
        self.assertEqual(line.get_options()["data"], {"type": "inline", "value": []})

    def test_valid_none_data(self):
        line = Line().set_data(data=None)
        self.assertIsNone(line.get_options().get("data"))

    def test_valid_fetch_data_opts(self):
        fetch = opts.FetchDataOpts(value="https://example.com/data.json")
        line = Line().set_data(data=fetch)
        self.assertIsNotNone(line.get_options()["data"])

    def test_invalid_object_data_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line().set_data(data=object())
        self.assertIn("set_data()", str(ctx.exception))
        self.assertIn("object", str(ctx.exception))
        self.assertIn("Hint", str(ctx.exception))

    def test_invalid_set_data_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line().set_data(data={1, 2, 3})
        self.assertIn("set_data()", str(ctx.exception))
        self.assertIn("set", str(ctx.exception))

    def test_scalar_data_accepted(self):
        """Liquid 等图表需要传入 float/int/str 标量数据。"""
        from pyantv import Liquid

        liquid = Liquid().set_data(data=0.3)
        self.assertIsNotNone(liquid.get_options().get("data"))

    def test_chain_call_returns_self(self):
        line = Line()
        result = line.set_data(data=[{"x": 1}])
        self.assertIs(result, line)


class TestInitOptsValidation(unittest.TestCase):
    """测试 Base.__init__() 的 init_opts/render_opts 校验。"""

    def test_valid_init_opts_object(self):
        line = Line(init_opts=opts.InitOpts(width="800px"))
        self.assertEqual(line.width, "800px")

    def test_valid_init_opts_dict(self):
        line = Line(init_opts={"width": "600px"})
        self.assertEqual(line.width, "600px")

    def test_invalid_init_opts_string_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line(init_opts="invalid")
        self.assertIn("init_opts", str(ctx.exception))
        self.assertIn("str", str(ctx.exception))

    def test_invalid_init_opts_int_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line(init_opts=123)
        self.assertIn("init_opts", str(ctx.exception))
        self.assertIn("int", str(ctx.exception))

    def test_invalid_render_opts_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line(render_opts="invalid")
        self.assertIn("render_opts", str(ctx.exception))
        self.assertIn("str", str(ctx.exception))

    def test_invalid_render_opts_list_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line(render_opts=[1, 2, 3])
        self.assertIn("render_opts", str(ctx.exception))
        self.assertIn("list", str(ctx.exception))


class TestUseRendererValidation(unittest.TestCase):
    """测试 use_renderer() 的输入校验。"""

    def test_valid_renderer_string(self):
        line = Line().use_renderer("svg")
        self.assertEqual(line.get_options()["renderer"], "svg")

    def test_invalid_renderer_int_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line().use_renderer(123)
        self.assertIn("use_renderer()", str(ctx.exception))
        self.assertIn("int", str(ctx.exception))

    def test_invalid_renderer_none_raises_type_error(self):
        with self.assertRaises(TypeError) as ctx:
            Line().use_renderer(None)
        self.assertIn("use_renderer()", str(ctx.exception))

    def test_invalid_renderer_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            Line().use_renderer("opengl")


class TestDataFrameValidation(unittest.TestCase):
    """测试 pandas DataFrame 通过校验（不被误拦截）。"""

    def test_dataframe_passes_validation(self):
        try:
            import pandas as pd
        except ImportError:
            self.skipTest("pandas not installed")

        df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
        line = Line().set_data(data=df)
        result = line.get_options()["data"]
        self.assertEqual(len(result), 2)

    def test_numpy_array_passes_validation(self):
        try:
            import numpy as np
        except ImportError:
            self.skipTest("numpy not installed")

        arr = np.array([1, 2, 3])
        line = Line().set_data(data=arr)
        result = line.get_options()["data"]
        self.assertEqual(result, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

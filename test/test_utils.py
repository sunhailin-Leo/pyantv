"""工具函数（JsCode、OrderedSet、replace_placeholder 等）测试。"""

import unittest

from pyantv.commons import utils
from pyantv.datasets import EXTRA


class TestUtils(unittest.TestCase):

    def test_utils_produce_require_dict_with_extra(self):
        EXTRA["https://api.baidu.com"] = {
            "https://api.baidu.com/test.min": ["https://api.baidu.com/test.min", "css"]
        }
        cfg_0 = utils.produce_require_dict(
            utils.OrderedSet("https://api.baidu.com/test.min"),
            "https://example.com",
        )
        self.assertEqual(cfg_0["libraries"], ["'https://api.baidu.com/test.min'"])

    def test_js_code(self):
        fn = "function() { console.log('test_js_code') }"
        js_code = utils.JsCode(fn)
        self.assertEqual(js_code.js_code, "--x_x--0_0--{}--x_x--0_0--".format(fn))

    def test_js_code_equality(self):
        code_a = utils.JsCode("(d) => d.value")
        code_b = utils.JsCode("(d) => d.value")
        code_c = utils.JsCode("(d) => d.name")
        self.assertEqual(code_a, code_b)
        self.assertNotEqual(code_a, code_c)

    def test_js_code_equality_with_str(self):
        code = utils.JsCode("(d) => d.value")
        self.assertEqual(code, "--x_x--0_0--(d) => d.value--x_x--0_0--")
        self.assertNotEqual(code, "(d) => d.value")

    def test_js_code_equality_with_other_type(self):
        code = utils.JsCode("(d) => d.value")
        self.assertEqual(code.__eq__(42), NotImplemented)
        self.assertEqual(code.__eq__(None), NotImplemented)
        self.assertEqual(code.__eq__([1, 2]), NotImplemented)

    def test_js_code_repr(self):
        code = utils.JsCode("(d) => d.value")
        result = repr(code)
        self.assertIn("JsCode", result)
        self.assertIn("(d) => d.value", result)

    def test_js_code_hash(self):
        code_a = utils.JsCode("(d) => d.value")
        code_b = utils.JsCode("(d) => d.value")
        self.assertEqual(hash(code_a), hash(code_b))
        code_set = {code_a, code_b}
        self.assertEqual(len(code_set), 1)

    def test_ordered_set(self):
        s = utils.OrderedSet()
        s.add("a", "b", "c")
        self.assertEqual(s.items, ["a", "b", "c"])

    def test_utils_remove_key_with_none_value(self):
        mock_data = [1, 2, 3]
        list_res = utils.remove_key_with_none_value(mock_data)
        assert list_res == mock_data

        mock_data_none = None
        none_res = utils.remove_key_with_none_value(mock_data_none)
        assert none_res == mock_data_none

    def test_utils_remove_key_with_none_value_raise_value_error(self):
        import numpy as np
        import pandas as pd

        mock_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        mock_numpy_data = np.array(mock_data)
        tmp_df = pd.DataFrame({"x": mock_data})
        mock_series_data = tmp_df["x"]
        try:
            utils.remove_key_with_none_value({"data": mock_numpy_data})
        except ValueError:
            pass

        try:
            utils.remove_key_with_none_value({"data": mock_series_data})
        except ValueError:
            pass

    def test_clean_dict_empty_string_removes_key(self):
        input_dict = {"key": ""}
        result = dict(utils.remove_key_with_none_value(input_dict))
        self.assertNotIn("key", result)

    def test_clean_array_value_is_list_tuple_set(self):
        input_ = {"x": [[1, 2, 3]]}
        result = utils.remove_key_with_none_value(input_)
        self.assertEqual(result["x"], [[1, 2, 3]])

        input_ = {"x": [(1, 2, 3)]}
        result = utils.remove_key_with_none_value(input_)
        self.assertEqual(result["x"], [[1, 2, 3]])

        input_ = {"x": [{1, 2, 3}]}
        result = utils.remove_key_with_none_value(input_)
        self.assertEqual(result["x"], [[1, 2, 3]])

    def test_replace_placeholder_basic(self):
        # 带引号包裹的占位符
        self.assertEqual(
            utils.replace_placeholder('"--x_x--0_0--console.log(1)--x_x--0_0--"'),
            "console.log(1)",
        )
        # 不带引号的占位符
        self.assertEqual(
            utils.replace_placeholder("--x_x--0_0--fn()--x_x--0_0--"),
            "fn()",
        )
        # 无占位符不变
        self.assertEqual(
            utils.replace_placeholder("no placeholder here"),
            "no placeholder here",
        )
        # 混合：带引号包裹 + 普通文本
        self.assertEqual(
            utils.replace_placeholder('a "--x_x--0_0--x--x_x--0_0--" b'),
            "a x b",
        )

    def test_replace_placeholder_edge_cases(self):
        # 空字符串
        self.assertEqual(utils.replace_placeholder(""), "")
        # 纯占位符（不带引号）
        self.assertEqual(utils.replace_placeholder("--x_x--0_0--"), "")
        # 纯占位符（带引号）
        self.assertEqual(utils.replace_placeholder('"--x_x--0_0--"'), "")
        # 前有引号后无引号
        self.assertEqual(utils.replace_placeholder('"--x_x--0_0--'), "")
        # 前无引号后有引号
        self.assertEqual(utils.replace_placeholder('--x_x--0_0--"'), "")
        # 多个连续占位符
        self.assertEqual(utils.replace_placeholder("--x_x--0_0----x_x--0_0--"), "")

    def test_replace_placeholder_with_quotes_basic(self):
        # 基础移除
        self.assertEqual(
            utils.replace_placeholder_with_quotes(
                "--x_x--0_0--console.log(1)--x_x--0_0--"
            ),
            "console.log(1)",
        )
        # 无占位符不变
        self.assertEqual(
            utils.replace_placeholder_with_quotes("no placeholder"),
            "no placeholder",
        )
        # 保留引号（引号不属于占位符）
        self.assertEqual(
            utils.replace_placeholder_with_quotes('"--x_x--0_0--val--x_x--0_0--"'),
            '"val"',
        )

    def test_replace_placeholder_with_quotes_edge_cases(self):
        # 空字符串
        self.assertEqual(utils.replace_placeholder_with_quotes(""), "")
        # 纯占位符
        self.assertEqual(utils.replace_placeholder_with_quotes("--x_x--0_0--"), "")
        # 多个连续占位符
        self.assertEqual(
            utils.replace_placeholder_with_quotes("--x_x--0_0----x_x--0_0--"),
            "",
        )

    def test_replace_placeholder_integration(self):
        """集成测试：JsCode 创建 → JSON 序列化 → 占位符移除。"""
        js = utils.JsCode("(d) => d.value")
        raw_json = '{"encode": "' + js.js_code + '"}'
        cleaned = utils.replace_placeholder(raw_json)
        self.assertNotIn("--x_x--0_0--", cleaned)
        self.assertEqual(cleaned, '{"encode": (d) => d.value}')

    def test_convert_data_numpy_ndarray(self):
        """测试 numpy ndarray 数据转换。"""
        import numpy as np

        arr = np.array([1, 2, 3])
        result = utils.convert_data_if_needed(arr)
        self.assertEqual(result, [1, 2, 3])
        self.assertIsInstance(result, list)

    def test_convert_data_numpy_2d_array(self):
        """测试 numpy 二维数组转换。"""
        import numpy as np

        arr = np.array([[1, 2], [3, 4]])
        result = utils.convert_data_if_needed(arr)
        self.assertEqual(result, [[1, 2], [3, 4]])
        self.assertIsInstance(result, list)

    def test_convert_data_fallback_no_pandas_no_numpy(self):
        """pandas/numpy 不可用时走 except ImportError。"""
        import builtins

        real_import = builtins.__import__

        def mock_import(name, *args, **kwargs):
            if name in ("pandas", "numpy"):
                raise ImportError(f"mocked: {name}")
            return real_import(name, *args, **kwargs)

        builtins.__import__ = mock_import
        try:
            result = utils.convert_data_if_needed("hello")
            self.assertEqual(result, "hello")
        finally:
            builtins.__import__ = real_import

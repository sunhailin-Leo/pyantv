"""DataFrame 数据源支持测试。"""

import json
import unittest

import numpy as np
import pandas as pd

from pyantv import Line
from pyantv.commons.utils import convert_data_if_needed
from pyantv.options.chart_options import FetchDataOpts


class TestConvertDataIfNeeded(unittest.TestCase):
    """convert_data_if_needed 函数的完整测试。"""

    # --- DataFrame 转换 ---

    def test_dataframe_to_records(self):
        """DataFrame 应转换为 list[dict]。"""
        dataframe = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
        result = convert_data_if_needed(dataframe)
        self.assertEqual(result, [{"x": 1, "y": 3}, {"x": 2, "y": 4}])

    def test_empty_dataframe(self):
        """空 DataFrame 应转换为空列表。"""
        result = convert_data_if_needed(pd.DataFrame())
        self.assertEqual(result, [])

    def test_dataframe_with_nan(self):
        """DataFrame 中的 NaN 应转换为 None。"""
        dataframe = pd.DataFrame({"a": [1.0, None, 3.0]})
        result = convert_data_if_needed(dataframe)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["a"], 1.0)
        self.assertIsNone(result[1]["a"])
        self.assertEqual(result[2]["a"], 3.0)

    # --- Series 转换 ---

    def test_series_to_list(self):
        """Series 应转换为 list。"""
        series = pd.Series([1, 2, 3])
        result = convert_data_if_needed(series)
        self.assertEqual(result, [1, 2, 3])

    def test_empty_series(self):
        """空 Series 应转换为空列表。"""
        result = convert_data_if_needed(pd.Series(dtype=float))
        self.assertEqual(result, [])

    # --- ndarray 转换 ---

    def test_ndarray_to_list(self):
        """ndarray 应转换为 list。"""
        array = np.array([1, 2, 3])
        result = convert_data_if_needed(array)
        self.assertEqual(result, [1, 2, 3])

    def test_empty_ndarray(self):
        """空 ndarray 应转换为空列表。"""
        result = convert_data_if_needed(np.array([]))
        self.assertEqual(result, [])

    def test_numpy_types_to_native(self):
        """numpy int64/float64 应转换为原生 Python 类型。"""
        array = np.array([np.int64(1), np.float64(2.5)])
        result = convert_data_if_needed(array)
        self.assertIsInstance(result[0], (int, float))
        self.assertIsInstance(result[1], float)

    # --- 透传场景 ---

    def test_passthrough_list(self):
        """原生 list 应原样返回。"""
        data = [{"a": 1}, {"a": 2}]
        result = convert_data_if_needed(data)
        self.assertIs(result, data)

    def test_passthrough_dict(self):
        """原生 dict 应原样返回。"""
        data = {"type": "inline", "value": [1, 2]}
        result = convert_data_if_needed(data)
        self.assertIs(result, data)

    def test_passthrough_none(self):
        """None 应原样返回。"""
        result = convert_data_if_needed(None)
        self.assertIsNone(result)

    def test_passthrough_basic_opts(self):
        """BasicOpts 子类（如 FetchDataOpts）应原样返回。"""
        fetch_opts = FetchDataOpts(value="https://example.com/data.json")
        result = convert_data_if_needed(fetch_opts)
        self.assertIs(result, fetch_opts)

    def test_passthrough_string(self):
        """字符串应原样返回。"""
        result = convert_data_if_needed("some_string")
        self.assertEqual(result, "some_string")

    # --- JSON 序列化安全 ---

    def test_json_safe_after_dataframe_conversion(self):
        """DataFrame 转换后的数据应可通过 json.dumps 序列化。"""
        dataframe = pd.DataFrame(
            {
                "name": ["Alice", "Bob"],
                "score": [np.int64(95), np.int64(87)],
                "rate": [np.float64(0.95), np.float64(0.87)],
            }
        )
        result = convert_data_if_needed(dataframe)
        serialized = json.dumps(result)
        self.assertIsInstance(serialized, str)

    def test_json_safe_after_ndarray_conversion(self):
        """ndarray 转换后的数据应可通过 json.dumps 序列化。"""
        array = np.array([np.int64(1), np.float64(2.0), np.int64(3)])
        result = convert_data_if_needed(array)
        serialized = json.dumps(result)
        self.assertIsInstance(serialized, str)


class TestSetDataWithDataFrame(unittest.TestCase):
    """验证 Chart.set_data() 与 DataFrame 的集成。"""

    def test_set_data_with_dataframe(self):
        """Line.set_data(DataFrame) 应自动转换并存入 options。"""
        dataframe = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
        line = Line().set_data(data=dataframe)
        options = line.get_options()
        self.assertEqual(
            options["data"],
            [{"x": 1, "y": 3}, {"x": 2, "y": 4}],
        )

    def test_set_data_chain_with_dataframe(self):
        """DataFrame 传入后链式调用 set_encode 应正常工作。"""
        dataframe = pd.DataFrame({"year": ["2020", "2021"], "value": [3, 5]})
        line = (
            Line()
            .set_data(data=dataframe)
            .set_encode(x_field_name="year", y_field_name="value")
        )
        options = line.get_options()
        self.assertEqual(
            options["data"],
            [{"year": "2020", "value": 3}, {"year": "2021", "value": 5}],
        )
        self.assertEqual(options["encode"]["x"], "year")

    def test_set_data_with_list_unchanged(self):
        """原生 list 传入 set_data 行为不变。"""
        data = [{"a": 1}, {"a": 2}]
        line = Line().set_data(data=data)
        self.assertEqual(line.get_options()["data"], data)

    def test_set_data_with_fetch_opts_unchanged(self):
        """FetchDataOpts 传入 set_data 不被转换。"""
        fetch_opts = FetchDataOpts(value="https://example.com/data.json")
        line = Line().set_data(data=fetch_opts)
        self.assertIs(line.get_options()["data"], fetch_opts)

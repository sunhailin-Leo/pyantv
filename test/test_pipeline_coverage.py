"""补充 pipeline.py 覆盖率的单元测试。

覆盖目标行：
- L388: _convert_x_to_timestamp datetime.date 分支
- L393-399: _convert_x_to_timestamp str 分支 + ValueError
- L500: _downsample_lttb n<=max_points 短路
- L585: _downsample_uniform n<=max_points 短路
- L614: _downsample_random n<=max_points 短路
"""

import datetime
import unittest

from pyantv.data.pipeline import (
    _convert_x_to_timestamp,
    _downsample_lttb,
    _downsample_random,
    _downsample_uniform,
)


class TestConvertXToTimestamp(unittest.TestCase):
    """_convert_x_to_timestamp 各类型分支测试。"""

    def test_numeric_passthrough(self):
        self.assertEqual(_convert_x_to_timestamp(42), 42.0)
        self.assertEqual(_convert_x_to_timestamp(3.14), 3.14)

    def test_datetime_object(self):
        dt = datetime.datetime(2024, 1, 15, 12, 0, 0)
        result = _convert_x_to_timestamp(dt)
        self.assertEqual(result, dt.timestamp())

    def test_date_object(self):
        """覆盖 L388: datetime.date 分支。"""
        date_val = datetime.date(2024, 6, 15)
        result = _convert_x_to_timestamp(date_val)
        expected = datetime.datetime.combine(
            date_val, datetime.time.min
        ).timestamp()
        self.assertEqual(result, expected)

    def test_iso_date_string(self):
        """覆盖 L393: str 分支成功路径。"""
        result = _convert_x_to_timestamp("2024-01-15")
        expected = datetime.datetime.fromisoformat("2024-01-15").timestamp()
        self.assertEqual(result, expected)

    def test_iso_datetime_string(self):
        """覆盖 L393: str 分支（带时间）。"""
        result = _convert_x_to_timestamp("2024-01-15T12:30:00")
        expected = datetime.datetime.fromisoformat(
            "2024-01-15T12:30:00"
        ).timestamp()
        self.assertEqual(result, expected)

    def test_invalid_string_raises_value_error(self):
        """覆盖 L395-399: str 分支 ValueError。"""
        with self.assertRaises(ValueError) as ctx:
            _convert_x_to_timestamp("not-a-date")
        self.assertIn("Cannot convert x value", str(ctx.exception))
        self.assertIn("ISO format", str(ctx.exception))

    def test_unsupported_type_raises_value_error(self):
        """覆盖 else 分支（L400+）。"""
        with self.assertRaises(ValueError) as ctx:
            _convert_x_to_timestamp([1, 2, 3])
        self.assertIn("Unsupported x value type", str(ctx.exception))


class TestDownsampleShortCircuit(unittest.TestCase):
    """downsample 子函数的 n<=max_points 短路分支测试。"""

    def _make_data(self, count):
        return [{"x": i, "y": i * 2} for i in range(count)]

    def test_lttb_short_circuit(self):
        """覆盖 L500: _downsample_lttb n<=max_points 返回深拷贝。"""
        data = self._make_data(5)
        result = _downsample_lttb(data, max_points=10, x_field="x", y_field="y")
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], data[0])
        # 确认是深拷贝
        result[0]["x"] = 999
        self.assertNotEqual(data[0]["x"], 999)

    def test_uniform_short_circuit(self):
        """覆盖 L585: _downsample_uniform n<=max_points 返回深拷贝。"""
        data = self._make_data(5)
        result = _downsample_uniform(data, max_points=10)
        self.assertEqual(len(result), 5)
        result[0]["x"] = 999
        self.assertNotEqual(data[0]["x"], 999)

    def test_random_short_circuit(self):
        """覆盖 L614: _downsample_random n<=max_points 返回深拷贝。"""
        data = self._make_data(5)
        result = _downsample_random(data, max_points=10)
        self.assertEqual(len(result), 5)
        result[0]["x"] = 999
        self.assertNotEqual(data[0]["x"], 999)

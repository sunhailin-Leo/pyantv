"""降采样函数单元测试。

测试覆盖：
- LTTB 算法正确性（端点保留、数值 x 轴、日期 x 轴）
- uniform 采样稳定性
- random 采样（seed 稳定、顺序保留）
- 边界场景（空数据、小数据、字段缺失）
"""

import datetime
import unittest

from pyantv.data.pipeline import downsample


class TestDownsample(unittest.TestCase):
    """降采样函数测试类。"""

    def test_lttb_preserves_endpoints(self):
        """LTTB 算法保留首末端点。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]
        result = downsample(data, max_points=10, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 10)
        self.assertEqual(result[0]["x"], 0)
        self.assertEqual(result[0]["y"], 0)
        self.assertEqual(result[-1]["x"], 99)
        self.assertEqual(result[-1]["y"], 198)

    def test_lttb_with_numeric_x(self):
        """LTTB 支持数值 x 轴。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]
        result = downsample(data, max_points=10, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 10)
        self.assertTrue(all("x" in row for row in result))
        self.assertTrue(all("y" in row for row in result))

    def test_lttb_with_datetime_x(self):
        """LTTB 支持 datetime 对象作为 x 轴。"""
        base_date = datetime.datetime(2024, 1, 1)
        data = [
            {"x": base_date + datetime.timedelta(days=i), "y": i * 2} for i in range(100)
        ]
        result = downsample(data, max_points=10, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 10)
        self.assertEqual(result[0]["x"], base_date)
        self.assertEqual(result[-1]["x"], base_date + datetime.timedelta(days=99))

    def test_lttb_with_date_string_x(self):
        """LTTB 支持日期字符串作为 x 轴。"""
        data = [{"x": f"2024-01-{i:02d}", "y": i * 2} for i in range(1, 32)]
        result = downsample(data, max_points=10, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 10)
        self.assertEqual(result[0]["x"], "2024-01-01")
        self.assertEqual(result[-1]["x"], "2024-01-31")

    def test_lttb_small_data_returns_original(self):
        """LTTB 小数据（max_points >= len(data)）直接返回原数据。"""
        data = [{"x": i, "y": i * 2} for i in range(5)]
        result = downsample(data, max_points=10, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 5)
        self.assertEqual(result, data)

    def test_lttb_exact_max_points(self):
        """LTTB 降采样后数据点数精确等于 max_points。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]
        result = downsample(data, max_points=20, method="lttb", x_field="x", y_field="y")

        self.assertEqual(len(result), 20)

    def test_lttb_missing_x_field_raises_error(self):
        """LTTB 缺少 x_field 抛出 ValueError。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        with self.assertRaises(ValueError) as context:
            downsample(
                data, max_points=10, method="lttb", x_field="missing", y_field="y"
            )

        self.assertIn("field 'missing' does not exist", str(context.exception))

    def test_lttb_missing_y_field_raises_error(self):
        """LTTB 缺少 y_field 抛出 ValueError。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        with self.assertRaises(ValueError) as context:
            downsample(
                data, max_points=10, method="lttb", x_field="x", y_field="missing"
            )

        self.assertIn("field 'missing' does not exist", str(context.exception))

    def test_lttb_no_fields_raises_error(self):
        """LTTB 未提供 x_field/y_field 抛出 ValueError。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        with self.assertRaises(ValueError) as context:
            downsample(data, max_points=10, method="lttb")

        self.assertIn("x_field and y_field are required", str(context.exception))

    def test_uniform_stability(self):
        """uniform 方法保证时序稳定性（多次采样结果相同）。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        result1 = downsample(data, max_points=10, method="uniform")
        result2 = downsample(data, max_points=10, method="uniform")

        self.assertEqual(result1, result2)

    def test_uniform_preserves_order(self):
        """uniform 采样保留原始顺序。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]
        result = downsample(data, max_points=10, method="uniform")

        x_values = [row["x"] for row in result]
        self.assertEqual(x_values, sorted(x_values))

    def test_random_with_seed_is_deterministic(self):
        """random 方法固定 seed 保证可重现。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        result1 = downsample(data, max_points=10, method="random", random_state=42)
        result2 = downsample(data, max_points=10, method="random", random_state=42)

        self.assertEqual(result1, result2)

    def test_random_output_is_index_sorted(self):
        """random 采样后输出的 x 字段按原始 index 升序排列。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]
        result = downsample(data, max_points=10, method="random", random_state=42)

        x_values = [row["x"] for row in result]
        self.assertEqual(x_values, sorted(x_values))

    def test_random_different_seeds_different_results(self):
        """random 方法不同 seed 产生不同结果。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        result1 = downsample(data, max_points=10, method="random", random_state=42)
        result2 = downsample(data, max_points=10, method="random", random_state=43)

        self.assertNotEqual(result1, result2)

    def test_empty_data_raises_error(self):
        """空数据抛出 ValueError。"""
        with self.assertRaises(ValueError) as context:
            downsample([], max_points=10)

        self.assertIn("data cannot be empty", str(context.exception))

    def test_invalid_max_points_raises_error(self):
        """非法 max_points 抛出 ValueError。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        with self.assertRaises(ValueError) as context:
            downsample(data, max_points=0)

        self.assertIn("max_points must be positive", str(context.exception))

    def test_invalid_method_raises_error(self):
        """非法 method 抛出 ValueError。"""
        data = [{"x": i, "y": i * 2} for i in range(100)]

        with self.assertRaises(ValueError) as context:
            downsample(data, max_points=10, method="invalid")

        self.assertIn("method must be one of", str(context.exception))

    def test_non_list_data_raises_error(self):
        """非列表数据抛出 TypeError。"""
        with self.assertRaises(TypeError) as context:
            downsample("not a list", max_points=10)

        self.assertIn("data must be a list", str(context.exception))


if __name__ == "__main__":
    unittest.main()

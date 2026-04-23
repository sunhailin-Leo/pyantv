"""set_data 采样功能单元测试。

测试覆盖：
- 触发/不触发采样场景
- 采样警告
- DataFrame 兼容性
"""

import unittest
import warnings

from pyantv import Line


class TestSetDataSampling(unittest.TestCase):
    """set_data 采样功能测试类。"""

    def test_sample_if_large_triggers_warning(self):
        """数据点数超过 sample_if_large 时触发警告并降采样。

        用纯数值 x 轴（而非日期字符串）来解耦 LTTB 的时间戳解析逻辑，
        本用例只验证 "触发采样 + 发出 UserWarning" 这一行为。
        """
        data = [{"x": i, "value": i} for i in range(1, 1001)]

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            chart = Line()
            chart.set_data(
                data=data,
                sample_if_large=100,
                sample_method="lttb",
                sample_x_field="x",
                sample_y_field="value",
            )

            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[0].category, UserWarning))
            self.assertIn("exceeds sample_if_large", str(w[0].message))
            self.assertIn("Downsampling to 100 points", str(w[0].message))

            sampled_data = chart.options.get("data")
            self.assertIsNotNone(sampled_data)
            self.assertEqual(len(sampled_data), 100)

    def test_sample_if_large_no_trigger(self):
        """数据点数不超过 sample_if_large 时不触发采样。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 51)]

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            chart = Line()
            chart.set_data(
                data=data,
                sample_if_large=100,
                sample_method="lttb",
                sample_x_field="date",
                sample_y_field="value",
            )

            self.assertEqual(len(w), 0)

            sampled_data = chart.options.get("data")
            self.assertIsNotNone(sampled_data)
            self.assertEqual(len(sampled_data), 50)

    def test_sample_if_large_none_no_sampling(self):
        """sample_if_large=None 时不进行采样。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 1001)]

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            chart = Line()
            chart.set_data(data=data)

            self.assertEqual(len(w), 0)

            sampled_data = chart.options.get("data")
            self.assertIsNotNone(sampled_data)
            self.assertEqual(len(sampled_data), 1000)

    def test_sample_method_uniform(self):
        """使用 uniform 方法采样。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 1001)]

        chart = Line()
        chart.set_data(
            data=data,
            sample_if_large=100,
            sample_method="uniform",
        )

        sampled_data = chart.options.get("data")
        self.assertIsNotNone(sampled_data)
        self.assertEqual(len(sampled_data), 100)

    def test_sample_method_random(self):
        """使用 random 方法采样。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 1001)]

        chart = Line()
        chart.set_data(
            data=data,
            sample_if_large=100,
            sample_method="random",
        )

        sampled_data = chart.options.get("data")
        self.assertIsNotNone(sampled_data)
        self.assertEqual(len(sampled_data), 100)

    def test_sample_with_dataframe(self):
        """DataFrame 输入配合 sample_if_large 正常工作。

        使用纯数值 x 轴，本用例关注的是 DataFrame 兼容性而非日期 x 轴，
        日期 x 轴专门在 test_downsample.py 中覆盖。
        """
        try:
            import pandas as pd
        except ImportError:
            self.skipTest("pandas not installed")

        df = pd.DataFrame(
            {
                "x": list(range(1000)),
                "value": list(range(1000)),
            }
        )

        chart = Line()
        chart.set_data(
            data=df,
            sample_if_large=100,
            sample_method="lttb",
            sample_x_field="x",
            sample_y_field="value",
        )

        sampled_data = chart.options.get("data")
        self.assertIsNotNone(sampled_data)
        self.assertEqual(len(sampled_data), 100)


if __name__ == "__main__":
    unittest.main()

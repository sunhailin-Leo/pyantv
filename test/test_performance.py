"""性能基线测试。

测试覆盖：
- LTTB 降采样性能（10 万点降采样到 1 千点）
- 性能基线分层（本地 500ms / CI 800ms）
"""

import os
import time
import unittest

from pyantv.data.pipeline import downsample


class TestPerformance(unittest.TestCase):
    """性能基线测试类。"""

    def _get_threshold(self) -> float:
        """获取性能阈值，根据 CI 环境变量自动切换。

        Returns:
            性能阈值（秒）。
        """
        if os.environ.get("CI") == "true":
            return 0.8  # CI 环境：800ms
        return 0.5  # 本地开发：500ms

    def test_lttb_100k_to_1k_perf(self):
        """10 万点 LTTB 降采样到 1 千点的耗时测试。

        验证：
        - 本地开发机：< 500ms
        - GitHub Actions CI：< 800ms
        """
        data = [{"x": i, "y": i * 2} for i in range(100000)]
        max_points = 1000

        start_time = time.time()
        result = downsample(
            data=data,
            max_points=max_points,
            method="lttb",
            x_field="x",
            y_field="y",
        )
        end_time = time.time()

        elapsed_ms = (end_time - start_time) * 1000
        threshold_ms = self._get_threshold() * 1000

        self.assertEqual(len(result), 1000)
        self.assertLess(
            elapsed_ms,
            threshold_ms,
            f"LTTB 降采样耗时 {elapsed_ms:.2f}ms 超过阈值 {threshold_ms:.0f}ms",
        )


if __name__ == "__main__":
    unittest.main()

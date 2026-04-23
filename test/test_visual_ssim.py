"""视觉回归测试 - SSIM 路径。

使用 Playwright 截图 + scikit-image SSIM 对比，验证渲染效果与基准图片一致。

双轨共存策略：
- 本文件包含 3 个独立的 SSIM 专项测试用例
- 原有的 10 个 pixel 测试用例保留在 test/test_visual_regression.py 中

运行前需要安装：
    pip install playwright Pillow scikit-image
    playwright install chromium

首次运行需要先生成基准图片：
    UPDATE_BASELINES=1 pytest test/test_visual_ssim.py -v

正常测试模式（对比基准图片）：
    pytest test/test_visual_ssim.py -v
"""

import unittest

import pytest

from pyantv.charts import Line, Interval
from pyantv.options import (
    CoordinateThetaOpts,
    TransformStackYOpts,
)

# 依赖硬约束（M-SKIMAGE-AVAILABLE）：
# scikit-image / Pillow / playwright 已在 [project.optional-dependencies].test 中声明，
# 安装 `pip install -e '.[test]'` 后必定可用。此处**故意不用** try/except + skipUnless，
# 若 import 失败应视为 test extra 安装不完整，由上游硬失败，而非静默跳过。
from test.visual_ssim_helpers import assert_visual_match_ssim


@pytest.mark.slow
class TestVisualSSIM(unittest.TestCase):
    """视觉回归测试类 - SSIM 路径。"""

    def test_visual_ssim_line_basic(self):
        """Line 基础折线图视觉回归（SSIM 路径）。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                    {"year": "2022", "value": 150},
                    {"year": "2023", "value": 280},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        assert_visual_match_ssim(chart, "visual_line_basic_ssim")

    def test_visual_ssim_pie_chart(self):
        """饼图视觉回归（SSIM 路径）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "Category A", "count": 40},
                    {"item": "Category B", "count": 30},
                    {"item": "Category C", "count": 20},
                    {"item": "Category D", "count": 10},
                ]
            )
            .set_encode(y_field_name="count", color_field="item")
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts())
        )
        assert_visual_match_ssim(chart, "visual_pie_chart_ssim")

    def test_visual_ssim_stacked_bar(self):
        """堆叠柱状图视觉回归（SSIM 路径）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "type": "X", "value": 30},
                    {"category": "A", "type": "Y", "value": 20},
                    {"category": "B", "type": "X", "value": 50},
                    {"category": "B", "type": "Y", "value": 40},
                    {"category": "C", "type": "X", "value": 35},
                    {"category": "C", "type": "Y", "value": 25},
                ]
            )
            .set_encode(
                x_field_name="category",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
        )
        assert_visual_match_ssim(chart, "visual_stacked_bar_ssim")

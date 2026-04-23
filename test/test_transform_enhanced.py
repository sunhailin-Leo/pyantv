"""增强数据转换功能测试。"""

import unittest

from pyantv.options.global_options import (
    TransformGroupXOpts,
    TransformStackYOpts,
    TransformNormalizeYOpts,
    TransformJitterOpts,
    TransformJitterXOpts,
    TransformSymmetryYOpts,
    TransformSelectOpts,
    TransformSelectXOpts,
    TransformStackXOpts,
    TransformSortXOpts,
    TransformSortYOpts,
)
from pyantv.charts import Interval


class TestTransformEnhanced(unittest.TestCase):
    """测试图表变换选项类"""

    def test_transform_group_x_opts(self):
        """验证 TransformGroupXOpts 包含 type='groupX'"""
        opts = TransformGroupXOpts()
        self.assertEqual(opts.opts["type"], "groupX")

    def test_transform_stack_y_opts(self):
        """验证 TransformStackYOpts 包含 type='stackY'"""
        opts = TransformStackYOpts()
        self.assertEqual(opts.opts["type"], "stackY")

    def test_transform_normalize_y_opts(self):
        """验证 TransformNormalizeYOpts 包含 type='normalizeY'"""
        opts = TransformNormalizeYOpts()
        self.assertEqual(opts.opts["type"], "normalizeY")

    def test_transform_jitter_opts(self):
        """验证 TransformJitterOpts 包含 type='jitter'"""
        opts = TransformJitterOpts()
        self.assertEqual(opts.opts["type"], "jitter")

    def test_transform_jitter_x_opts(self):
        """验证 TransformJitterXOpts 包含 type='jitterX'"""
        opts = TransformJitterXOpts()
        self.assertEqual(opts.opts["type"], "jitterX")

    def test_transform_symmetry_y_opts(self):
        """验证 TransformSymmetryYOpts 包含 type='symmetryY'"""
        opts = TransformSymmetryYOpts()
        self.assertEqual(opts.opts["type"], "symmetryY")

    def test_transform_select_opts(self):
        """验证 TransformSelectOpts 包含 type='select'"""
        opts = TransformSelectOpts()
        self.assertEqual(opts.opts["type"], "select")

    def test_transform_select_x_opts(self):
        """验证 TransformSelectXOpts 包含 type='selectX'"""
        opts = TransformSelectXOpts()
        self.assertEqual(opts.opts["type"], "selectX")

    def test_transform_stack_x_opts(self):
        """验证 TransformStackXOpts 包含 type='stackX'"""
        opts = TransformStackXOpts()
        self.assertEqual(opts.opts["type"], "stackX")

    def test_transform_sort_x_opts(self):
        """验证 TransformSortXOpts 包含 type='sortX'"""
        opts = TransformSortXOpts()
        self.assertEqual(opts.opts["type"], "sortX")

    def test_transform_sort_y_opts(self):
        """验证 TransformSortYOpts 包含 type='sortY'"""
        opts = TransformSortYOpts()
        self.assertEqual(opts.opts["type"], "sortY")

    def test_set_transform_with_list(self):
        """验证 chart.set_transform([opts]) 正确设置变换列表"""
        chart = Interval()
        opts = TransformGroupXOpts()
        chart.set_transform([opts])
        self.assertIsNotNone(chart.options.get("transform"))
        self.assertEqual(len(chart.options["transform"]), 1)
        self.assertEqual(chart.options["transform"][0].opts["type"], "groupX")

    def test_set_transform_chain_call(self):
        """验证链式调用返回 self"""
        chart = Interval()
        result = chart.set_transform([TransformGroupXOpts()])
        self.assertIsInstance(result, Interval)
        self.assertIs(result, chart)

    def test_transform_in_global_options(self):
        """验证 set_global_options(transform_opts=[...]) 正确设置变换"""
        chart = Interval()
        opts = TransformStackYOpts()
        chart.set_global_options(transform_opts=[opts])
        self.assertIsNotNone(chart.options.get("transform"))
        self.assertEqual(len(chart.options["transform"]), 1)
        self.assertEqual(chart.options["transform"][0].opts["type"], "stackY")


if __name__ == "__main__":
    unittest.main()

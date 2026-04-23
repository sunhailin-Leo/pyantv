"""类型存根文件（.pyi）完整性测试。"""

import os
import unittest


class TestTypeStubsExist(unittest.TestCase):
    """验证核心 .pyi 类型存根文件存在且可被导入系统发现。"""

    STUBS_DIR = os.path.join(os.path.dirname(__file__), "..", "pyantv", "charts")

    def test_chart_pyi_exists(self):
        path = os.path.join(self.STUBS_DIR, "chart.pyi")
        self.assertTrue(os.path.isfile(path), f"{path} not found")

    def test_base_pyi_exists(self):
        path = os.path.join(self.STUBS_DIR, "base.pyi")
        self.assertTrue(os.path.isfile(path), f"{path} not found")

    def test_mixins_pyi_exists(self):
        path = os.path.join(self.STUBS_DIR, "mixins.pyi")
        self.assertTrue(os.path.isfile(path), f"{path} not found")

    def test_chart_pyi_contains_set_data(self):
        path = os.path.join(self.STUBS_DIR, "chart.pyi")
        content = open(path).read()
        self.assertIn("def set_data", content)

    def test_chart_pyi_contains_set_encode(self):
        path = os.path.join(self.STUBS_DIR, "chart.pyi")
        content = open(path).read()
        self.assertIn("def set_encode", content)

    def test_chart_pyi_returns_self(self):
        path = os.path.join(self.STUBS_DIR, "chart.pyi")
        content = open(path).read()
        self.assertIn("-> Self", content)

    def test_mixins_pyi_contains_use_renderer(self):
        path = os.path.join(self.STUBS_DIR, "mixins.pyi")
        content = open(path).read()
        self.assertIn("def use_renderer", content)

    def test_base_pyi_contains_render(self):
        path = os.path.join(self.STUBS_DIR, "base.pyi")
        content = open(path).read()
        self.assertIn("def render", content)


if __name__ == "__main__":
    unittest.main()

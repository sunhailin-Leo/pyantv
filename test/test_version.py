"""版本号格式和导入验证测试。"""

import unittest


class TestVersion(unittest.TestCase):
    def test_version_importable(self):
        import pyantv

        self.assertTrue(hasattr(pyantv, "__version__"))

    def test_version_is_string(self):
        import pyantv

        self.assertIsInstance(pyantv.__version__, str)

    def test_version_pep440_format(self):
        import pyantv

        pattern = r"^\d+\.\d+\.\d+"
        self.assertRegex(pyantv.__version__, pattern)

    def test_author_importable(self):
        import pyantv

        self.assertTrue(hasattr(pyantv, "__author__"))
        self.assertEqual(pyantv.__author__, "sunhailin-Leo")

    def test_version_from_module(self):
        from pyantv._version import __version__

        self.assertIsInstance(__version__, str)
        self.assertTrue(len(__version__) > 0)

    def test_version_not_empty(self):
        import pyantv

        self.assertTrue(len(pyantv.__version__) > 0)

"""离线资源管理功能测试。

本模块测试离线资源下载、注册、host 管理等功能。
严格遵循 Sprint 63 合约的验收标准。
"""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from pyantv import Line
from pyantv.globals import CurrentConfig
from pyantv.offline import (
    AssetEntry,
    AssetRegistry,
    OfflineInstallError,
    get_active_host,
    install_assets,
    set_offline_host,
)


class TestOfflineModule(unittest.TestCase):
    """离线模块基础测试。"""

    # M-NO-IMPORTORSKIP: 禁止使用 importorskip，直接 import
    # 模块不存在即为 FAIL，不得转为 SKIP

    def test_module_import(self):
        """测试模块可以正常导入（M-NO-IMPORTORSKIP）。"""
        from pyantv.offline import (
            AssetRegistry,
            install_assets,
            set_offline_host,
            get_active_host,
            OfflineInstallError,
        )

        self.assertIsNotNone(AssetRegistry)
        self.assertIsNotNone(install_assets)
        self.assertIsNotNone(set_offline_host)
        self.assertIsNotNone(get_active_host)
        self.assertIsNotNone(OfflineInstallError)


class TestAssetEntry(unittest.TestCase):
    """AssetEntry 测试。"""

    def test_asset_entry_properties(self):
        """测试 AssetEntry 属性。"""
        entry = AssetEntry(
            name="G2",
            version="5.2.11",
            cdn_url="https://unpkg.com/@antv/g2@5.2.11/dist/g2.min.js",
            filename="g2.min.js",
            sri_hash="sha384-xxx",
        )
        self.assertEqual(entry.name, "G2")
        self.assertEqual(entry.version, "5.2.11")
        self.assertEqual(
            entry.cdn_url, "https://unpkg.com/@antv/g2@5.2.11/dist/g2.min.js"
        )
        self.assertEqual(entry.filename, "g2.min.js")
        self.assertEqual(entry.sri_hash, "sha384-xxx")


class TestAssetRegistry(unittest.TestCase):
    """AssetRegistry 测试。"""

    def setUp(self):
        """测试前清理注册表。"""
        AssetRegistry._registry.clear()

    def tearDown(self):
        """测试后恢复默认资源。"""
        AssetRegistry._registry.clear()
        # 恢复默认注册
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()

    def test_register_and_get(self):
        """测试注册和获取资源。"""
        AssetRegistry.register(
            name="TEST",
            version="1.0.0",
            cdn_url="https://example.com/test@1.0.0/test.js",
            filename="test.js",
        )
        entry = AssetRegistry.get("TEST")
        self.assertEqual(entry.name, "TEST")
        self.assertEqual(entry.version, "1.0.0")

    def test_get_nonexistent_raises_keyerror(self):
        """测试获取不存在的资源抛出 KeyError。"""
        with self.assertRaises(KeyError):
            AssetRegistry.get("NONEXISTENT")

    def test_list_registered(self):
        """测试列出已注册资源。"""
        AssetRegistry.register(
            name="A", version="1.0", cdn_url="https://a.com/a.js", filename="a.js"
        )
        AssetRegistry.register(
            name="B", version="2.0", cdn_url="https://b.com/b.js", filename="b.js"
        )
        registered = AssetRegistry.list_registered()
        self.assertIn("A", registered)
        self.assertIn("B", registered)

    def test_unregister(self):
        """测试注销资源。"""
        AssetRegistry.register(
            name="TEMP", version="1.0", cdn_url="https://t.com/t.js", filename="t.js"
        )
        self.assertIn("TEMP", AssetRegistry.list_registered())
        AssetRegistry.unregister("TEMP")
        self.assertNotIn("TEMP", AssetRegistry.list_registered())

    def test_default_g2_registered(self):
        """测试默认注册 G2 资源（S-DEFAULT-G2）。"""
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()
        entry = AssetRegistry.get("G2")
        self.assertEqual(entry.name, "G2")
        self.assertEqual(entry.version, "5.2.11")
        self.assertEqual(
            entry.cdn_url, "https://unpkg.com/@antv/g2@5.2.11/dist/g2.min.js"
        )

    def test_g2_version_pinned(self):
        """测试 G2 CDN URL 包含具体版本（M-G2-VERSION-PINNED）。"""
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()
        entry = AssetRegistry.get("G2")
        self.assertIn("@5.2.11", entry.cdn_url)

    def test_g6_placeholder_registered(self):
        """测试 G6 占位注册（S-G6-PLACEHOLDER）。"""
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()
        entry = AssetRegistry.get("G6")
        self.assertEqual(entry.name, "G6")
        self.assertEqual(entry.version, "5.0.51")

    def test_l7_placeholder_registered(self):
        """测试 L7 占位注册（S-L7-PLACEHOLDER）。"""
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()
        entry = AssetRegistry.get("L7")
        self.assertEqual(entry.name, "L7")
        self.assertEqual(entry.version, "2.22.1")


class TestInstallAssets(unittest.TestCase):
    """install_assets 函数测试。"""

    def setUp(self):
        """测试前清理注册表。"""
        AssetRegistry._registry.clear()

    def tearDown(self):
        """测试后恢复默认资源。"""
        AssetRegistry._registry.clear()
        from pyantv.offline.assets import _register_default_assets

        _register_default_assets()

    @patch("urllib.request.urlopen")
    def test_install_assets_basic(self, mock_urlopen):
        """测试基础安装功能（M-VERIFY-1）。"""
        # Mock 响应
        mock_response = MagicMock()
        mock_response.read.return_value = b"fake js content"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # 注册测试资源
        AssetRegistry.register(
            name="TEST",
            version="1.0.0",
            cdn_url="https://example.com/test.js",
            filename="test.js",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            result = install_assets(target_dir=tmpdir, libs=["TEST"])
            self.assertIn("TEST", result)
            self.assertTrue(Path(result["TEST"]).exists())

    @patch("urllib.request.urlopen")
    def test_selective_download(self, mock_urlopen):
        """测试选择性下载（S-SELECTIVE-DOWNLOAD）。"""
        mock_response = MagicMock()
        mock_response.read.return_value = b"content"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        AssetRegistry.register(
            name="A", version="1.0", cdn_url="https://a.com/a.js", filename="a.js"
        )
        AssetRegistry.register(
            name="B", version="2.0", cdn_url="https://b.com/b.js", filename="b.js"
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            result = install_assets(target_dir=tmpdir, libs=["A"])
            self.assertIn("A", result)
            self.assertNotIn("B", result)

    @patch("urllib.request.urlopen")
    def test_cache_behavior(self, mock_urlopen):
        """测试缓存行为（S-CACHE）。"""
        call_count = {"count": 0}

        def mock_read():
            call_count["count"] += 1
            return b"content"

        mock_response = MagicMock()
        mock_response.read.side_effect = mock_read
        mock_urlopen.return_value.__enter__.return_value = mock_response

        AssetRegistry.register(
            name="CACHED",
            version="1.0",
            cdn_url="https://c.com/c.js",
            filename="c.js",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            # 第一次下载
            install_assets(target_dir=tmpdir, libs=["CACHED"], use_cache=True)
            first_count = call_count["count"]

            # 第二次下载（使用缓存）
            install_assets(target_dir=tmpdir, libs=["CACHED"], use_cache=True)
            self.assertEqual(call_count["count"], first_count)

            # 强制下载
            install_assets(target_dir=tmpdir, libs=["CACHED"], use_cache=False)
            self.assertGreater(call_count["count"], first_count)

    @patch("urllib.request.urlopen")
    def test_version_override(self, mock_urlopen):
        """测试版本覆盖。"""
        mock_response = MagicMock()
        mock_response.read.return_value = b"content"
        mock_urlopen.return_value.__enter__.return_value = mock_response

        AssetRegistry.register(
            name="VERSION_TEST",
            version="1.0.0",
            cdn_url="https://example.com/lib@1.0.0/lib.js",
            filename="lib.js",
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            install_assets(
                target_dir=tmpdir,
                libs=["VERSION_TEST"],
                version_map={"VERSION_TEST": "2.0.0"},
            )
            # 验证 URL 被修改
            mock_urlopen.assert_called()
            call_args = mock_urlopen.call_args[0][0]
            self.assertIn("@2.0.0", call_args)

    def test_install_nonexistent_raises_error(self):
        """测试安装不存在的资源抛出 OfflineInstallError。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(OfflineInstallError):
                install_assets(target_dir=tmpdir, libs=["NONEXISTENT"])


class TestOfflineHost(unittest.TestCase):
    """离线 host 管理测试。"""

    def test_set_and_get_offline_host(self):
        """测试设置和获取离线 host（M-VERIFY-2）。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            set_offline_host("file:///path/to/assets")
            self.assertEqual(get_active_host(), "file:///path/to/assets")
        finally:
            CurrentConfig.OFFLINE_HOST = original_host

    def test_offline_host_priority(self):
        """测试 offline host 优先级（M-VERIFY-2）。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            # 设置 OFFLINE_HOST
            set_offline_host("file:///offline/assets")
            self.assertEqual(get_active_host(), "file:///offline/assets")

            # 清除 OFFLINE_HOST，测试环境变量
            CurrentConfig.OFFLINE_HOST = ""
            with patch.dict(os.environ, {"PYANTV_OFFLINE_HOST": "http://env-host"}):
                self.assertEqual(get_active_host(), "http://env-host")

            # 清除环境变量，测试默认 ONLINE_HOST
            with patch.dict(os.environ, {}, clear=True):
                # 移除 PYANTV_OFFLINE_HOST
                if "PYANTV_OFFLINE_HOST" in os.environ:
                    del os.environ["PYANTV_OFFLINE_HOST"]
                self.assertEqual(get_active_host(), CurrentConfig.ONLINE_HOST)
        finally:
            CurrentConfig.OFFLINE_HOST = original_host

    def test_env_lazy_read(self):
        """测试环境变量懒读（M-ENV-LAZY-READ）。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            CurrentConfig.OFFLINE_HOST = ""
            # 初始没有环境变量
            with patch.dict(os.environ, {}, clear=True):
                if "PYANTV_OFFLINE_HOST" in os.environ:
                    del os.environ["PYANTV_OFFLINE_HOST"]
                self.assertEqual(get_active_host(), CurrentConfig.ONLINE_HOST)

            # 设置环境变量后立即生效（无需重新 import）
            with patch.dict(os.environ, {"PYANTV_OFFLINE_HOST": "http://new-host"}):
                self.assertEqual(get_active_host(), "http://new-host")
        finally:
            CurrentConfig.OFFLINE_HOST = original_host

    def test_env_var_name_correct(self):
        """测试环境变量名是 PYANTV_OFFLINE_HOST（S-ENV-VAR）。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            CurrentConfig.OFFLINE_HOST = ""
            with patch.dict(os.environ, {"PYANTV_OFFLINE_HOST": "http://correct-name"}):
                self.assertEqual(get_active_host(), "http://correct-name")
        finally:
            CurrentConfig.OFFLINE_HOST = original_host


class TestCrossPlatformFileUri(unittest.TestCase):
    """跨平台 file:// URI 测试。"""

    def test_file_uri_generation(self):
        """测试 file:// URI 生成（S-CROSS-PLATFORM-FILE-URI）。"""
        # 使用 pathlib.Path.as_uri() 生成跨平台 URI。
        # 注意：as_uri() 要求传入绝对路径，Windows 上 "/tmp/..." 是相对路径会抛
        # ValueError，因此用 tempfile.gettempdir() 拿到当前平台真实的绝对临时目录。
        import tempfile

        test_path = Path(tempfile.gettempdir()) / "assets" / "g2.min.js"
        file_uri = test_path.as_uri()
        self.assertTrue(file_uri.startswith("file://"))
        # 文件名在 URI 中保留
        self.assertIn("g2.min.js", file_uri)

    def test_windows_path_uri(self):
        """测试 Windows 路径 URI。"""
        # 模拟 Windows 路径
        from pathlib import PureWindowsPath

        win_path = PureWindowsPath("C:\\assets\\g2.min.js")
        file_uri = win_path.as_uri()
        self.assertTrue(file_uri.startswith("file:///"))
        self.assertIn("g2.min.js", file_uri)


class TestRenderWithOfflineHost(unittest.TestCase):
    """测试离线 host 渲染。"""

    def test_render_with_offline_host(self):
        """测试使用离线 host 渲染（M-RENDER）。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            set_offline_host("file:///path/to/assets")

            chart = Line()
            html = chart.render_embed()

            # 验证 HTML 中的 script src 使用 offline host
            self.assertIn('src="file:///path/to/assets', html)
        finally:
            CurrentConfig.OFFLINE_HOST = original_host

    def test_render_with_env_host(self):
        """测试使用环境变量 host 渲染。"""
        original_host = CurrentConfig.OFFLINE_HOST
        try:
            CurrentConfig.OFFLINE_HOST = ""
            with patch.dict(os.environ, {"PYANTV_OFFLINE_HOST": "http://env-assets"}):
                chart = Line()
                html = chart.render_embed()
                self.assertIn('src="http://env-assets', html)
        finally:
            CurrentConfig.OFFLINE_HOST = original_host


class TestGlobalStateIsolation(unittest.TestCase):
    """测试全局状态隔离（S-TEST-FIXTURE-ISOLATION）。"""

    def setUp(self):
        """在每个测试前保存原始状态。"""
        self.original_online_host = CurrentConfig.ONLINE_HOST
        self.original_offline_host = CurrentConfig.OFFLINE_HOST
        self.original_notebook_type = CurrentConfig.NOTEBOOK_TYPE

    def tearDown(self):
        """在每个测试后恢复原始状态。"""
        CurrentConfig.ONLINE_HOST = self.original_online_host
        CurrentConfig.OFFLINE_HOST = self.original_offline_host
        CurrentConfig.NOTEBOOK_TYPE = self.original_notebook_type

    def test_global_state_isolated(self):
        """测试全局状态被正确隔离。"""
        # 修改全局状态
        CurrentConfig.ONLINE_HOST = "http://modified-host"
        CurrentConfig.OFFLINE_HOST = "file:///modified-offline"

        # 验证修改生效
        self.assertEqual(CurrentConfig.ONLINE_HOST, "http://modified-host")
        self.assertEqual(CurrentConfig.OFFLINE_HOST, "file:///modified-offline")

        # tearDown 会自动恢复原始状态


if __name__ == "__main__":
    unittest.main()

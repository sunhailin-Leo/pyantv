"""补充 assets.py 覆盖率的单元测试。

覆盖目标行：
- L139: install_assets — urllib.request.urlopen 成功下载
- L145: install_assets — local_file.write_bytes 写入
- L180-181: install_assets — 下载异常时抛出 OfflineInstallError
"""

import tempfile
import unittest
from unittest.mock import MagicMock, patch

from pyantv.offline.assets import (
    AssetRegistry,
    OfflineInstallError,
    install_assets,
)


class TestInstallAssets(unittest.TestCase):
    """install_assets 下载逻辑测试。"""

    def setUp(self):
        """注册一个测试用资源。"""
        AssetRegistry.register(
            name="TestLib",
            version="1.0.0",
            cdn_url="https://cdn.example.com/@test/lib@1.0.0/dist/test.min.js",
            filename="test.min.js",
        )

    def tearDown(self):
        """清理注册的测试资源。"""
        AssetRegistry.unregister("TestLib")

    def test_download_success(self):
        """覆盖 L139, 145: 成功下载并写入本地文件。"""
        fake_content = b"console.log('hello');"
        mock_response = MagicMock()
        mock_response.read.return_value = fake_content
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch(
                "urllib.request.urlopen",
                return_value=mock_response,
            ):
                result = install_assets(
                    target_dir=tmp_dir,
                    libs=["TestLib"],
                    use_cache=False,
                )

            self.assertIn("TestLib", result)
            import os

            local_path = result["TestLib"]
            self.assertTrue(os.path.exists(local_path))
            with open(local_path, "rb") as f:
                self.assertEqual(f.read(), fake_content)

    def test_download_failure_raises_error(self):
        """覆盖 L180-181: 下载失败时抛出 OfflineInstallError。"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch(
                "urllib.request.urlopen",
                side_effect=ConnectionError("Network unreachable"),
            ):
                with self.assertRaises(OfflineInstallError) as ctx:
                    install_assets(
                        target_dir=tmp_dir,
                        libs=["TestLib"],
                        use_cache=False,
                    )
                self.assertIn("Failed to download", str(ctx.exception))
                self.assertIn("TestLib", str(ctx.exception))

    def test_download_with_version_override(self):
        """测试 version_map 版本覆盖功能。"""
        fake_content = b"console.log('v2');"
        mock_response = MagicMock()
        mock_response.read.return_value = fake_content
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch(
                "urllib.request.urlopen",
                return_value=mock_response,
            ) as mock_urlopen:
                result = install_assets(
                    target_dir=tmp_dir,
                    libs=["TestLib"],
                    version_map={"TestLib": "2.0.0"},
                    use_cache=False,
                )

            self.assertIn("TestLib", result)
            called_url = mock_urlopen.call_args[0][0]
            self.assertIn("@2.0.0", called_url)

    def test_cache_hit_skips_download(self):
        """测试缓存命中时跳过下载。"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            import os

            # 预先创建缓存文件
            cache_file = os.path.join(tmp_dir, "test.min.js")
            with open(cache_file, "w") as f:
                f.write("cached")

            with patch(
                "urllib.request.urlopen",
            ) as mock_urlopen:
                result = install_assets(
                    target_dir=tmp_dir,
                    libs=["TestLib"],
                    use_cache=True,
                )
                mock_urlopen.assert_not_called()
            self.assertIn("TestLib", result)

    def test_unregistered_lib_raises_error(self):
        """测试未注册的库名抛出 OfflineInstallError。"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with self.assertRaises(OfflineInstallError) as ctx:
                install_assets(
                    target_dir=tmp_dir,
                    libs=["NonExistentLib"],
                )
            self.assertIn("not registered", str(ctx.exception))

    def test_default_target_dir(self):
        """覆盖 L139: target_dir=None 使用默认路径。"""
        import os

        fake_content = b"console.log('default');"
        mock_response = MagicMock()
        mock_response.read.return_value = fake_content
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        # 用 normpath 规范化为当前平台的分隔符，避免在 Windows 上
        # "C:\\Users\\x/.pyantv/assets" 与 "C:\\Users\\x\\.pyantv\\assets\\test.min.js"
        # 因混合分隔符导致 assertIn 误判。
        default_dir = os.path.normpath(os.path.expanduser("~/.pyantv/assets"))

        with patch(
            "urllib.request.urlopen",
            return_value=mock_response,
        ):
            result = install_assets(
                target_dir=None,
                libs=["TestLib"],
                use_cache=False,
            )

        self.assertIn("TestLib", result)
        self.assertIn(default_dir, os.path.normpath(result["TestLib"]))
        # 清理下载的文件
        downloaded_file = result["TestLib"]
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)

    def test_default_libs_list(self):
        """覆盖 L145: libs=None 使用所有注册库。"""
        fake_content = b"console.log('all');"
        mock_response = MagicMock()
        mock_response.read.return_value = fake_content
        mock_response.__enter__ = MagicMock(return_value=mock_response)
        mock_response.__exit__ = MagicMock(return_value=False)

        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch(
                "urllib.request.urlopen",
                return_value=mock_response,
            ):
                result = install_assets(
                    target_dir=tmp_dir,
                    libs=None,
                    use_cache=False,
                )
        # libs=None 时应下载所有已注册库，至少包含 TestLib
        self.assertIn("TestLib", result)

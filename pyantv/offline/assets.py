"""离线资源管理与私有化部署支持。

本模块提供 AntV 前端资源的离线下载、注册和 host 管理功能，
支持私有化部署场景。
"""
import os
from pathlib import Path
from typing import ClassVar, Dict, List, Optional

from ..globals import CurrentConfig


class OfflineInstallError(Exception):
    """离线资源安装失败异常。"""


class AssetEntry:
    """AntV 资源条目，包含版本、CDN URL、文件名、校验和等元数据。"""

    def __init__(
        self,
        name: str,
        version: str,
        cdn_url: str,
        filename: str,
        sri_hash: Optional[str] = None,
    ):
        """初始化资源条目。

        :param name: 资源名称（如 "G2"、"G6"、"L7"）。
        :param version: 资源版本（如 "5.2.11"）。
        :param cdn_url: CDN URL（如 "https://unpkg.com/@antv/g2@5.2.11/dist/g2.min.js"）。
        :param filename: 本地文件名（如 "g2.min.js"）。
        :param sri_hash: SRI 哈希值（可选）。
        """
        self._name = name
        self._version = version
        self._cdn_url = cdn_url
        self._filename = filename
        self._sri_hash = sri_hash

    @property
    def name(self) -> str:
        """资源名称。"""
        return self._name

    @property
    def version(self) -> str:
        """资源版本。"""
        return self._version

    @property
    def cdn_url(self) -> str:
        """CDN URL。"""
        return self._cdn_url

    @property
    def filename(self) -> str:
        """本地文件名。"""
        return self._filename

    @property
    def sri_hash(self) -> Optional[str]:
        """SRI 哈希值。"""
        return self._sri_hash


class AssetRegistry:
    """AntV 资源注册表，管理各库的版本和 CDN URL。"""

    _registry: ClassVar[Dict[str, AssetEntry]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        version: str,
        cdn_url: str,
        filename: str,
        sri_hash: Optional[str] = None,
    ) -> None:
        """注册 AntV 资源。

        :param name: 资源名称。
        :param version: 资源版本。
        :param cdn_url: CDN URL。
        :param filename: 本地文件名。
        :param sri_hash: SRI 哈希值（可选）。
        """
        cls._registry[name] = AssetEntry(name, version, cdn_url, filename, sri_hash)

    @classmethod
    def get(cls, name: str) -> AssetEntry:
        """获取已注册的资源条目。

        :param name: 资源名称。
        :returns: 资源条目。
        :raises KeyError: 资源未注册时抛出。
        """
        if name not in cls._registry:
            raise KeyError(f"Asset '{name}' not registered")
        return cls._registry[name]

    @classmethod
    def list_registered(cls) -> List[str]:
        """列出所有已注册的资源名称。

        :returns: 资源名称列表。
        """
        return list(cls._registry.keys())

    @classmethod
    def unregister(cls, name: str) -> None:
        """注销资源。

        :param name: 资源名称。
        """
        if name in cls._registry:
            del cls._registry[name]


def install_assets(
    target_dir: Optional[str] = None,
    libs: Optional[List[str]] = None,
    version_map: Optional[Dict[str, str]] = None,
    use_cache: bool = True,
) -> Dict[str, str]:
    """下载指定 AntV 前端资源到本地目录。

    :param target_dir: 目标目录，默认 ``~/.pyantv/assets``。
    :param libs: 要下载的库列表，默认下载所有已注册库。
    :param version_map: 版本覆盖映射，如 ``{"G2": "5.2.0"}``。
    :param use_cache: 是否使用缓存（已存在则跳过），默认 True。
    :returns: ``{lib_name: local_path}`` 映射字典。
    :raises OfflineInstallError: 下载失败时抛出。
    """
    # 确定目标目录
    if target_dir is None:
        target_dir = os.path.expanduser("~/.pyantv/assets")
    target_path = Path(target_dir)
    target_path.mkdir(parents=True, exist_ok=True)

    # 确定要下载的库列表
    if libs is None:
        libs = AssetRegistry.list_registered()

    # 准备结果字典
    result: Dict[str, str] = {}

    # 下载每个库
    for lib_name in libs:
        try:
            entry = AssetRegistry.get(lib_name)
        except KeyError:
            raise OfflineInstallError(f"Asset '{lib_name}' not registered")

        # 应用版本覆盖
        cdn_url = entry.cdn_url
        if version_map and lib_name in version_map:
            new_version = version_map[lib_name]
            # 替换 URL 中的版本号
            cdn_url = cdn_url.replace(f"@{entry.version}", f"@{new_version}")

        # 确定本地文件路径
        local_file = target_path / entry.filename

        # 检查缓存
        if use_cache and local_file.exists():
            result[lib_name] = str(local_file)
            continue

        # 下载文件
        try:
            import urllib.request

            with urllib.request.urlopen(cdn_url) as response:
                content = response.read()
            local_file.write_bytes(content)
            result[lib_name] = str(local_file)
        except Exception as e:
            raise OfflineInstallError(f"Failed to download {lib_name}: {e}")

    return result


def set_offline_host(host: str) -> None:
    """设置离线 host，优先于 ONLINE_HOST 使用。

    :param host: 离线 host URL，支持 ``file://`` 协议。
    """
    CurrentConfig.OFFLINE_HOST = host


def get_active_host() -> str:
    """获取当前应使用的 host。

    优先级：OFFLINE_HOST > 环境变量 PYANTV_OFFLINE_HOST > ONLINE_HOST。

    :returns: 当前 host URL。
    """
    # 优先级 1: 程序设置的 OFFLINE_HOST
    if CurrentConfig.OFFLINE_HOST:
        return CurrentConfig.OFFLINE_HOST

    # 优先级 2: 环境变量 PYANTV_OFFLINE_HOST（每次调用时读取，不缓存）
    env_host = os.environ.get("PYANTV_OFFLINE_HOST")
    if env_host:
        return env_host

    # 优先级 3: 默认 ONLINE_HOST
    return CurrentConfig.ONLINE_HOST


# 注册默认资源
def _register_default_assets():
    """注册默认的 AntV 资源。"""
    # G2 5.2.11（已验证版本）
    AssetRegistry.register(
        name="G2",
        version="5.2.11",
        cdn_url="https://unpkg.com/@antv/g2@5.2.11/dist/g2.min.js",
        filename="g2.min.js",
    )
    # G6 5.0.51（占位注册）
    AssetRegistry.register(
        name="G6",
        version="5.0.51",
        cdn_url="https://unpkg.com/@antv/g6@5.0.51/dist/g6.min.js",
        filename="g6.min.js",
    )
    # L7 2.22.1（占位注册）
    AssetRegistry.register(
        name="L7",
        version="2.22.1",
        cdn_url="https://unpkg.com/@antv/l7@2.22.1/dist/l7.js",
        filename="l7.js",
    )


# 模块加载时注册默认资源
_register_default_assets()

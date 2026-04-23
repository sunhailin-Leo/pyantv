"""离线资源管理与私有化部署支持。

本模块提供 AntV 前端资源的离线下载、注册和 host 管理功能，
支持私有化部署场景。

示例:
    >>> from pyantv.offline import (
    ...     AssetRegistry, install_assets,
    ...     set_offline_host, get_active_host,
    ... )
    >>>
    >>> # 查看已注册的资源
    >>> AssetRegistry.list_registered()
    ['G2', 'G6', 'L7']
    >>>
    >>> # 下载资源到本地
    >>> install_assets(target_dir="./assets", libs=["G2"])
    {'G2': './assets/g2.min.js'}
    >>>
    >>> # 设置离线 host
    >>> set_offline_host("file:///path/to/assets")
    >>>
    >>> # 获取当前生效的 host
    >>> get_active_host()
    'file:///path/to/assets'
"""
from pyantv.offline.assets import (
    AssetEntry,
    AssetRegistry,
    OfflineInstallError,
    get_active_host,
    install_assets,
    set_offline_host,
)

__all__ = [
    "AssetEntry",
    "AssetRegistry",
    "OfflineInstallError",
    "install_assets",
    "set_offline_host",
    "get_active_host",
]

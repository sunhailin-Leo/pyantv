"""
Internationalization (i18n) module for pyantv.
Supports multiple languages for UI text translations.
"""

from typing import Dict, Optional

# Supported locales
SUPPORTED_LOCALES = ["zh-CN", "en-US", "ja-JP"]

# Default locale
_DEFAULT_LOCALE = "zh-CN"

# Language packs
_LOCALE_DATA: Dict[str, Dict[str, str]] = {
    "zh-CN": {
        "loading": "加载中...",
        "no_data": "暂无数据",
        "reset": "重置",
        "export_image": "导出图片",
        "export_data": "导出数据",
        "total": "总计",
        "average": "平均",
        "max": "最大",
        "min": "最小",
        "count": "计数",
        "sum": "求和",
        "zoom_in": "放大",
        "zoom_out": "缩小",
        "scroll_left": "向左滚动",
        "scroll_right": "向右滚动",
    },
    "en-US": {
        "loading": "Loading...",
        "no_data": "No Data",
        "reset": "Reset",
        "export_image": "Export Image",
        "export_data": "Export Data",
        "total": "Total",
        "average": "Average",
        "max": "Max",
        "min": "Min",
        "count": "Count",
        "sum": "Sum",
        "zoom_in": "Zoom In",
        "zoom_out": "Zoom Out",
        "scroll_left": "Scroll Left",
        "scroll_right": "Scroll Right",
    },
    "ja-JP": {
        "loading": "読み込み中...",
        "no_data": "データなし",
        "reset": "リセット",
        "export_image": "画像をエクスポート",
        "export_data": "データをエクスポート",
        "total": "合計",
        "average": "平均",
        "max": "最大",
        "min": "最小",
        "count": "カウント",
        "sum": "合計",
        "zoom_in": "ズームイン",
        "zoom_out": "ズームアウト",
        "scroll_left": "左へスクロール",
        "scroll_right": "右へスクロール",
    },
}

# Current locale
_current_locale: str = _DEFAULT_LOCALE


def set_locale(locale: str) -> None:
    """
    Set the global locale for the application.

    Args:
        locale: Locale string (e.g., 'zh-CN', 'en-US', 'ja-JP')

    Raises:
        ValueError: If locale is not supported
    """
    if locale not in _LOCALE_DATA and locale not in SUPPORTED_LOCALES:
        raise ValueError(
            f"Locale '{locale}' is not supported. "
            f"Supported locales: {SUPPORTED_LOCALES}"
        )
    global _current_locale
    _current_locale = locale


def get_locale() -> str:
    """
    Get the current locale.

    Returns:
        Current locale string
    """
    return _current_locale


def get_text(key: str, locale: Optional[str] = None) -> str:
    """
    Get translated text for the given key.

    Args:
        key: Translation key
        locale: Optional locale string. If None, uses current locale

    Returns:
        Translated text, or the key itself if not found
    """
    target_locale = locale if locale is not None else _current_locale
    locale_dict = _LOCALE_DATA.get(target_locale, {})
    return locale_dict.get(key, key)


def register_locale(locale: str, data: Dict[str, str]) -> None:
    """
    Register a custom locale or update an existing one.

    Args:
        locale: Locale string (e.g., 'fr-FR')
        data: Dictionary of translation key-value pairs
    """
    _LOCALE_DATA[locale] = data
    if locale not in SUPPORTED_LOCALES:
        SUPPORTED_LOCALES.append(locale)

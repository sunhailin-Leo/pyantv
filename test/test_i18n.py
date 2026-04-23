"""
Tests for the i18n module.
"""

import pytest
from pyantv.i18n import set_locale, get_locale, get_text, register_locale


def test_default_locale_is_zh_cn():
    """Test that the default locale is zh-CN."""
    set_locale("zh-CN")
    assert get_locale() == "zh-CN"


def test_set_locale_en_us():
    """Test setting locale to en-US."""
    set_locale("en-US")
    assert get_locale() == "en-US"


def test_set_locale_ja_jp():
    """Test setting locale to ja-JP."""
    set_locale("ja-JP")
    assert get_locale() == "ja-JP"


def test_set_locale_invalid_raises():
    """Test that setting an invalid locale raises ValueError."""
    set_locale("zh-CN")
    with pytest.raises(ValueError):
        set_locale("invalid-locale")


def test_get_text_zh_cn():
    """Test getting text in zh-CN."""
    set_locale("zh-CN")
    assert get_text("loading") == "加载中..."
    assert get_text("no_data") == "暂无数据"


def test_get_text_en_us():
    """Test getting text in en-US."""
    set_locale("en-US")
    assert get_text("loading") == "Loading..."
    assert get_text("no_data") == "No Data"


def test_get_text_ja_jp():
    """Test getting text in ja-JP."""
    set_locale("ja-JP")
    assert get_text("loading") == "読み込み中..."
    assert get_text("no_data") == "データなし"


def test_get_text_missing_key():
    """Test getting text for a missing key returns the key itself."""
    set_locale("zh-CN")
    assert get_text("nonexistent_key") == "nonexistent_key"


def test_get_text_with_locale_param():
    """Test getting text with explicit locale parameter."""
    set_locale("zh-CN")
    assert get_text("loading", "en-US") == "Loading..."
    assert get_locale() == "zh-CN"


def test_register_locale():
    """Test registering a custom locale."""
    custom_data = {
        "loading": "Chargement...",
        "no_data": "Pas de données",
    }
    register_locale("fr-FR", custom_data)
    set_locale("fr-FR")
    assert get_locale() == "fr-FR"
    assert get_text("loading") == "Chargement..."

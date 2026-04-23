"""JSON Snapshot 测试工具函数。

提供快照生成、对比、更新机制，用于验证 pyantv 图表的 JSON 配置
与预期基准完全一致。

使用方式：
    # 正常测试模式（对比快照）
    pytest test/test_snapshots.py

    # 更新快照模式（生成/覆盖快照文件）
    UPDATE_SNAPSHOTS=1 pytest test/test_snapshots.py
"""

import json
import os
from pathlib import Path

SNAPSHOT_DIR = Path(__file__).parent / "snapshots"


def _should_update_snapshots() -> bool:
    """检查是否处于快照更新模式。"""
    return os.environ.get("UPDATE_SNAPSHOTS", "").strip() in ("1", "true", "yes")


def _normalize_for_comparison(data):
    """递归规范化数据，确保对比时忽略 key 顺序。

    将 dict 的 key 排序，确保 JSON 序列化后的字符串一致。
    """
    if isinstance(data, dict):
        return {k: _normalize_for_comparison(v) for k, v in sorted(data.items())}
    if isinstance(data, list):
        return [_normalize_for_comparison(item) for item in data]
    return data


def _diff_dicts(actual, expected, path="") -> list:
    """递归对比两个字典，返回差异列表。"""
    diffs = []

    if type(actual) is not type(expected):
        diffs.append(
            f"  {path or 'root'}: type mismatch - "
            f"actual={type(actual).__name__}, expected={type(expected).__name__}"
        )
        return diffs

    if isinstance(actual, dict):
        all_keys = set(actual.keys()) | set(expected.keys())
        for key in sorted(all_keys):
            child_path = f"{path}.{key}" if path else key
            if key not in actual:
                diffs.append(f"  {child_path}: MISSING in actual")
            elif key not in expected:
                diffs.append(f"  {child_path}: EXTRA in actual = {actual[key]!r}")
            else:
                diffs.extend(_diff_dicts(actual[key], expected[key], child_path))
    elif isinstance(actual, list):
        if len(actual) != len(expected):
            diffs.append(
                f"  {path}: list length mismatch - "
                f"actual={len(actual)}, expected={len(expected)}"
            )
        for i, (actual_item, expected_item) in enumerate(zip(actual, expected)):
            diffs.extend(_diff_dicts(actual_item, expected_item, f"{path}[{i}]"))
    elif actual != expected:
        diffs.append(
            f"  {path}: value mismatch - actual={actual!r}, expected={expected!r}"
        )

    return diffs


def assert_snapshot_match(chart, snapshot_name: str) -> None:
    """对比图表的 dump_options() 输出与快照文件。

    Args:
        chart: pyantv 图表实例
        snapshot_name: 快照文件名（不含 .json 后缀）

    Raises:
        AssertionError: 当快照不匹配时
        FileNotFoundError: 当快照文件不存在且非更新模式时
    """
    json_str = chart.dump_options()
    actual = json.loads(json_str)

    snapshot_path = SNAPSHOT_DIR / f"{snapshot_name}.json"

    if _should_update_snapshots():
        SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
        normalized = _normalize_for_comparison(actual)
        with open(snapshot_path, "w", encoding="utf-8") as file:
            json.dump(normalized, file, indent=2, ensure_ascii=False)
        return

    if not snapshot_path.exists():
        raise FileNotFoundError(
            f"Snapshot file not found: {snapshot_path}\n"
            f"Run with UPDATE_SNAPSHOTS=1 to generate it."
        )

    with open(snapshot_path, "r", encoding="utf-8") as file:
        expected = json.load(file)

    actual_normalized = _normalize_for_comparison(actual)
    expected_normalized = _normalize_for_comparison(expected)

    if actual_normalized != expected_normalized:
        diffs = _diff_dicts(actual_normalized, expected_normalized)
        diff_text = "\n".join(diffs[:20])
        total = len(diffs)
        suffix = f"\n  ... and {total - 20} more" if total > 20 else ""
        raise AssertionError(
            f"Snapshot mismatch for '{snapshot_name}':\n"
            f"{diff_text}{suffix}\n\n"
            f"Run with UPDATE_SNAPSHOTS=1 to update the snapshot."
        )

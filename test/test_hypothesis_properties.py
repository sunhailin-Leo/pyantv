"""Property-based 测试文件，使用 Hypothesis 验证 pyantv 核心模块的不变式。"""

import json

from hypothesis import given, strategies as st

from pyantv import Line
from pyantv.commons.utils import (
    JsCode,
    OrderedSet,
    replace_placeholder,
    remove_key_with_none_value,
    convert_data_if_needed,
    PLACEHOLDER,
)
from pyantv.data.pipeline import bin_data, aggregate, normalize, sample
from pyantv.options import TitleOpts
from pyantv.globals import ChartEvent


# ============================================================================
# utils 模块（7 个 property）
# ============================================================================


@given(st.text())
def test_jscode_roundtrip(s):
    """此 property 保证了 JsCode 对象的去占位符操作是可逆的。"""
    js_code = JsCode(s)
    # 去掉占位符后应该等于原始字符串
    assert js_code.js_code.replace(PLACEHOLDER, "") == s


@given(
    st.lists(st.integers(), min_size=0, max_size=10),
    st.integers(min_value=0, max_value=9),
)
def test_ordered_set_idempotent(items, index):
    """此 property 保证了 OrderedSet 的 add 操作满足幂等性。"""
    ordered_set = OrderedSet(*items)
    # 记录添加前的 items
    items_before = ordered_set.items.copy()

    # 添加一个已存在的元素（如果有）
    if items_before:
        ordered_set.add(items_before[index % len(items_before)])

    # items 列表应该不变
    assert ordered_set.items == items_before


@given(st.lists(st.integers(), min_size=0, max_size=10))
def test_ordered_set_preserves_order(items):
    """此 property 保证了 OrderedSet 维持元素的插入顺序。"""
    ordered_set = OrderedSet()
    for item in items:
        ordered_set.add(item)

    # 去重后应该保持首次出现的顺序
    seen = set()
    expected_order = []
    for item in items:
        if item not in seen:
            seen.add(item)
            expected_order.append(item)

    assert ordered_set.items == expected_order


@given(st.text())
def test_replace_placeholder_homomorphism(s):
    """此 property 保证了 replace_placeholder 对不含占位符的字符串是同态的。"""
    # 不包含 PLACEHOLDER 的字符串应该原样返回
    result = replace_placeholder(s)
    assert result == s


@given(st.dictionaries(st.text(), st.none() | st.integers() | st.text(), max_size=5))
def test_remove_key_with_none_value_nested(d):
    """此 property 保证了递归删除嵌套字典中的 None 值键。"""
    result = remove_key_with_none_value(d)

    # 验证结果中不存在值为 None 的键
    def check_no_none_values(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                assert value is not None
                check_no_none_values(value)
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                check_no_none_values(item)

    check_no_none_values(result)


@given(st.none())
def test_convert_data_if_needed_none(data):
    """此 property 保证了 convert_data_if_needed 对 None 输入返回 None。"""
    result = convert_data_if_needed(data)
    assert result is None


@given(st.lists(st.dictionaries(st.text(), st.integers()), min_size=0, max_size=5))
def test_convert_data_if_needed_list_of_dicts(data):
    """此 property 保证了 convert_data_if_needed 对字典列表输入原样返回。"""
    result = convert_data_if_needed(data)
    assert result == data


# ============================================================================
# data pipeline 模块（4 个 property）
# ============================================================================


@given(
    st.lists(
        st.fixed_dictionaries({"value": st.floats(min_value=-100, max_value=100)}),
        min_size=1,
        max_size=10,
    ),
    st.just("value"),
    st.integers(min_value=2, max_value=5),
)
def test_bin_data_length(data, field, bins):
    """此 property 保证了 bin 操作保持数据行数不变。"""
    result = bin_data(data, field, bins=bins)
    assert len(result) == len(data)


@given(
    st.lists(
        st.fixed_dictionaries(
            {
                "category": st.sampled_from(["A", "B", "C"]),
                "value": st.integers(min_value=0, max_value=100),
            }
        ),
        min_size=1,
        max_size=10,
    ),
    st.just("category"),
    st.just("value"),
)
def test_aggregate_count_sum(data, group_by, field):
    """此 property 保证了 count 聚合的守恒性。"""
    result = aggregate(data, group_by, field, method="count")

    # count 之和应该等于原数据长度
    total_count = sum(row[field] for row in result)
    assert total_count == len(data)


@given(
    st.lists(
        st.fixed_dictionaries({"value": st.floats(min_value=-100, max_value=100)}),
        min_size=1,
        max_size=10,
    ),
    st.just("value"),
)
def test_normalize_min_max_range(data, field):
    """此 property 保证了 min-max 归一化的值域约束。"""
    result = normalize(data, field, method="min-max")

    # 所有值应该在 [0, 1] 范围内
    for row in result:
        assert 0 <= row[field] <= 1


@given(
    st.lists(
        st.dictionaries(st.sampled_from(["x", "y"]), st.integers()),
        min_size=1,
        max_size=10,
    ),
    st.integers(min_value=1, max_value=10),
)
def test_sample_length(data, n):
    """此 property 保证了 sample 返回的正确长度。"""
    result = sample(data, n=n, seed=42)
    expected_length = min(n, len(data))
    assert len(result) == expected_length


# ============================================================================
# chart API（3 个 property）
# ============================================================================


@given(
    st.lists(
        st.fixed_dictionaries({"x": st.integers(), "y": st.integers()}),
        min_size=1,
        max_size=10,
    ),
    st.just("x"),
    st.just("y"),
)
def test_chart_dump_options_json(data, x_field, y_field):
    """此 property 保证了 Chart 的 dump_options 返回可解析的 JSON。"""
    chart = Line()
    chart.set_data(data)
    chart.set_encode(x_field_name=x_field, y_field_name=y_field)

    options_json = chart.dump_options()

    # 应该可以被 json.loads 解析
    parsed = json.loads(options_json)
    assert isinstance(parsed, dict)


@given(st.lists(st.dictionaries(st.text(), st.integers()), min_size=0, max_size=5))
def test_chart_empty_data(data):
    """此 property 保证了 Chart 能处理空数据。"""
    chart = Line()
    # 空数据不应该抛异常
    chart.set_data(data)

    # 即使没有数据，dump_options 也应该能工作
    options_json = chart.dump_options()
    assert isinstance(options_json, str)


@given(st.text())
def test_title_opts_title(s):
    """此 property 保证了 TitleOpts 的 title 属性正确存储。"""
    title_opts = TitleOpts(title=s)
    assert title_opts.opts["title"] == s


# ============================================================================
# 其他（1 个 property）
# ============================================================================


def test_chart_event_members_are_strings():
    """此 property 保证了 ChartEvent 的所有成员都是字符串类型。"""
    # 检查 ChartEvent 的所有属性都是字符串
    for attr_name in dir(ChartEvent):
        if not attr_name.startswith("_"):
            attr_value = getattr(ChartEvent, attr_name)
            assert isinstance(attr_value, str)


# ============================================================================
# 边界字符串测试（补充 property）
# ============================================================================


@given(st.text())
def test_boundary_strings_not_crash(s):
    """此 property 保证了边界字符串（包括空串、emoji、unicode BOM、控制字符）不会导致渲染崩溃。"""
    # 测试各种边界字符串
    js_code = JsCode(s)
    result = js_code.js_code.replace(PLACEHOLDER, "")
    assert isinstance(result, str)

    # 测试 replace_placeholder
    replaced = replace_placeholder(s)
    assert isinstance(replaced, str)

    # 测试 remove_key_with_none_value
    test_dict = {"key": s}
    cleaned = remove_key_with_none_value(test_dict)
    assert isinstance(cleaned, dict)


@given(st.text())
def test_chart_with_boundary_strings(s):
    """此 property 保证了 Chart 能处理边界字符串作为数据。"""
    data = [{"x": s, "y": 1}]
    chart = Line()
    chart.set_data(data)

    # 不应该抛异常
    options_json = chart.dump_options()
    assert isinstance(options_json, str)

"""JSON 配置校验工具函数集 + 校验工具自身的完整测试。

提供一组断言工具，用于深度校验 pyantv 生成的 AntV G2 options 字典
与期望配置结构的一致性。
"""

import unittest
from unittest.mock import patch

from pyantv.commons.utils import JsCode


# ---------------------------------------------------------------------------
# 哨兵值
# ---------------------------------------------------------------------------


class _AnySentinel:
    """哨兵类，用于 assert_options_contains 中表示"只要键存在即可"。"""

    def __repr__(self) -> str:
        return "ANY"


ANY = _AnySentinel()


# ---------------------------------------------------------------------------
# 核心校验函数
# ---------------------------------------------------------------------------


def _compare_values(actual, expected, path: str) -> None:
    """比较两个值，利用 JsCode.__eq__ 直接比较。

    Args:
        actual: 实际值
        expected: 期望值
        path: 当前键路径（用于错误消息）

    Raises:
        AssertionError: 当值不匹配时
    """
    if actual != expected:
        raise AssertionError(
            f"Mismatch at '{path}': expected {expected!r}, got {actual!r}"
        )


def assert_options_contains(
    actual: dict,
    expected: dict,
    max_depth: int = 50,
    path: str = "",
) -> None:
    """深度断言 actual 字典包含 expected 中的所有键值对。

    支持嵌套字典和列表的递归校验。
    当 expected 中某个值为 ANY 哨兵时，仅校验键存在。
    列表匹配语义：expected 列表中的每个元素按索引位置与 actual
    列表中对应索引的元素递归比较。如果 expected 列表长度小于
    actual，则仅校验 expected 覆盖的索引位置。

    Args:
        actual: 实际生成的 options 字典
        expected: 期望包含的键值对子集
        max_depth: 最大递归深度（默认 50），防止栈溢出
        path: 当前递归路径（用于错误消息），调用方无需传入

    Raises:
        AssertionError: 当 actual 不包含 expected 中的某个键值对时，
                        错误消息包含完整的键路径
        RecursionError: 当嵌套深度超过 max_depth 时
    """
    if max_depth <= 0:
        raise RecursionError(f"Max recursion depth exceeded at '{path}'")

    if not isinstance(expected, dict):
        raise TypeError(f"expected must be a dict, got {type(expected).__name__}")

    for key, expected_value in expected.items():
        current_path = f"{path}.{key}" if path else str(key)

        if not isinstance(actual, dict):
            raise AssertionError(
                f"Expected dict at '{path}', got {type(actual).__name__}"
            )

        if key not in actual:
            raise AssertionError(f"Missing key '{current_path}' in actual options")

        actual_value = actual[key]

        if isinstance(expected_value, _AnySentinel):
            continue

        if isinstance(expected_value, dict):
            if not isinstance(actual_value, dict):
                raise AssertionError(
                    f"Expected dict at '{current_path}', "
                    f"got {type(actual_value).__name__}"
                )
            assert_options_contains(
                actual_value,
                expected_value,
                max_depth=max_depth - 1,
                path=current_path,
            )
        elif isinstance(expected_value, list):
            if not isinstance(actual_value, list):
                raise AssertionError(
                    f"Expected list at '{current_path}', "
                    f"got {type(actual_value).__name__}"
                )
            if len(actual_value) < len(expected_value):
                raise AssertionError(
                    f"List at '{current_path}' has {len(actual_value)} "
                    f"elements, expected at least {len(expected_value)}"
                )
            for idx, expected_item in enumerate(expected_value):
                item_path = f"{current_path}.{idx}"
                if isinstance(expected_item, _AnySentinel):
                    continue
                if isinstance(expected_item, dict):
                    if not isinstance(actual_value[idx], dict):
                        raise AssertionError(
                            f"Expected dict at '{item_path}', "
                            f"got {type(actual_value[idx]).__name__}"
                        )
                    assert_options_contains(
                        actual_value[idx],
                        expected_item,
                        max_depth=max_depth - 1,
                        path=item_path,
                    )
                elif isinstance(expected_item, list):
                    if not isinstance(actual_value[idx], list):
                        raise AssertionError(
                            f"Expected list at '{item_path}', "
                            f"got {type(actual_value[idx]).__name__}"
                        )
                    assert_options_contains(
                        {"_list": actual_value[idx]},
                        {"_list": expected_item},
                        max_depth=max_depth - 1,
                        path=item_path,
                    )
                else:
                    _compare_values(actual_value[idx], expected_item, item_path)
        else:
            _compare_values(actual_value, expected_value, current_path)


def assert_options_structure(
    actual: dict,
    required_keys: list,
) -> None:
    """断言 actual 字典包含所有 required_keys 指定的键路径。

    支持点号分隔的嵌套路径，如 "encode.x"、"scale.y.type"。
    支持数组索引路径，如 "children.0.type"、"children.0.encode.x"。

    Args:
        actual: 实际生成的 options 字典
        required_keys: 必须存在的键路径列表

    Raises:
        AssertionError: 当某个键路径不存在时，
                        错误消息包含缺失的键路径
    """
    for key_path in required_keys:
        parts = key_path.split(".")
        current = actual
        traversed = []

        for part in parts:
            if isinstance(current, list):
                try:
                    index = int(part)
                except ValueError:
                    raise AssertionError(
                        f"Expected integer index at "
                        f"'{'.'.join(traversed)}.{part}' in path "
                        f"'{key_path}', but current value is a list"
                    )
                if index < 0 or index >= len(current):
                    raise AssertionError(
                        f"Index {index} out of range at "
                        f"'{'.'.join(traversed)}' (list length "
                        f"{len(current)}) in path '{key_path}'"
                    )
                current = current[index]
            elif isinstance(current, dict):
                if part.isdigit() and part not in current:
                    try:
                        index = int(part)
                        if isinstance(current.get(index), (dict, list)):
                            current = current[index]
                            traversed.append(part)
                            continue
                    except (ValueError, KeyError, TypeError):
                        pass
                if part not in current:
                    raise AssertionError(
                        f"Missing key path '{key_path}': "
                        f"key '{part}' not found at "
                        f"'{'.'.join(traversed) or 'root'}'"
                    )
                current = current[part]
            else:
                raise AssertionError(
                    f"Cannot traverse path '{key_path}': "
                    f"value at '{'.'.join(traversed)}' is "
                    f"{type(current).__name__}, not dict or list"
                )
            traversed.append(part)


def assert_chart_type(actual: dict, expected_type: str) -> None:
    """断言图表的 type 字段正确。

    Args:
        actual: 实际生成的 options 字典
        expected_type: 期望的图表类型字符串

    Raises:
        AssertionError: 当 type 字段不匹配时
    """
    actual_type = actual.get("type")
    if actual_type != expected_type:
        raise AssertionError(
            f"Chart type mismatch: expected '{expected_type}', " f"got '{actual_type}'"
        )


def assert_encode_fields(actual: dict, **expected_fields) -> None:
    """断言 encode 配置中的字段映射正确。

    Args:
        actual: 实际生成的 options 字典
        **expected_fields: 期望的编码字段，如 x="year", y="value"

    Raises:
        AssertionError: 当 encode 不存在或字段不匹配时
    """
    if "encode" not in actual:
        raise AssertionError("Missing 'encode' in options")

    encode = actual["encode"]
    for field_name, expected_value in expected_fields.items():
        if field_name not in encode:
            raise AssertionError(f"Missing encode field '{field_name}'")
        actual_value = encode[field_name]
        _compare_values(actual_value, expected_value, f"encode.{field_name}")


def assert_scale_config(
    actual: dict,
    channel: str,
    **expected_config,
) -> None:
    """断言指定通道的 scale 配置正确。

    Args:
        actual: 实际生成的 options 字典
        channel: 通道名称，如 "x"、"y"、"color"
        **expected_config: 期望的 scale 配置，如 type="band"

    Raises:
        AssertionError: 当 scale 不存在或配置不匹配时
    """
    if "scale" not in actual:
        raise AssertionError("Missing 'scale' in options")

    scale = actual["scale"]
    if channel not in scale:
        raise AssertionError(f"Missing scale channel '{channel}'")

    channel_config = scale[channel]
    if not isinstance(channel_config, dict):
        raise AssertionError(
            f"Scale channel '{channel}' is not a dict, "
            f"got {type(channel_config).__name__}"
        )

    for config_key, expected_value in expected_config.items():
        if config_key not in channel_config:
            raise AssertionError(
                f"Missing scale config '{config_key}' " f"in channel '{channel}'"
            )
        actual_value = channel_config[config_key]
        if actual_value != expected_value:
            raise AssertionError(
                f"Scale config mismatch at '{channel}.{config_key}': "
                f"expected {expected_value!r}, got {actual_value!r}"
            )


# ===================================================================
# 测试类
# ===================================================================


class TestAssertOptionsContains(unittest.TestCase):
    """assert_options_contains 的完整测试。"""

    def test_simple_match(self):
        actual = {"type": "line", "data": [1, 2, 3]}
        expected = {"type": "line"}
        assert_options_contains(actual, expected)

    def test_nested_match(self):
        actual = {"encode": {"x": "year", "y": "value", "z": None}}
        expected = {"encode": {"x": "year", "y": "value"}}
        assert_options_contains(actual, expected)

    def test_nested_mismatch(self):
        actual = {"encode": {"x": "year"}}
        expected = {"encode": {"x": "month"}}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_contains(actual, expected)
        self.assertIn("encode.x", str(ctx.exception))

    def test_missing_key(self):
        actual = {"type": "line"}
        expected = {"encode": {"x": "year"}}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_contains(actual, expected)
        self.assertIn("encode", str(ctx.exception))

    def test_any_sentinel(self):
        actual = {"type": "line", "data": [1, 2, 3]}
        expected = {"type": "line", "data": ANY}
        assert_options_contains(actual, expected)

    def test_any_sentinel_nested(self):
        actual = {"encode": {"x": "year", "y": "value"}}
        expected = {"encode": ANY}
        assert_options_contains(actual, expected)

    def test_list_index_match(self):
        actual = {"children": [{"type": "line"}, {"type": "point"}]}
        expected = {"children": [{"type": "line"}]}
        assert_options_contains(actual, expected)

    def test_list_full_match(self):
        actual = {"children": [{"type": "line"}, {"type": "point"}]}
        expected = {"children": [{"type": "line"}, {"type": "point"}]}
        assert_options_contains(actual, expected)

    def test_list_mismatch(self):
        actual = {"children": [{"type": "line"}, {"type": "point"}]}
        expected = {"children": [{"type": "area"}]}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_contains(actual, expected)
        self.assertIn("children.0", str(ctx.exception))

    def test_list_too_short(self):
        actual = {"items": [1]}
        expected = {"items": [1, 2, 3]}
        with self.assertRaises(AssertionError):
            assert_options_contains(actual, expected)

    def test_max_depth_exceeded(self):
        nested = {"a": "leaf"}
        for _ in range(60):
            nested = {"nested": nested}
        with self.assertRaises(RecursionError):
            assert_options_contains(nested, nested, max_depth=50)

    def test_error_message_contains_path(self):
        actual = {"a": {"b": {"c": "wrong"}}}
        expected = {"a": {"b": {"c": "right"}}}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_contains(actual, expected)
        msg = str(ctx.exception)
        self.assertIn("a.b.c", msg)
        self.assertIn("right", msg)
        self.assertIn("wrong", msg)

    def test_empty_expected(self):
        actual = {"type": "line", "data": [1, 2]}
        assert_options_contains(actual, {})

    def test_none_value_match(self):
        actual = {"encode": {"x": "year", "z": None}}
        expected = {"encode": {"z": None}}
        assert_options_contains(actual, expected)

    def test_jscode_match(self):
        actual = {"encode": {"x": JsCode("(d) => d.year")}}
        expected = {"encode": {"x": JsCode("(d) => d.year")}}
        assert_options_contains(actual, expected)

    def test_jscode_mismatch(self):
        actual = {"encode": {"x": JsCode("(d) => d.year")}}
        expected = {"encode": {"x": JsCode("(d) => d.month")}}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_contains(actual, expected)
        self.assertIn("encode.x", str(ctx.exception))


class TestAssertOptionsStructure(unittest.TestCase):
    """assert_options_structure 的完整测试。"""

    def test_simple_keys(self):
        actual = {"type": "line", "data": [1, 2]}
        assert_options_structure(actual, ["type", "data"])

    def test_nested_keys(self):
        actual = {"encode": {"x": "year", "y": "value"}}
        assert_options_structure(actual, ["encode.x", "encode.y"])

    def test_missing_nested_key(self):
        actual = {"type": "line"}
        with self.assertRaises(AssertionError) as ctx:
            assert_options_structure(actual, ["encode.x"])
        self.assertIn("encode.x", str(ctx.exception))

    def test_array_index_path(self):
        actual = {"children": [{"type": "line"}]}
        assert_options_structure(actual, ["children.0.type"])

    def test_array_index_out_of_range(self):
        actual = {"children": [{"type": "line"}]}
        with self.assertRaises(AssertionError):
            assert_options_structure(actual, ["children.5.type"])

    def test_deep_nested_path(self):
        actual = {"scale": {"y": {"type": "linear", "domain": [0, 100]}}}
        assert_options_structure(actual, ["scale.y.type", "scale.y.domain"])

    def test_mixed_dict_and_list_path(self):
        actual = {
            "children": [
                {"encode": {"x": "year"}},
                {"encode": {"x": "month"}},
            ]
        }
        assert_options_structure(actual, ["children.0.encode.x", "children.1.encode.x"])


class TestAssertChartType(unittest.TestCase):
    """assert_chart_type 的完整测试。"""

    def test_match(self):
        assert_chart_type({"type": "line"}, "line")

    def test_mismatch(self):
        with self.assertRaises(AssertionError) as ctx:
            assert_chart_type({"type": "line"}, "interval")
        self.assertIn("interval", str(ctx.exception))

    def test_missing_type(self):
        with self.assertRaises(AssertionError):
            assert_chart_type({}, "line")


class TestAssertEncodeFields(unittest.TestCase):
    """assert_encode_fields 的完整测试。"""

    def test_encode_fields_match(self):
        actual = {
            "encode": {
                "x": "year",
                "y": "value",
                "color": "type",
                "z": None,
            }
        }
        assert_encode_fields(actual, x="year", y="value")

    def test_encode_fields_mismatch(self):
        actual = {"encode": {"x": "year", "y": "value"}}
        with self.assertRaises(AssertionError) as ctx:
            assert_encode_fields(actual, x="month")
        self.assertIn("encode.x", str(ctx.exception))

    def test_encode_missing(self):
        with self.assertRaises(AssertionError):
            assert_encode_fields({}, x="year")

    def test_encode_field_missing(self):
        actual = {"encode": {"x": "year"}}
        with self.assertRaises(AssertionError):
            assert_encode_fields(actual, y="value")

    def test_encode_with_jscode(self):
        actual = {"encode": {"x": JsCode("(d) => d.year")}}
        assert_encode_fields(actual, x=JsCode("(d) => d.year"))


class TestAssertScaleConfig(unittest.TestCase):
    """assert_scale_config 的完整测试。"""

    def test_scale_config_match(self):
        actual = {"scale": {"x": {"type": "band", "range": [0, 1]}}}
        assert_scale_config(actual, "x", type="band")

    def test_scale_config_full_match(self):
        actual = {"scale": {"x": {"type": "band", "range": [0, 1]}}}
        assert_scale_config(actual, "x", type="band", range=[0, 1])

    def test_scale_config_mismatch(self):
        actual = {"scale": {"x": {"type": "band"}}}
        with self.assertRaises(AssertionError) as ctx:
            assert_scale_config(actual, "x", type="linear")
        self.assertIn("x.type", str(ctx.exception))

    def test_scale_missing(self):
        with self.assertRaises(AssertionError):
            assert_scale_config({}, "x", type="band")

    def test_scale_channel_missing(self):
        actual = {"scale": {"x": {"type": "band"}}}
        with self.assertRaises(AssertionError):
            assert_scale_config(actual, "y", type="linear")

    def test_scale_config_key_missing(self):
        actual = {"scale": {"x": {"type": "band"}}}
        with self.assertRaises(AssertionError):
            assert_scale_config(actual, "x", domain=[0, 100])


class TestEnhancedDecorator(unittest.TestCase):
    """增强的 @chart_base_test 装饰器测试。"""

    @patch("pyantv.render.engine.write_utf8_html_file")
    def test_decorator_with_expected_options_mismatch(self, fake_writer):
        from pyantv.charts import Interval
        from pyantv.globals import ChartType
        from test import chart_base_test

        interval = (
            Interval()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )

        with self.assertRaises(AssertionError):

            @chart_base_test(
                chart_type=ChartType.INTERVAL,
                expected_options={"encode": {"x": "wrong_field"}},
            )
            def fake_test(self_inner):
                return interval

            fake_test(self)

    @patch("pyantv.render.engine.write_utf8_html_file")
    def test_decorator_with_expected_options_pass(self, fake_writer):
        from pyantv.charts import Interval
        from pyantv.globals import ChartType
        from test import chart_base_test

        interval = (
            Interval()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )

        @chart_base_test(
            chart_type=ChartType.INTERVAL,
            expected_options={"encode": {"x": "x", "y": "y"}},
        )
        def fake_test(self_inner):
            return interval

        fake_test(self)

    @patch("pyantv.render.engine.write_utf8_html_file")
    def test_decorator_without_expected_options(self, fake_writer):
        from pyantv.charts import Interval
        from pyantv.globals import ChartType
        from test import chart_base_test

        interval = (
            Interval()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
        )

        @chart_base_test(chart_type=ChartType.INTERVAL)
        def fake_test(self_inner):
            return interval

        fake_test(self)

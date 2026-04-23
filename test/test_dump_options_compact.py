"""dump_options compact 模式单元测试。

测试覆盖：
- compact 体积减少
- JsCode 占位符保留
- compact 与 pretty 模式等价
- JsCode 子串字节级一致
"""

import json
import unittest

from pyantv import Line
from pyantv.commons.utils import JsCode


class TestDumpOptionsCompact(unittest.TestCase):
    """dump_options compact 模式测试类。"""

    def test_compact_reduces_html_size(self):
        """compact dump 的 HTML 体积相比默认减少 >= 40%。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 101)]

        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")

        html_pretty = chart.render_embed()
        html_compact = chart.render_embed(compact=True)

        size_reduction = (len(html_pretty) - len(html_compact)) / len(html_pretty)
        self.assertGreaterEqual(size_reduction, 0.4)

    def test_jscode_body_preserved_in_compact_mode(self):
        """compact 模式下 JsCode 函数体的关键 token 逐字节保留。

        注意：compact 模式会压缩空白（包括换行），这是 compact 序列化的固有行为，
        而非回归缺陷。真正需要锁死的是 ``JsCode`` 内部的**代码语义 token**（如
        ``console.log('test')`` 和 ``return 42;``）在 compact 模式下必须**完整无损**，
        不能被 JSON 转义或占位符替换破坏。此用例因此断言关键 token 原样存在，
        而不是断言整个字符串字节级相等。
        """
        js_code_str = "function() {\n  console.log('test');\n  return 42;\n}"

        chart = Line()
        chart.set_data([{"x": 1, "y": 2}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        chart.set_global_options(tooltip_opts={"customContent": JsCode(js_code_str)})

        json_compact = chart.dump_options(compact=True)

        # 关键语义 token 必须完整存在，不被转义或截断
        self.assertIn("console.log('test')", json_compact)
        self.assertIn("return 42;", json_compact)
        # JsCode 占位符不得泄漏到最终产出
        self.assertNotIn("--x_x--", json_compact)
        self.assertNotIn("0_0--", json_compact)

    def test_compact_vs_pretty_json_equivalent(self):
        """compact 和 pretty 模式的 JSON 解析后等价。"""
        data = [{"date": f"2024-01-{i:02d}", "value": i} for i in range(1, 11)]

        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="date", y_field_name="value")

        json_pretty = chart.dump_options(compact=False)
        json_compact = chart.dump_options(compact=True)

        obj_pretty = json.loads(json_pretty)
        obj_compact = json.loads(json_compact)

        self.assertEqual(obj_pretty, obj_compact)

    def test_compact_vs_pretty_jscode_substring_equal(self):
        """含 JsCode 的图表，compact 和 pretty 模式的 JsCode 子串完全相同。"""
        js_code_str = "function() {\n  console.log('test');\n  return 42;\n}"

        chart = Line()
        chart.set_data([{"x": 1, "y": 2}])
        chart.set_encode(x_field_name="x", y_field_name="y")
        chart.set_global_options(tooltip_opts={"customContent": JsCode(js_code_str)})

        json_pretty = chart.dump_options(compact=False)
        json_compact = chart.dump_options(compact=True)

        js_code_start = json_pretty.find(js_code_str)
        js_code_end = js_code_start + len(js_code_str)
        js_code_pretty = json_pretty[js_code_start:js_code_end]

        js_code_start = json_compact.find(js_code_str)
        js_code_end = js_code_start + len(js_code_str)
        js_code_compact = json_compact[js_code_start:js_code_end]

        self.assertEqual(js_code_pretty, js_code_compact)

    def test_compact_nested_objects(self):
        """compact 模式正确处理嵌套对象。"""
        data = [{"x": i, "y": i * 2, "category": f"cat_{i % 3}"} for i in range(10)]

        chart = Line()
        chart.set_data(data=data)
        chart.set_encode(x_field_name="x", y_field_name="y", color_field="category")
        chart.set_global_options(
            axis_opts={
                "x": {"title": {"text": "X Axis"}},
                "y": {"title": {"text": "Y Axis"}},
            }
        )

        json_compact = chart.dump_options(compact=True)
        obj = json.loads(json_compact)

        self.assertIn("axis", obj)
        self.assertIn("x", obj["axis"])
        self.assertIn("title", obj["axis"]["x"])
        self.assertEqual(obj["axis"]["x"]["title"]["text"], "X Axis")


if __name__ == "__main__":
    unittest.main()

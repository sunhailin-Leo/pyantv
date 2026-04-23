import sys
from unittest.mock import patch

from pyantv.charts.chart import Base


class ConsoleOutputRedirect:
    """Wrapper to redirect stdout or stderr"""

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirect = ConsoleOutputRedirect(sys.stdout)


def chart_base_test(chart_type: str, expected_options: dict = None):
    """增强的图表基础测试装饰器。

    向后兼容：expected_options 默认为 None，此时行为与原版完全一致。
    当传入 expected_options 时，额外调用 assert_options_contains 进行
    深度校验。

    Args:
        chart_type: 期望的图表类型（位置参数，与现有 30+ 调用兼容）
        expected_options: 可选关键字参数，期望的 options 子集（深度校验）
    """

    def decorator(test_func):

        @patch("pyantv.render.engine.write_utf8_html_file")
        def wrapper(self, fake_writer):
            chart: Base = test_func(self)
            chart.render()
            _, content = fake_writer.call_args[0]

            self.assertGreater(len(content), 500)
            self.assertEqual(chart.options.get("type"), chart_type)

            if expected_options is not None:
                from test.test_helpers import assert_options_contains

                assert_options_contains(chart.options, expected_options)

            return None

        return wrapper

    return decorator

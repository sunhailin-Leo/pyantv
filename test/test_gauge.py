"""Gauge 仪表盘基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Gauge
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
)


class TestGaugeChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.GAUGE)
    def test_gauge_base(self):
        c = (
            Gauge(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
            )
            .set_data(
                data={
                    "value": {
                        "target": 120,
                        "total": 400,
                        "name": "score",
                    }
                }
            )
            .set_global_options(legend_opts=False)
        )

        return c

    @chart_base_test(chart_type=ChartType.GAUGE)
    def test_gauge_style(self):
        c = (
            Gauge(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
            )
            .set_data(
                data={
                    "value": {
                        "target": 120,
                        "total": 400,
                        "name": "score",
                    }
                }
            )
            .set_global_options(legend_opts=False)
            .set_gauge_style(
                text_content={"color": "red"},
            )
        )

        return c

    def test_gauge_options_validation(self):
        """验证 Gauge 图表的 JSON 配置结构正确性。"""
        gauge_data = {
            "value": {
                "target": 120,
                "total": 400,
                "name": "score",
            }
        }
        gauge = Gauge().set_data(data=gauge_data)
        options = gauge.options
        assert_chart_type(options, "gauge")
        assert_options_contains(
            options,
            {
                "type": "gauge",
                "data": gauge_data,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
            ],
        )

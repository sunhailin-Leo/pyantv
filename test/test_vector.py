"""Vector 向量图基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Vector
from pyantv.globals import ChartType
from pyantv.commons.utils import JsCode

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


class TestVectorChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VECTOR)
    def test_vector_base(self):
        c = (
            Vector()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/antfincdn/"
                    "F5VcgnqRku/wind.json",
                )
            )
            .set_encode(
                x_field_name="longitude",
                y_field_name="latitude",
                color_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
                size_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
                rotate_field=JsCode(
                    "({ u, v }) => (Math.atan2(v, u) * 180) / Math.PI",
                ),
            )
            .set_scale(
                color_scale_opts={"palette": "viridis"},
                size_scale_opts={"range": [6, 20]},
            )
            .set_global_options(
                axis_opts=opts.AxisOpts(
                    x_axis_opts=opts.AxisCfgOpts(
                        axis_grid_opts=opts.AxisGridOpts(
                            is_show_grid=False,
                        ),
                    ),
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_grid_opts=opts.AxisGridOpts(
                            is_show_grid=False,
                        ),
                    ),
                ),
                legend_opts=False,
                tooltip_opts=opts.TooltipOpts(
                    title={"channel": "color", "valueFormatter": ".1f"}
                ),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VECTOR)
    def test_vector_style(self):
        c = (
            Vector()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/antfincdn/"
                    "F5VcgnqRku/wind.json",
                )
            )
            .set_encode(
                x_field_name="longitude",
                y_field_name="latitude",
                color_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
                size_field=JsCode("({ u, v }) => Math.hypot(v, u)"),
                rotate_field=JsCode(
                    "({ u, v }) => (Math.atan2(v, u) * 180) / Math.PI",
                ),
            )
            .set_scale(
                color_scale_opts={"palette": "viridis"},
                size_scale_opts={"range": [6, 20]},
            )
            .set_global_options(
                axis_opts=opts.AxisOpts(
                    x_axis_opts=opts.AxisCfgOpts(
                        axis_grid_opts=opts.AxisGridOpts(
                            is_show_grid=False,
                        ),
                    ),
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_grid_opts=opts.AxisGridOpts(
                            is_show_grid=False,
                        ),
                    ),
                ),
                legend_opts=False,
                tooltip_opts=opts.TooltipOpts(
                    title={"channel": "color", "valueFormatter": ".1f"}
                ),
                style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
            )
            .set_vector_style(arrow_size=10)
        )

        return c

    def test_vector_options_validation(self):
        """验证 Vector 图表的 JSON 配置结构正确性。"""
        TEST_DATA = [
            {"longitude": 0, "latitude": 0, "u": 1, "v": 1},
        ]
        chart = (
            Vector()
            .set_data(data=TEST_DATA)
            .set_encode(
                x_field_name="longitude",
                y_field_name="latitude",
            )
        )
        options = chart.options
        assert_chart_type(options, "vector")
        assert_encode_fields(options, x="longitude", y="latitude")
        assert_options_contains(
            options,
            {
                "type": "vector",
                "data": TEST_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode",
            ],
        )

"""Density 密度图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import Density
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


TEST_DENSITY_DATA = [
    {"x": "setosa", "y": 5.1, "size": 3.5},
    {"x": "setosa", "y": 4.9, "size": 3.0},
    {"x": "versicolor", "y": 7.0, "size": 3.2},
    {"x": "versicolor", "y": 6.4, "size": 3.2},
]


class TestDensityChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.DENSITY)
    def test_density_base(self):
        c = (
            Density(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/species.json",
                    transform=[
                        opts.KdeDataTransformOpts(
                            field="y",
                            group_by=["x"],
                            size=20,
                        )
                    ],
                )
            )
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="x",
                size_field="size",
            )
            .set_global_options(tooltip_opts=False)
        )

        return c

    def test_density_options_validation(self):
        """验证 Density 图表的 JSON 配置结构正确性。"""
        density = (
            Density()
            .set_data(data=TEST_DENSITY_DATA)
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="x",
                size_field="size",
            )
        )
        options = density.options
        assert_chart_type(options, "density")
        assert_encode_fields(options, x="x", y="y", color="x", size="size")
        assert_options_contains(
            options,
            {
                "type": "density",
                "encode": {"x": "x", "y": "y", "color": "x", "size": "size"},
                "data": TEST_DENSITY_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.x",
                "encode.y",
                "encode.color",
                "encode.size",
            ],
        )

"""Polygon 多边形图基础功能测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import Polygon
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


class TestPolygonChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.POLYGON)
    def test_polygon_base(self):
        transform_func = """
        (data) => {
          const dv = new DataSet.View().source(data).transform({
            type: 'bin.hexagon',
            fields: ['longitude', 'latitude'],
            binWidth: [2, 3],
            as: ['longitude', 'latitude', 'count'],
          });
          return dv.rows;
        }
        """

        c = (
            Polygon()
            .add_js_dependencies(*["antv@DataSet"])
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/hexbin-china.json",
                    transform=[
                        opts.CustomDataTransformOpts(
                            callback=JsCode(transform_func),
                        )
                    ],
                )
            )
            .set_encode(
                x_field_name="longitude",
                y_field_name="latitude",
                color_field="count",
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    range_="#BAE7FF-#1890FF-#0050B3",
                ),
            )
            .set_global_options(
                state_opts=opts.StateOpts(
                    active_style_opts=opts.BaseChartStyleOpts(fill="orange"),
                    inactive_style_opts=opts.BaseChartStyleOpts(opacity=0.8),
                ),
                axis_opts=False,
                legend_opts=False,
                tooltip_opts=opts.TooltipOpts(
                    items=[opts.TooltipItemOpts(field="count")],
                ),
                interaction_opts=opts.InteractionOpts(element_highlight_opts=True),
                style_opts=opts.BaseChartStyleOpts(
                    line_width=5,
                    stroke="#fff",
                ),
            )
            .set_polygon_style(arrow_size=10)
        )

        return c

    def test_polygon_options_validation(self):
        """验证 Polygon 图表的 JSON 配置结构正确性。"""
        TEST_POLYGON_DATA = [
            {"longitude": 116.4, "latitude": 39.9, "count": 10},
            {"longitude": 121.5, "latitude": 31.2, "count": 20},
        ]
        polygon = (
            Polygon()
            .set_data(data=TEST_POLYGON_DATA)
            .set_encode(
                x_field_name="longitude",
                y_field_name="latitude",
                color_field="count",
            )
        )
        options = polygon.options
        assert_chart_type(options, "polygon")
        assert_encode_fields(options, x="longitude", y="latitude", color="count")
        assert_options_contains(
            options,
            {
                "type": "polygon",
                "encode": {"x": "longitude", "y": "latitude", "color": "count"},
                "data": TEST_POLYGON_DATA,
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
            ],
        )

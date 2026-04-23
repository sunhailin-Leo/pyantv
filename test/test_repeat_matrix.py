"""RepeatMatrix 重复矩阵图测试。"""

import unittest

from pyantv import options as opts
from pyantv.charts import RepeatMatrix, Line
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    ANY,
)


class TestRepeatMatrixChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.REPEATMATRIX)
    def test_repeat_matrix_base(self):
        line = (
            Line()
            .set_encode(
                color_field="location",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupXOpts(
                        channel_name="y",
                        channel_transform="mean",
                    ),
                ],
            )
            .set_scale(y_scale_opts=opts.ScaleBaseOpts(is_zero=True))
        )

        c = (
            RepeatMatrix(
                init_opts=opts.InitOpts(
                    width="320px",
                    height="720px",
                ),
                render_opts=opts.RenderOpts(
                    padding_bottom=60,
                    padding_left=50,
                    is_auto_fit=True,
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/weather.json",
                    transform=[
                        opts.MapDataTransformOpts(
                            callback=JsCode(
                                "({ date, ...d }) => "
                                "({...d, date: new Date(date).getMonth() + ''})",
                            )
                        )
                    ],
                )
            )
            .set_encode(
                x_field_name="date",
                y_field_name=["temp_max", "precipitation", "wind"],
            )
            .set_repeat_matrix_children(children=[line.get_options()])
        )
        return c

    @chart_base_test(chart_type=ChartType.REPEATMATRIX)
    def test_repeat_matrix_encode(self):
        line = (
            Line()
            .set_encode(
                color_field="location",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupXOpts(
                        channel_name="y",
                        channel_transform="mean",
                    ),
                ],
            )
            .set_scale(y_scale_opts=opts.ScaleBaseOpts(is_zero=True))
        )

        c = (
            RepeatMatrix(
                init_opts=opts.InitOpts(
                    width="320px",
                    height="720px",
                ),
                render_opts=opts.RenderOpts(
                    padding_bottom=60,
                    padding_left=50,
                    is_auto_fit=True,
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/weather.json",
                    transform=[
                        opts.MapDataTransformOpts(
                            callback=JsCode(
                                "({ date, ...d }) => "
                                "({...d, date: new Date(date).getMonth() + ''})",
                            )
                        )
                    ],
                )
            )
            .set_encode(
                x_field_name="date",
                y_field_name=["temp_max", "precipitation", "wind"],
            )
            .set_repeat_matrix_children(children=[line.get_options()])
            .set_repeat_matrix_encode(
                x_field_name="date",
                y_field_name=["temp_max", "precipitation", "wind"],
            )
        )
        return c

    def test_repeat_matrix_options_validation(self):
        """验证 RepeatMatrix 图表的 JSON 配置结构正确性。"""
        chart = (
            RepeatMatrix()
            .set_data(
                data=[
                    {"date": "2024-01", "temp_max": 10, "precipitation": 5, "wind": 3},
                    {"date": "2024-02", "temp_max": 12, "precipitation": 6, "wind": 4},
                ]
            )
            .set_encode(
                x_field_name="date",
                y_field_name=["temp_max", "precipitation", "wind"],
            )
            .set_repeat_matrix_children(
                children=[
                    Line()
                    .set_encode(
                        color_field="location",
                    )
                    .get_options()
                ]
            )
        )

        options = chart.options
        assert_chart_type(options, "repeatMatrix")
        assert_options_contains(
            options,
            {
                "type": "repeatMatrix",
                "data": [
                    {"date": "2024-01", "temp_max": 10, "precipitation": 5, "wind": 3},
                    {"date": "2024-02", "temp_max": 12, "precipitation": 6, "wind": 4},
                ],
                "children": ANY,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "children",
            ],
        )

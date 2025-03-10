import unittest

from pyantv import options as opts
from pyantv.charts import RepeatMatrix, Line
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


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

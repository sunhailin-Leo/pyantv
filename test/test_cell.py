import unittest

from pyantv import options as opts
from pyantv.charts import Cell
from pyantv.globals import ChartType

from test import chart_base_test

TEST_INTERVAL_DATA = [
    {"letter": "A", "frequency": 0.08167},
    {"letter": "B", "frequency": 0.01492},
    {"letter": "C", "frequency": 0.02782},
    {"letter": "D", "frequency": 0.04253},
    {"letter": "E", "frequency": 0.12702},
    {"letter": "F", "frequency": 0.02288},
    {"letter": "G", "frequency": 0.02015},
    {"letter": "H", "frequency": 0.06094},
    {"letter": "I", "frequency": 0.06966},
    {"letter": "J", "frequency": 0.00153},
    {"letter": "K", "frequency": 0.00772},
    {"letter": "L", "frequency": 0.04025},
    {"letter": "M", "frequency": 0.02406},
    {"letter": "N", "frequency": 0.06749},
    {"letter": "O", "frequency": 0.07507},
    {"letter": "P", "frequency": 0.01929},
    {"letter": "Q", "frequency": 0.00095},
    {"letter": "R", "frequency": 0.05987},
    {"letter": "S", "frequency": 0.06327},
    {"letter": "T", "frequency": 0.09056},
    {"letter": "U", "frequency": 0.02758},
    {"letter": "V", "frequency": 0.00978},
    {"letter": "W", "frequency": 0.0236},
    {"letter": "X", "frequency": 0.0015},
    {"letter": "Y", "frequency": 0.01974},
    {"letter": "Z", "frequency": 0.00074},
]


class TestCellChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.CELL)
    def test_cell_base(self):
        c = (
            Cell()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/bmw-prod/"
                    "bd287f2c-3e2b-4d0a-8428-6a85211dce33.json",
                )
            )
            .set_encode(x_field_name="x", y_field_name="y", color_field="index")
            .set_scale(color_scale_opts=opts.ScaleOrdinalOpts())
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#000",
                    inset=2,
                ),
                animate_opts=opts.AnimateOpts(
                    enter_opts=opts.AnimatePropertiesOpts(
                        type_="fadeIn",
                    ),
                ),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.CELL)
    def test_cell_style(self):
        c = (
            Cell()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/bmw-prod/"
                    "bd287f2c-3e2b-4d0a-8428-6a85211dce33.json",
                )
            )
            .set_encode(x_field_name="x", y_field_name="y", color_field="index")
            .set_scale(color_scale_opts=opts.ScaleOrdinalOpts())
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#000",
                    inset=2,
                ),
                animate_opts=opts.AnimateOpts(
                    enter_opts=opts.AnimatePropertiesOpts(
                        type_="fadeIn",
                    ),
                ),
            )
            .set_cell_style(
                base_radius_inset_opts=opts.BaseChartRadiusInsetStyleOpts(
                    inset=2,
                    radius=2,
                ),
            )
        )

        return c

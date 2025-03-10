import unittest

from pyantv import options as opts
from pyantv.charts import BoxPlot
from pyantv.globals import ChartType

from test import chart_base_test


class TestBoxplotChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.BOXPLOT)
    def test_boxplot_base(self):
        c = (
            BoxPlot()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/morley.json"
                )
            )
            .set_encode(
                x_field_name="Expt",
                y_field_name="Speed",
            )
            .set_global_options(inset=6, padding_left="60")
        )

        return c

    @chart_base_test(chart_type=ChartType.BOXPLOT)
    def test_boxplot_style(self):
        c = (
            BoxPlot()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/morley.json"
                )
            )
            .set_encode(
                x_field_name="Expt",
                y_field_name="Speed",
            )
            .set_boxplot_style(
                is_extend=True,
                point_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
                box_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
            )
            .set_global_options(inset=6, padding_left="60")
        )

        return c

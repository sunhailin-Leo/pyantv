import unittest

from pyantv import options as opts
from pyantv.charts import Liquid
from pyantv.globals import ChartType

from test import chart_base_test


class TestLiquidChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.LIQUID)
    def test_liquid_base(self):
        c = (
            Liquid(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
            )
            .set_data(data=0.3)
            .set_liquid_style(
                outline_border=4,
                outline_distance=8,
                wave_length=128,
            )
        )

        return c

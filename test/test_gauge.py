import unittest

from pyantv import options as opts
from pyantv.charts import Gauge
from pyantv.globals import ChartType

from test import chart_base_test


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

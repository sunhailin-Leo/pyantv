import unittest

from pyantv import options as opts
from pyantv.charts import Density
from pyantv.globals import ChartType

from test import chart_base_test


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

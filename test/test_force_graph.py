import unittest

from pyantv import options as opts
from pyantv.charts import ForceGraph
from pyantv.globals import ChartType

from test import chart_base_test


class TestForceGraphChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.FORCEGRAPH)
    def test_force_graph_base(self):
        c = (
            ForceGraph(
                render_opts=opts.RenderOpts(is_auto_fit=True),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/miserable.json",
                )
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    range_=[
                        "#4e79a7",
                        "#f28e2c",
                        "#e15759",
                        "#76b7b2",
                        "#59a14f",
                        "#edc949",
                        "#af7aa1",
                        "#ff9da7",
                        "#9c755f",
                        "#bab0ab",
                    ],
                ),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.FORCEGRAPH)
    def test_force_graph_layout(self):
        c = (
            ForceGraph(
                render_opts=opts.RenderOpts(is_auto_fit=True),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/miserable.json",
                )
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    range_=[
                        "#4e79a7",
                        "#f28e2c",
                        "#e15759",
                        "#76b7b2",
                        "#59a14f",
                        "#edc949",
                        "#af7aa1",
                        "#ff9da7",
                        "#9c755f",
                        "#bab0ab",
                    ],
                ),
            )
            .set_force_graph_layout(
                is_joint=True,
            )
        )

        return c

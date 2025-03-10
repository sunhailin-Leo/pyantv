import unittest

from pyantv import options as opts
from pyantv.charts import Sankey
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class TestSankeyChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.SANKEY)
    def test_sankey_base(self):
        c = (
            Sankey(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="900px",
                    height="600px",
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/energy.json",
                    transform=[
                        opts.CustomDataTransformOpts(
                            callback=JsCode("(data) => ({links: data})")
                        )
                    ],
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
            .set_sankey_layout(
                node_align="center",
                node_padding=0.03,
            )
            .set_sankey_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    spacing=3,
                    font_weight="bold",
                ),
                node_style_opts=opts.BaseChartStyleOpts(line_width=1.2),
                link_style_opts=opts.BaseChartStyleOpts(fill_opacity=0.4),
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.SANKEY)
    def test_sankey_style(self):
        c = (
            Sankey(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="900px",
                    height="600px",
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/energy.json",
                    transform=[
                        opts.CustomDataTransformOpts(
                            callback=JsCode("(data) => ({links: data})")
                        )
                    ],
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
            .set_sankey_layout(
                node_align="center",
                node_padding=0.03,
            )
            .set_sankey_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    spacing=3,
                    font_weight="bold",
                ),
                node_style_opts=opts.BaseChartStyleOpts(line_width=1.2),
                link_style_opts=opts.BaseChartStyleOpts(fill_opacity=0.4),
            )
        )

        return c

import unittest

from pyantv import options as opts
from pyantv.charts import Link, View
from pyantv.globals import ChartType
from pyantv.commons.utils import JsCode

from test import chart_base_test


class TestLinkChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_link_base(self):
        link_1 = (
            Link()
            .set_encode(
                x_field_name="Date",
                y_field_name=["Low", "High"],
                color_field=JsCode("(d) => Math.sign(d.Close - d.Open)"),
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(stroke="black"),
                tooltip_opts=opts.TooltipOpts(
                    title=JsCode("(d) => d.Date.toLocaleString()"),
                    items=[
                        opts.TooltipItemOpts(field="Low", name="low"),
                        opts.TooltipItemOpts(field="High", name="high"),
                    ],
                ),
            )
        )

        link_2 = (
            Link()
            .set_encode(
                x_field_name="Date",
                y_field_name=["Open", "Close"],
                color_field=JsCode("(d) => Math.sign(d.Close - d.Open)"),
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    radius=2, fill_opacity=1, line_width=4, line_cap="round,"
                ),
                tooltip_opts=opts.TooltipOpts(
                    title="",
                    items=[
                        opts.TooltipItemOpts(field="Open", name="open"),
                        opts.TooltipItemOpts(field="Close", name="close"),
                    ],
                ),
            )
        )

        view = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl2.json",
                    transform=[
                        opts.MapDataTransformOpts(
                            callback=JsCode("(d) => ({...d, Date: new Date(d.Date)})"),
                        ),
                    ],
                )
            )
            .set_view_children(
                children=[
                    link_1.get_options(),
                    link_2.get_options(),
                ]
            )
            .set_scale(
                color_scale_opts=opts.ScaleOrdinalOpts(
                    domain=[1, 0, -1],
                    range_=["#4daf4a", "#999999", "#e41a1c"],
                )
            )
            .set_global_options(
                interaction_opts=opts.InteractionOpts(
                    tooltip_opts=opts.InteractionTooltipOpts(
                        is_shared=True,
                        is_group_name=False,
                    )
                )
            )
        )

        return view

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_link_style(self):
        link_1 = (
            Link()
            .set_encode(
                x_field_name="Date",
                y_field_name=["Low", "High"],
                color_field=JsCode("(d) => Math.sign(d.Close - d.Open)"),
            )
            .set_global_options(
                tooltip_opts=opts.TooltipOpts(
                    title=JsCode("(d) => d.Date.toLocaleString()"),
                    items=[
                        opts.TooltipItemOpts(field="Low", name="low"),
                        opts.TooltipItemOpts(field="High", name="high"),
                    ],
                ),
            )
            .set_link_style(
                arrow_size=10,
                base_style_opts=opts.BaseChartStyleOpts(stroke="black"),
            )
        )

        link_2 = (
            Link()
            .set_encode(
                x_field_name="Date",
                y_field_name=["Open", "Close"],
                color_field=JsCode("(d) => Math.sign(d.Close - d.Open)"),
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    radius=2, fill_opacity=1, line_width=4, line_cap="round,"
                ),
                tooltip_opts=opts.TooltipOpts(
                    title="",
                    items=[
                        opts.TooltipItemOpts(field="Open", name="open"),
                        opts.TooltipItemOpts(field="Close", name="close"),
                    ],
                ),
            )
        )

        view = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl2.json",
                    transform=[
                        opts.MapDataTransformOpts(
                            callback=JsCode("(d) => ({...d, Date: new Date(d.Date)})"),
                        ),
                    ],
                )
            )
            .set_view_children(
                children=[
                    link_1.get_options(),
                    link_2.get_options(),
                ]
            )
            .set_scale(
                color_scale_opts=opts.ScaleOrdinalOpts(
                    domain=[1, 0, -1],
                    range_=["#4daf4a", "#999999", "#e41a1c"],
                )
            )
            .set_global_options(
                interaction_opts=opts.InteractionOpts(
                    tooltip_opts=opts.InteractionTooltipOpts(
                        is_shared=True,
                        is_group_name=False,
                    )
                )
            )
        )

        return view

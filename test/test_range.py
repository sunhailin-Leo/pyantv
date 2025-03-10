import unittest

from pyantv import options as opts
from pyantv.charts import (
    View,
    LineX,
    LineY,
    Range,
    RangeX,
    RangeY,
    Point,
    Line,
)
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class TestRangeChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_range_base(self):
        line_x = LineX().set_data(data=[0])

        line_y = LineY().set_data(data=[0])

        range_ = (
            Range()
            .set_data(
                data=[
                    {"x": [-25, 0], "y": [-30, 0], "region": "1"},
                    {"x": [-25, 0], "y": [0, 20], "region": "2"},
                    {"x": [0, 5], "y": [-30, 0], "region": "2"},
                    {"x": [0, 5], "y": [0, 20], "region": "1"},
                ]
            )
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                color_field="region",
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    range_=["#d8d0c0", "#a3dda1"],
                    is_independent=True,
                    # guide: null ???
                )
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    fill_opacity=0.2,
                )
            )
        )

        point = (
            Point()
            .set_encode(
                x_field_name="change in female rate",
                y_field_name="change in male rate",
                size_field="pop",
                color_field="continent",
                shape_field="point",
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    range_=[
                        "#ffd500",
                        "#82cab2",
                        "#193442",
                        "#d18768",
                        "#7e827a",
                    ],
                ),
                x_scale_opts=opts.ScaleLinearOpts(domain=[-25, 5]),
                y_scale_opts=opts.ScaleLinearOpts(domain=[-30, 20]),
                size_scale_opts=opts.ScaleLinearOpts(range_=[4, 30]),
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#bbb",
                    fill_opacity=0.8,
                ),
                axis_opts=opts.AxisOpts(
                    x_axis_opts=opts.AxisCfgOpts(
                        axis_title_opts=False,
                    ),
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_title_opts=False,
                    ),
                ),
            )
        )

        c = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/bmw-prod/"
                    "0b37279d-1674-42b4-b285-29683747ad9a.json"
                )
            )
            .set_view_children(
                children=[
                    line_x.get_options(),
                    line_y.get_options(),
                    range_.get_options(),
                    point.get_options(),
                ]
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_rangex_base(self):
        range_x = (
            RangeX()
            .set_data(
                data=[
                    {
                        "year": [
                            JsCode("new Date('1933')"),
                            JsCode("new Date('1945')"),
                        ],
                        "event": "Nazi Rule",
                    },
                    {
                        "year": [
                            JsCode("new Date('1948')"),
                            JsCode("new Date('1989')"),
                        ],
                        "event": "GDR (East Germany)",
                    },
                ]
            )
            .set_encode(
                x_field_name="year",
                color_field="event",
            )
            .set_scale(
                color_scale_opts=opts.ScaleBaseOpts(
                    is_independent=True, range_=["#FAAD14", "#30BF78"]
                )
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    fill_opacity=0.75,
                )
            )
        )

        line = Line().set_encode(
            x_field_name=JsCode("(d) => new Date(d.year)"),
            y_field_name="population",
            color_field="#333",
        )

        point = (
            Point()
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.year)"),
                y_field_name="population",
                color_field="#333",
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    line_width=1.5,
                )
            )
        )

        c = (
            View()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/year-population.json",
                )
            )
            .set_view_children(
                children=[
                    range_x.get_options(),
                    line.get_options(),
                    point.get_options(),
                ]
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_rangey_base(self):
        range_y = (
            RangeY()
            .set_data(data=[{"y": [54, 72]}])
            .set_encode(y_field_name="y")
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    fill_opacity=0.75,
                )
            )
        )

        point = (
            Point()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/basement_prod/"
                    "6b4aa721-b039-49b9-99d8-540b3f87d339.json",
                )
            )
            .set_encode(
                x_field_name="height",
                y_field_name="weight",
                color_field="gender",
            )
        )

        c = View().set_view_children(
            children=[
                range_y.get_options(),
                point.get_options(),
            ]
        )

        return c

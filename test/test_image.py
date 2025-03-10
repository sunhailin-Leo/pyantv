import unittest

from pyantv import options as opts
from pyantv.charts import Image, View, Link, Line
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


TEST_IMAGE_DATA = [
    {
        "name": "Internet Explorer",
        "value": 26,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/eOYRaLPOmkieVvjyjTzM.png",
    },
    {
        "name": "Chrome",
        "value": 40,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/dWJWRLWfpOEbwCyxmZwu.png",
    },
    {
        "name": "Firefox",
        "value": 30,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/ZEPeDluKmAoTioCABBTc.png",
    },
    {
        "name": "Safari",
        "value": 24,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/eZYhlLzqWLAYwOHQAXmc.png",
    },
    {
        "name": "Opera",
        "value": 15,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/vXiGOWCGZNKuVVpVYQAw.png",
    },
    {
        "name": "Undetectable",
        "value": 8,
        "url": "https://gw.alipayobjects.com/zos/rmsportal/NjApYXminrnhBgOXyuaK.png",
    },
]


class TestImageChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_image_base(self):
        link = (
            Link()
            .set_encode(
                x_field_name=["name", "name"],
                y_field_name=JsCode("(d) => [0, d.value]"),
            )
            .set_link_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    stroke="#dfdfdf",
                    line_dash=[2, 2],
                ),
            )
        )

        line = (
            Line()
            .set_encode(
                x_field_name="name",
                y_field_name="value",
                shape_field="smooth",
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(),
                y_scale_opts=opts.ScaleLinearOpts(domain=[0, 50]),
            )
            .set_line_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.5,
                ),
            )
        )

        image = (
            Image()
            .set_encode(
                x_field_name="name",
                y_field_name="value",
                ext_field={"src": "url"},
            )
            .set_scale(
                x_scale_opts=opts.ScaleBandOpts(),
                y_scale_opts=opts.ScaleLinearOpts(domain=[0, 50]),
            )
            .set_image_style(
                base_style_opts=opts.BaseChartStyleOpts(
                    opacity=0.95,
                ),
            )
        )

        c = (
            View()
            .set_data(data=TEST_IMAGE_DATA)
            .set_view_children(
                children=[
                    link.get_options(),
                    line.get_options(),
                    image.get_options(),
                ]
            )
        )

        return c

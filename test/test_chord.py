import unittest

from pyantv import options as opts
from pyantv.charts import Chord
from pyantv.globals import ChartType

from test import chart_base_test


TEST_CHORD_DATA = [
    {
        "source": "北京",
        "target": "天津",
        "value": 30,
    },
    {
        "source": "北京",
        "target": "上海",
        "value": 80,
    },
    {
        "source": "北京",
        "target": "河北",
        "value": 46,
    },
    {
        "source": "北京",
        "target": "辽宁",
        "value": 49,
    },
    {
        "source": "北京",
        "target": "黑龙江",
        "value": 69,
    },
    {
        "source": "北京",
        "target": "吉林",
        "value": 19,
    },
    {
        "source": "天津",
        "target": "河北",
        "value": 62,
    },
    {
        "source": "天津",
        "target": "辽宁",
        "value": 82,
    },
    {
        "source": "天津",
        "target": "上海",
        "value": 16,
    },
    {
        "source": "上海",
        "target": "黑龙江",
        "value": 16,
    },
    {
        "source": "河北",
        "target": "黑龙江",
        "value": 76,
    },
    {
        "source": "河北",
        "target": "内蒙古",
        "value": 24,
    },
    {
        "source": "内蒙古",
        "target": "北京",
        "value": 32,
    },
]


class TestChordChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.CHORD)
    def test_chord_base(self):
        c = (
            Chord(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="900px",
                    height="600px",
                ),
            )
            .set_data(data={"value": {"links": TEST_CHORD_DATA}})
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

    @chart_base_test(chart_type=ChartType.CHORD)
    def test_chord_style(self):
        c = (
            Chord(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="900px",
                    height="600px",
                ),
            )
            .set_data(data={"value": {"links": TEST_CHORD_DATA}})
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
            .set_chord_style(
                y_=0.5,
                node_width_ratio=0.05,
                node_padding_ratio=0.02,
            )
        )

        return c

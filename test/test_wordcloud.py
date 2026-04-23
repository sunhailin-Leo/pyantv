"""WordCloud 词云图基础功能测试。"""

import unittest

import pyantv.options as opts

from pyantv.charts import Wordcloud
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
)


class TestWordCloudChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.WORDCLOUD)
    def test_wordcloud_base(self):
        c = (
            Wordcloud(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                    padding_top=40,
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/philosophy-word.json",
                )
            )
            .set_encode(color_field="text")
            .set_scale(
                color_scale_opts={"palette": "viridis"},
                size_scale_opts={"range": [6, 20]},
            )
            .set_wordcloud_layout(
                sprial="rectangular",
                font_size=[20, 100],
            )
        )

        return c

    @chart_base_test(chart_type=ChartType.WORDCLOUD)
    def test_wordcloud_style(self):
        c = (
            Wordcloud(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                    padding_top=40,
                ),
            )
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/philosophy-word.json",
                )
            )
            .set_encode(color_field="text")
            .set_scale(
                color_scale_opts={"palette": "viridis"},
                size_scale_opts={"range": [6, 20]},
            )
            .set_wordcloud_layout(
                sprial="rectangular",
                font_size=[20, 100],
            )
            .set_global_options(
                style_opts=opts.BaseChartStyleOpts(
                    stroke="black",
                ),
            )
        )

        return c

    def test_wordcloud_options_validation(self):
        """验证 WordCloud 图表的 JSON 配置结构正确性。"""
        TEST_DATA = [
            {"text": "hello", "value": 10},
            {"text": "world", "value": 20},
        ]
        chart = Wordcloud().set_data(data=TEST_DATA).set_encode(color_field="text")
        options = chart.options
        assert_chart_type(options, "wordCloud")
        assert_options_contains(
            options,
            {
                "type": "wordCloud",
                "data": TEST_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode",
            ],
        )

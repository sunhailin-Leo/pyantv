import unittest

from pyantv import options as opts
from pyantv.charts import Wordcloud
from pyantv.globals import ChartType

from test import chart_base_test


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

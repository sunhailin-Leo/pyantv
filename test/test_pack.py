"""Pack 打包图基础功能测试。"""

import unittest

from simplejson import JSONEncoder

from pyantv import options as opts
from pyantv.charts import Pack
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test
from test.test_helpers import (
    assert_options_contains,
    assert_options_structure,
    assert_chart_type,
    assert_encode_fields,
)


class CustomJSONEncoder(JSONEncoder):
    def encode(self, obj):
        # 调用父类的 encode 方法获取默认的 JSON 字符串
        default_encoded = super().encode(obj)
        # 替换多余的反斜杠转义
        result = default_encoded.replace("\\\\", "\\")
        return result.replace('\\"', '"')


class TestPackChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.PACK)
    def test_pack_base(self):
        c = (
            Pack(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="1000px",
                    height="1000px",
                ),
            )
            .set_json_encoder(encoder=CustomJSONEncoder)
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/flare.json",
                )
            )
            .set_encode(
                value_field="value",
                color_field="depth",
            )
            .set_scale(
                color_scale_opts=opts.ScaleLinearOpts(
                    domain=[0, 5],
                    range_=["hsl(152,80%,80%)", "hsl(228,30%,40%)"],
                )
            )
            .set_pack_layout(padding=5)
            .set_global_options(legend_opts=False)
            .set_pack_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    text=JsCode(
                        '(d) => (d.r >= 10 && d.height === 0 ? `${d.data.name}` : "")',
                    ),
                )
            )
        )

        return c

    def test_pack_options_validation(self):
        """验证 Pack 图表的 JSON 配置结构正确性。"""
        TEST_PACK_DATA = [
            {"name": "root", "value": 100, "depth": 0},
            {"name": "child1", "value": 60, "depth": 1},
            {"name": "child2", "value": 40, "depth": 1},
        ]
        pack = (
            Pack()
            .set_data(data=TEST_PACK_DATA)
            .set_encode(
                value_field="value",
                color_field="depth",
            )
        )
        options = pack.options
        assert_chart_type(options, "pack")
        assert_encode_fields(options, value="value", color="depth")
        assert_options_contains(
            options,
            {
                "type": "pack",
                "encode": {"value": "value", "color": "depth"},
                "data": TEST_PACK_DATA,
            },
        )
        assert_options_structure(
            options,
            [
                "type",
                "data",
                "encode.value",
                "encode.color",
            ],
        )

    @chart_base_test(chart_type=ChartType.PACK)
    def test_pack_style(self):
        c = (
            Pack(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="1000px",
                    height="1000px",
                ),
            )
            .set_json_encoder(encoder=CustomJSONEncoder)
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/flare.json",
                )
            )
            .set_encode(
                value_field="value",
                color_field="depth",
            )
            .set_scale(
                color_scale_opts=opts.ScaleLinearOpts(
                    domain=[0, 5],
                    range_=["hsl(152,80%,80%)", "hsl(228,30%,40%)"],
                )
            )
            .set_pack_layout(padding=5)
            .set_global_options(
                legend_opts=False,
                style_opts=opts.BaseChartStyleOpts(
                    stroke="#fff",
                    line_width=1,
                ),
            )
            .set_pack_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    text=JsCode(
                        '(d) => (d.r >= 10 && d.height === 0 ? `${d.data.name}` : "")',
                    ),
                ),
            )
        )

        return c

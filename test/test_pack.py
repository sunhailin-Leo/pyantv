import unittest

from simplejson import JSONEncoder

from pyantv import options as opts
from pyantv.charts import Pack
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


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
            .set_global_options(legend_opts=False)
            .set_pack_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    text=JsCode(
                        '(d) => (d.r >= 10 && d.height === 0 ? `${d.data.name}` : "")',
                    ),
                ),
                base_style_opts=opts.BaseChartStyleOpts(
                    stroke="#fff",
                    line_width=1,
                ),
            )
        )

        return c

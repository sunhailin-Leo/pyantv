import unittest

from simplejson import JSONEncoder

from pyantv import options as opts
from pyantv.charts import TreeMap
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


class CustomJSONEncoder(JSONEncoder):
    def encode(self, obj):
        # 调用父类的 encode 方法获取默认的 JSON 字符串
        default_encoded = super().encode(obj)
        # 替换多余的反斜杠转义
        return default_encoded.replace("\\\\", "\\")


class TestTreeMapChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.TREEMAP)
    def test_treemap_base(self):
        c = (
            TreeMap(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                ),
                init_opts=opts.InitOpts(
                    width="1100px",
                    height="900px",
                ),
            )
            .set_json_encoder(encoder=CustomJSONEncoder)
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/flare-treemap.json",
                )
            )
            .set_encode(value_field="size")
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
                )
            )
            .set_treemap_style(
                label_style_opts=opts.BaseChartStyleOpts(
                    text=JsCode(
                        "(d) => d.data.name.split('.').pop()."
                        "split(/(?=[A-Z][a-z])/g)[0]",
                    ),
                    fill="#000",
                    position="top-left",
                ),
                base_style_opts=opts.BaseChartStyleOpts(
                    fill_opacity=0.5,
                ),
            )
            .set_treemap_layout(
                path=JsCode(r"(d) => d.name.replace(/\./g, '/')"),
                tile="treemapBinary",
                padding_inner=1,
            )
        )

        return c

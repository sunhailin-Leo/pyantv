import unittest

from simplejson import JSONEncoder

from pyantv import options as opts
from pyantv.charts import Tree
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


class TestTreeChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.TREE)
    def test_tree_base(self):
        c = (
            Tree(
                render_opts=opts.RenderOpts(
                    is_auto_fit=True,
                    inset_left=15,
                    inset_right=80,
                ),
                init_opts=opts.InitOpts(
                    width="800px",
                    height="1500px",
                ),
            )
            .set_json_encoder(encoder=CustomJSONEncoder)
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/flare.json",
                )
            )
            .set_tree_layout(
                sort_by=JsCode("(a, b) => a.value - b.value"),
            )
            .set_global_options(
                coordinate_opts={
                    "transform": [{"type": "transpose"}],
                },
            )
            .set_tree_style(
                node_style_opts=opts.BaseChartStyleOpts(
                    fill=JsCode('(d) => (d.height === 0 ? "#999" : "#000")'),
                ),
                link_style_opts=opts.BaseChartStyleOpts(stroke="#999"),
                label_style_opts=opts.BaseChartStyleOpts(
                    text=JsCode("(d) => d.data.name || '-'"),
                    font_size=JsCode("(d) => (d.height === 0 ? 7 : 12)"),
                    text_align=JsCode('(d) => (d.height === 0 ? "start" : "end")'),
                    position=JsCode('(d) => (d.height !== 0 ? "left" : "right")'),
                    dx=JsCode("(d) => (d.height === 0 ? 5 : -5)"),
                    background=True,
                    background_fill="#fff",
                ),
            )
        )

        return c

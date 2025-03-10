import unittest

from pyantv import options as opts
from pyantv.charts import View, Shape, Interval
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from simplejson import JSONEncoder

from test import chart_base_test


TEST_SHAPE_DATA = [
    {"month": "Jan.", "profit": 387264, "start": 0, "end": 387264},
    {"month": "Feb.", "profit": 772096, "start": 387264, "end": 1159360},
    {"month": "Mar.", "profit": 638075, "start": 1159360, "end": 1797435},
    {"month": "Apr.", "profit": -211386, "start": 1797435, "end": 1586049},
    {"month": "May", "profit": -138135, "start": 1586049, "end": 1447914},
    {"month": "Jun", "profit": -267238, "start": 1447914, "end": 1180676},
    {"month": "Jul.", "profit": 431406, "start": 1180676, "end": 1612082},
    {"month": "Aug.", "profit": 363018, "start": 1612082, "end": 1975100},
    {"month": "Sep.", "profit": -224638, "start": 1975100, "end": 1750462},
    {"month": "Oct.", "profit": -299867, "start": 1750462, "end": 1450595},
    {"month": "Nov.", "profit": 607365, "start": 1450595, "end": 2057960},
    {"month": "Dec.", "profit": 1106986, "start": 2057960, "end": 3164946},
    {"month": "Total", "start": 0, "end": 3164946},
]


class CustomJSONEncoder(JSONEncoder):
    def encode(self, obj):
        # 调用父类的 encode 方法获取默认的 JSON 字符串
        default_encoded = super().encode(obj)
        # 替换多余的反斜杠转义
        result = default_encoded.replace("\\\\", "\\")
        return result.replace('\\"', '"')


class TestShapeChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_shape_base(self):
        interval = (
            Interval()
            .set_data(data=TEST_SHAPE_DATA)
            .set_encode(
                x_field_name="month",
                y_field_name=["end", "start"],
                color_field=JsCode(
                    "(d) => d.month === 'Total' ? 'Total': d.profit > 0 "
                    "? 'Increase' : 'Decrease'",
                ),
            )
            .set_global_options(
                axis_opts=opts.AxisOpts(
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_label_opts=opts.AxisLabelOpts(label_formatter="~s")
                    )
                ),
                tooltip_opts=opts.TooltipOpts(
                    items=[
                        opts.TooltipItemOpts(channel="y", value_formatter="~s"),
                        opts.TooltipItemOpts(channel="y1", value_formatter="~s"),
                    ]
                ),
            )
        )

        shape_render_function = """
        function watermark({ x, y }, context) {
          const { document } = context;
          const g = document.createElement("g", {});
          const c1 = document.createElement("circle", {
            style: {
              cx: x,
              cy: y,
              lineWidth: 4,
              r: 65,
              stroke: "red",
              opacity: 0.3,
            },
          });
          const c2 = document.createElement("circle", {
            style: {
              cx: x,
              cy: y,
              lineWidth: 2,
              r: 50,
              stroke: "red",
              opacity: 0.3,
            },
          });
          const text = document.createElement("text", {
            style: {
              x,
              y,
              text: "数据保密",
              transformOrigin: "center",
              transform: "rotate(30)",
              fontSize: 20,
              fill: "red",
              textAlign: "center",
              textBaseline: "middle",
              fillOpacity: 0.3,
            },
          });
          g.appendChild(c1);
          g.appendChild(c2);
          g.appendChild(text);
          return g;
        }
        """

        shape = Shape().set_shape_style(
            x_="80%",
            y_="70%",
            render=JsCode(shape_render_function),
        )

        c = (
            View()
            .set_json_encoder(encoder=CustomJSONEncoder)
            .set_view_children(
                children=[
                    interval.get_options(),
                    shape.get_options(),
                ]
            )
        )

        return c

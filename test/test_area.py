import sys
import unittest
from io import StringIO
from test import stdout_redirect

from pyantv import options as opts
from pyantv.charts import Area, Line, View
from pyantv.globals import CurrentConfig, NotebookType, ChartType
from pyantv.commons.utils import JsCode
from pyantv.render.display import HTML

from test import chart_base_test

TEST_AREA_DATA = [
    {"year": "1991", "value": 15468},
    {"year": "1992", "value": 16100},
    {"year": "1993", "value": 15900},
    {"year": "1994", "value": 17409},
    {"year": "1995", "value": 17000},
    {"year": "1996", "value": 31056},
    {"year": "1997", "value": 31982},
    {"year": "1998", "value": 32040},
    {"year": "1999", "value": 33233},
]


class TestAreaChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.VIEW)
    def test_area_base(self):
        area = (
            Area()
            .set_encode(
                x_field_name=JsCode("(d) => d.year"),
                y_field_name="value",
                shape_field="area",
            )
            .set_global_options(
                axis_opts=opts.AxisOpts(
                    y_axis_opts=opts.AxisCfgOpts(
                        axis_label_opts=opts.AxisLabelOpts(
                            label_formatter="~s",
                        ),
                        axis_title_opts=False,
                    ),
                ),
                style_opts=opts.BaseChartStyleOpts(opacity=0.2),
            )
        )

        line = Line().set_encode(
            x_field_name="year",
            y_field_name="value",
            shape_field="line",
        )

        view = (
            View()
            .set_data(data=TEST_AREA_DATA)
            .set_view_children(
                children=[
                    area.get_options(),
                    line.get_options(),
                ]
            )
        )

        return view

    @chart_base_test(chart_type=ChartType.AREA)
    def test_area_style(self):
        c = (
            Area()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl.json",
                )
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date)"),
                y_field_name=JsCode(
                    "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
                ),
            )
            .set_area_style(
                is_connect=True,
                connect_style_opts=opts.BaseChartStyleOpts(
                    fill="grey",
                    fill_opacity=0.15,
                ),
                base_style_opts=opts.BaseChartStyleOpts(
                    fill="skyblue",
                    opacity=0.5,
                    stroke="yellow",
                ),
            )
        )

        return c

    def test_area_render_jupyter_notebook(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
        c = (
            Area()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl.json",
                )
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date)"),
                y_field_name=JsCode(
                    "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
                ),
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_jupyter_lab(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
        c = (
            Area()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl.json",
                )
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date)"),
                y_field_name=JsCode(
                    "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
                ),
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_nteract(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT
        c = (
            Area()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl.json",
                )
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date)"),
                y_field_name=JsCode(
                    "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
                ),
            )
        )
        nteract_code = c.render_notebook()
        self.assertEqual(isinstance(nteract_code, HTML), True)

    def test_area_render_zeppelin(self):
        CurrentConfig.NOTEBOOK_TYPE = NotebookType.ZEPPELIN
        c = (
            Area()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://assets.antv.antgroup.com/g2/aapl.json",
                )
            )
            .set_encode(
                x_field_name=JsCode("(d) => new Date(d.date)"),
                y_field_name=JsCode(
                    "(d) => (new Date(d.date).getUTCMonth() <= 3 ? NaN : d.close)",
                ),
            )
        )
        # Block Console stdout
        stdout_redirect.fp = StringIO()
        temp_stdout, sys.stdout = sys.stdout, stdout_redirect

        # render
        c.render_notebook()
        sys.stdout = temp_stdout

        # Block Result
        self.assertIn("%html", stdout_redirect.fp.getvalue())

import unittest

from pyantv import options as opts
from pyantv.charts import View, RangeX, Line, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


range_x = (
    RangeX()
    .set_data(
        data=[
            {
                "year": [JsCode("new Date('1933')"), JsCode("new Date('1945')")],
                "event": "Nazi Rule",
            },
            {
                "year": [JsCode("new Date('1948')"), JsCode("new Date('1989')")],
                "event": "GDR (East Germany)",
            },
        ]
    )
    .set_encode(
        x_field_name="year",
        color_field="event",
    )
    .set_scale(
        color_scale_opts=opts.ScaleBaseOpts(
            is_independent=True, range_=["#FAAD14", "#30BF78"]
        )
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            fill_opacity=0.75,
        )
    )
)

line = Line().set_encode(
    x_field_name=JsCode("(d) => new Date(d.year)"),
    y_field_name="population",
    color_field="#333",
)

point = (
    Point()
    .set_encode(
        x_field_name=JsCode("(d) => new Date(d.year)"),
        y_field_name="population",
        color_field="#333",
    )
    .set_global_options(
        style_opts=opts.BaseChartStyleOpts(
            line_width=1.5,
        )
    )
)

c = (
    View()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g2/year-population.json",
        )
    )
    .set_view_children(
        children=[
            range_x.get_options(),
            line.get_options(),
            point.get_options(),
        ]
    )
)

c.render("range_x_example.html")

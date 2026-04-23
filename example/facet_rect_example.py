import unittest

from pyantv import options as opts
from pyantv.charts import FacetRect, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


point = (
    Point()
    .set_encode(
        x_field_name="x",
        y_field_name="y",
    )
    .set_global_options(
        inset=10,
        style_opts=opts.BaseChartStyleOpts(
            stroke="#000",
        )
    )
)

c = (
    FacetRect(
        init_opts=opts.InitOpts(
            width="928px",
            height="270px",
        ),
        render_opts=opts.RenderOpts(
            padding_bottom=50,
            is_auto_fit=True,
        ),
    )
    .set_data(
        data=opts.FetchDataOpts(
            value="https://assets.antv.antgroup.com/g2/anscombe.json",
        )
    )
    .set_encode(x_field_name="series")
    .set_facet_rect_children(children=[point.get_options()])
    .set_global_options(padding_bottom=50)
)

c.render("facet_rect_example.html")

import unittest

from pyantv import options as opts
from pyantv.charts import View, RangeY, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test

range_y = RangeY().set_data(data=[{"y": [54, 72]}]).set_encode(y_field_name="y")

point = (
    Point()
    .set_data(
        data=opts.FetchDataOpts(
            value="https://gw.alipayobjects.com/os/basement_prod/"
            "6b4aa721-b039-49b9-99d8-540b3f87d339.json",
        )
    )
    .set_encode(
        x_field_name="height",
        y_field_name="weight",
        color_field="gender",
    )
)

c = View().set_view_children(
    children=[
        range_y.get_options(),
        point.get_options(),
    ]
)

c.render("range_y_example.html")

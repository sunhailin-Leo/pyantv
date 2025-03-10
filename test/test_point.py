import unittest

from pyantv import options as opts
from pyantv.charts import Point
from pyantv.globals import ChartType

from test import chart_base_test


class TestPointChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.POINT)
    def test_point_base(self):
        point = (
            Point()
            .set_data(
                data=opts.FetchDataOpts(
                    value="https://gw.alipayobjects.com/os/basement_prod/"
                    "6b4aa721-b039-49b9-99d8-540b3f87d339.json",
                ),
            )
            .set_encode(
                x_field_name="height", y_field_name="weight", color_field="gender"
            )
        )

        return point

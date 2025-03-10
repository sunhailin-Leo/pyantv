import unittest

from pyantv import options as opts
from pyantv.charts import FacetCircle, Interval
from pyantv.globals import ChartType

from test import chart_base_test


TEST_FACET_CIRCLE_DATA = [
    {"month": "Jan.", "name": "A", "value": 0.006934791595377909},
    {"month": "Jan.", "name": "B", "value": 0.5249123935566857},
    {"month": "Jan.", "name": "C", "value": 0.41513918986333054},
    {"month": "Jan.", "name": "D", "value": 0.3474757321282178},
    {"month": "Feb.", "name": "A", "value": 0.6744367620365121},
    {"month": "Feb.", "name": "B", "value": 0.4504203233465016},
    {"month": "Feb.", "name": "C", "value": 0.2707482104432508},
    {"month": "Feb.", "name": "D", "value": 0.22614146019086823},
    {"month": "Mar.", "name": "A", "value": 0.5557247339319145},
    {"month": "Mar.", "name": "B", "value": 0.6951649218419647},
    {"month": "Mar.", "name": "C", "value": 0.7634210571891193},
    {"month": "Mar.", "name": "D", "value": 0.11901586359852212},
    {"month": "Apr.", "name": "A", "value": 0.514494820814186},
    {"month": "Apr.", "name": "B", "value": 0.17937155820477635},
    {"month": "Apr.", "name": "C", "value": 0.1729889521811001},
    {"month": "Apr.", "name": "D", "value": 0.6075219633726585},
    {"month": "May", "name": "A", "value": 0.6641892333420556},
    {"month": "May", "name": "B", "value": 0.2748026213806656},
    {"month": "May", "name": "C", "value": 0.20986841335367035},
    {"month": "May", "name": "D", "value": 0.8509671288636294},
    {"month": "Jun.", "name": "A", "value": 0.3153419181969468},
    {"month": "Jun.", "name": "B", "value": 0.09871120013056367},
    {"month": "Jun.", "name": "C", "value": 0.2085997446446466},
    {"month": "Jun.", "name": "D", "value": 0.13652837966306097},
    {"month": "Jul.", "name": "A", "value": 0.9540322887154593},
    {"month": "Jul.", "name": "B", "value": 0.12680232093866128},
    {"month": "Jul.", "name": "C", "value": 0.34742683765572546},
    {"month": "Jul.", "name": "D", "value": 0.28922369449769825},
    {"month": "Aug.", "name": "A", "value": 0.5444075584603434},
    {"month": "Aug.", "name": "B", "value": 0.7038864443991115},
    {"month": "Aug.", "name": "C", "value": 0.06583633260211808},
    {"month": "Aug.", "name": "D", "value": 0.7067869976252501},
    {"month": "Sept.", "name": "A", "value": 0.02313037303762422},
    {"month": "Sept.", "name": "B", "value": 0.3621065531469456},
    {"month": "Sept.", "name": "C", "value": 0.6157564842047212},
    {"month": "Sept.", "name": "D", "value": 0.6441126344539341},
    {"month": "Oct.", "name": "A", "value": 0.06636955297133507},
    {"month": "Oct.", "name": "B", "value": 0.2156469705136128},
    {"month": "Oct.", "name": "C", "value": 0.055301084345322105},
    {"month": "Oct.", "name": "D", "value": 0.7325863254196638},
    {"month": "Nov.", "name": "A", "value": 0.7342592544641906},
    {"month": "Nov.", "name": "B", "value": 0.1918399564142519},
    {"month": "Nov.", "name": "C", "value": 0.5865105524459098},
    {"month": "Nov.", "name": "D", "value": 0.8707230658583645},
    {"month": "Dec.", "name": "A", "value": 0.7988933940766398},
    {"month": "Dec.", "name": "B", "value": 0.38032251002580675},
    {"month": "Dec.", "name": "C", "value": 0.7021168611921604},
    {"month": "Dec.", "name": "D", "value": 0.6896523695547305},
]


class TestFacetCircleChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.FACETCIRCLE)
    def test_facet_circle_base(self):
        interval = Interval().set_encode(
            x_field_name="name",
            y_field_name="value",
            color_field="name",
        )

        c = (
            FacetCircle()
            .set_data(data=TEST_FACET_CIRCLE_DATA)
            .set_facet_circle_encode(position="month")
            .set_facet_circle_children(children=[interval.get_options()])
        )

        return c

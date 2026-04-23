from pyantv import options as opts
from pyantv.charts import Interval
from pyantv.commons.utils import JsCode

TEST_HISTOGRAM_DATA = [
    {"value": [0, 2], "count": 1},
    {"value": [2, 4], "count": 2},
    {"value": [4, 6], "count": 3},
    {"value": [6, 8], "count": 6},
    {"value": [8, 10], "count": 8},
    {"value": [10, 12], "count": 11},
    {"value": [12, 14], "count": 7},
    {"value": [14, 16], "count": 6},
    {"value": [16, 18], "count": 5},
    {"value": [18, 20], "count": 2},
    {"value": [20, 22], "count": 2},
    {"value": [22, 24], "count": 1},
]

histogram = (
    Interval()
    .set_data(data=TEST_HISTOGRAM_DATA)
    .set_encode(x_field_name="value", y_field_name="count")
    .set_scale()
)
histogram.render("histogram_example.html")

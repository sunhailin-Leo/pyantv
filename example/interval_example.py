from pyantv import options as opts
from pyantv.charts import Interval

TEST_INTERVAL_DATA = [
    {"letter": "A", "frequency": 0.08167},
    {"letter": "B", "frequency": 0.01492},
    {"letter": "C", "frequency": 0.02782},
    {"letter": "D", "frequency": 0.04253},
    {"letter": "E", "frequency": 0.12702},
    {"letter": "F", "frequency": 0.02288},
    {"letter": "G", "frequency": 0.02015},
    {"letter": "H", "frequency": 0.06094},
    {"letter": "I", "frequency": 0.06966},
    {"letter": "J", "frequency": 0.00153},
    {"letter": "K", "frequency": 0.00772},
    {"letter": "L", "frequency": 0.04025},
    {"letter": "M", "frequency": 0.02406},
    {"letter": "N", "frequency": 0.06749},
    {"letter": "O", "frequency": 0.07507},
    {"letter": "P", "frequency": 0.01929},
    {"letter": "Q", "frequency": 0.00095},
    {"letter": "R", "frequency": 0.05987},
    {"letter": "S", "frequency": 0.06327},
    {"letter": "T", "frequency": 0.09056},
    {"letter": "U", "frequency": 0.02758},
    {"letter": "V", "frequency": 0.00978},
    {"letter": "W", "frequency": 0.0236},
    {"letter": "X", "frequency": 0.0015},
    {"letter": "Y", "frequency": 0.01974},
    {"letter": "Z", "frequency": 0.00074},
]

# shape_field="pyramid"
c = (
    Interval()
    .set_data(data=TEST_INTERVAL_DATA)
    .set_encode(x_field_name="letter", y_field_name="frequency")
    .set_interval_style(min_width=2)
)
c.render("interval_example.html")

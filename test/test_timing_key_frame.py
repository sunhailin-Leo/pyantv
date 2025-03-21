import unittest

from pyantv import options as opts
from pyantv.charts import TimingKeyFrame, Interval, Point
from pyantv.commons.utils import JsCode
from pyantv.globals import ChartType

from test import chart_base_test


TEST_TIMING_KEY_FRAME_DATA = [
    {"gender": "male", "height": 188, "weight": 84.1},
    {"gender": "male", "height": 177.8, "weight": 64.1},
    {"gender": "female", "height": 170.2, "weight": 55},
    {"gender": "female", "height": 167.6, "weight": 58.3},
    {"gender": "female", "height": 165.1, "weight": 64.1},
    {"gender": "female", "height": 159.2, "weight": 51.8},
    {"gender": "male", "height": 168.9, "weight": 55.5},
    {"gender": "female", "height": 170.2, "weight": 69.1},
    {"gender": "male", "height": 192, "weight": 102.3},
    {"gender": "female", "height": 155, "weight": 49.2},
    {"gender": "male", "height": 174, "weight": 86.8},
    {"gender": "male", "height": 177.8, "weight": 58},
    {"gender": "male", "height": 174, "weight": 65.6},
    {"gender": "male", "height": 175.9, "weight": 77.7},
    {"gender": "male", "height": 184.9, "weight": 86.4},
    {"gender": "female", "height": 161.2, "weight": 54.8},
    {"gender": "female", "height": 174, "weight": 54.5},
    {"gender": "male", "height": 164.5, "weight": 70},
    {"gender": "female", "height": 152.4, "weight": 67.3},
    {"gender": "female", "height": 163, "weight": 72},
    {"gender": "female", "height": 170.2, "weight": 67.7},
    {"gender": "male", "height": 170.5, "weight": 67.7},
    {"gender": "male", "height": 166.4, "weight": 75},
    {"gender": "female", "height": 157.5, "weight": 76.8},
    {"gender": "female", "height": 165.1, "weight": 104.1},
    {"gender": "female", "height": 160, "weight": 75.5},
    {"gender": "female", "height": 166.4, "weight": 70.7},
    {"gender": "female", "height": 160.2, "weight": 52.1},
    {"gender": "male", "height": 170.2, "weight": 77.3},
    {"gender": "male", "height": 166.4, "weight": 85.9},
    {"gender": "female", "height": 158.8, "weight": 49.1},
    {"gender": "male", "height": 175.3, "weight": 71.8},
    {"gender": "female", "height": 164.5, "weight": 60.3},
    {"gender": "male", "height": 188, "weight": 91.4},
    {"gender": "female", "height": 168.2, "weight": 49.2},
    {"gender": "male", "height": 167.6, "weight": 74.1},
    {"gender": "male", "height": 172.7, "weight": 84.1},
    {"gender": "female", "height": 163, "weight": 62},
    {"gender": "female", "height": 172.7, "weight": 68.2},
    {"gender": "male", "height": 177.1, "weight": 83.4},
    {"gender": "male", "height": 180.1, "weight": 93},
    {"gender": "male", "height": 182.2, "weight": 87.1},
    {"gender": "male", "height": 190.5, "weight": 89.1},
    {"gender": "female", "height": 169.4, "weight": 63.4},
    {"gender": "male", "height": 177.8, "weight": 96.8},
    {"gender": "male", "height": 176.5, "weight": 73},
    {"gender": "female", "height": 162.5, "weight": 52.2},
    {"gender": "male", "height": 176, "weight": 86.4},
    {"gender": "female", "height": 165.1, "weight": 56.8},
    {"gender": "male", "height": 177.8, "weight": 81.8},
    {"gender": "male", "height": 172.7, "weight": 73.4},
    {"gender": "female", "height": 162.6, "weight": 58.6},
    {"gender": "female", "height": 163.8, "weight": 58.5},
    {"gender": "female", "height": 160, "weight": 59.5},
    {"gender": "female", "height": 162.6, "weight": 53.9},
    {"gender": "male", "height": 180.6, "weight": 72.7},
    {"gender": "female", "height": 173, "weight": 59.8},
    {"gender": "female", "height": 160, "weight": 43.2},
    {"gender": "female", "height": 175.2, "weight": 66.8},
    {"gender": "female", "height": 163.5, "weight": 51.8},
    {"gender": "male", "height": 175.3, "weight": 72.1},
    {"gender": "male", "height": 190.5, "weight": 98.2},
    {"gender": "male", "height": 184.4, "weight": 68},
    {"gender": "female", "height": 162.1, "weight": 53.6},
    {"gender": "female", "height": 159.8, "weight": 53.2},
    {"gender": "female", "height": 175.3, "weight": 65.5},
    {"gender": "male", "height": 186.7, "weight": 101.4},
    {"gender": "female", "height": 172.7, "weight": 70.5},
    {"gender": "male", "height": 185.4, "weight": 76.4},
    {"gender": "female", "height": 167.8, "weight": 59},
    {"gender": "male", "height": 177.8, "weight": 61.4},
    {"gender": "female", "height": 149.9, "weight": 46.8},
    {"gender": "male", "height": 167.6, "weight": 66.8},
    {"gender": "male", "height": 176.5, "weight": 82.3},
    {"gender": "male", "height": 180.3, "weight": 71.4},
    {"gender": "female", "height": 156.2, "weight": 58.6},
    {"gender": "female", "height": 178, "weight": 70.6},
    {"gender": "female", "height": 155, "weight": 45.9},
    {"gender": "female", "height": 160, "weight": 50.2},
    {"gender": "male", "height": 188, "weight": 87.3},
    {"gender": "female", "height": 176.5, "weight": 73.6},
    {"gender": "male", "height": 167.6, "weight": 69.1},
    {"gender": "female", "height": 172.1, "weight": 56.6},
    {"gender": "male", "height": 182.9, "weight": 79.5},
    {"gender": "female", "height": 165.1, "weight": 58.2},
    {"gender": "male", "height": 178, "weight": 89.6},
    {"gender": "male", "height": 165.1, "weight": 66.4},
    {"gender": "female", "height": 165.1, "weight": 65.5},
    {"gender": "male", "height": 174, "weight": 72.2},
    {"gender": "male", "height": 192, "weight": 90},
    {"gender": "female", "height": 174, "weight": 55.5},
    {"gender": "female", "height": 160, "weight": 59},
    {"gender": "female", "height": 170, "weight": 55.9},
    {"gender": "male", "height": 176, "weight": 78.8},
    {"gender": "female", "height": 174, "weight": 66.4},
    {"gender": "female", "height": 161.3, "weight": 60.2},
    {"gender": "female", "height": 163.5, "weight": 50},
    {"gender": "female", "height": 170.2, "weight": 55.9},
    {"gender": "female", "height": 162.5, "weight": 58.2},
    {"gender": "male", "height": 177.8, "weight": 79.5},
    {"gender": "male", "height": 177.2, "weight": 94.1},
    {"gender": "male", "height": 185.4, "weight": 94.1},
    {"gender": "female", "height": 154.4, "weight": 46.2},
    {"gender": "female", "height": 167.6, "weight": 55.7},
    {"gender": "female", "height": 176.5, "weight": 71.8},
    {"gender": "female", "height": 174, "weight": 75.7},
    {"gender": "female", "height": 170.2, "weight": 72.8},
    {"gender": "male", "height": 181.6, "weight": 70.5},
    {"gender": "male", "height": 177, "weight": 72.5},
    {"gender": "female", "height": 152, "weight": 45.8},
    {"gender": "male", "height": 184.2, "weight": 94.5},
    {"gender": "male", "height": 177.8, "weight": 74.8},
    {"gender": "female", "height": 160, "weight": 80.5},
    {"gender": "male", "height": 170, "weight": 59.5},
    {"gender": "female", "height": 170.9, "weight": 54.2},
    {"gender": "female", "height": 161.2, "weight": 55.2},
    {"gender": "female", "height": 168.9, "weight": 60.5},
    {"gender": "female", "height": 164.5, "weight": 63.2},
    {"gender": "female", "height": 162.9, "weight": 59.4},
    {"gender": "female", "height": 154.5, "weight": 49},
]


class TestTimingKeyFrameChart(unittest.TestCase):

    @chart_base_test(chart_type=ChartType.TIMINGKEYFRAME)
    def test_timing_key_frame_base(self):
        point = (
            Point()
            .set_data(data=TEST_TIMING_KEY_FRAME_DATA)
            .set_encode(
                x_field_name="height",
                y_field_name="weight",
                color_field="gender",
                group_key_field="gender",
                shape_field="point",
            )
        )

        interval = (
            Interval()
            .set_data(data=TEST_TIMING_KEY_FRAME_DATA)
            .set_encode(
                x_field_name="gender",
                y_field_name="weight",
                color_field="gender",
                key_field="gender",
            )
            .set_global_options(
                transform_opts=[
                    opts.TransformGroupXOpts(
                        channel_name="y",
                        channel_transform="mean",
                    )
                ]
            )
        )

        c = (
            TimingKeyFrame()
            .set_global_options(
                direction="alternate",
                iteration_count=4,
            )
            .set_timing_key_frame_children(
                children=[
                    interval.get_options(),
                    point.get_options(),
                ]
            )
        )

        return c

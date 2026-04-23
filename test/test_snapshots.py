"""JSON Snapshot 测试。

验证 pyantv 图表的 dump_options() 输出与基准快照完全一致。
首次运行需要先生成快照：UPDATE_SNAPSHOTS=1 pytest test/test_snapshots.py
"""

import unittest

from pyantv.charts import (
    Line,
    Interval,
    Point,
    Area,
)

from pyantv.options import (
    AnimateOpts,
    AnimatePropertiesOpts,
    CoordinatePolarOpts,
    CoordinateThetaOpts,
    LabelOpts,
    ScaleLinearOpts,
    ScaleOrdinalOpts,
    TitleOpts,
    TransformStackYOpts,
    TransformDodgeXOpts,
)

from test.snapshot_helpers import assert_snapshot_match


class TestSnapshots(unittest.TestCase):
    """JSON Snapshot 测试类。"""

    def test_snapshot_line_basic(self):
        """Line 基础折线图快照。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                    {"year": "2022", "value": 150},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        assert_snapshot_match(chart, "line_basic")

    def test_snapshot_line_with_color(self):
        """Line 多系列折线图快照。"""
        chart = (
            Line()
            .set_data(
                data=[
                    {"year": "2020", "category": "A", "value": 100},
                    {"year": "2020", "category": "B", "value": 80},
                    {"year": "2021", "category": "A", "value": 200},
                    {"year": "2021", "category": "B", "value": 150},
                ]
            )
            .set_encode(
                x_field_name="year",
                y_field_name="value",
                color_field="category",
            )
        )
        assert_snapshot_match(chart, "line_with_color")

    def test_snapshot_interval_basic(self):
        """Interval 基础柱状图快照。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "value": 30},
                    {"category": "B", "value": 70},
                    {"category": "C", "value": 50},
                ]
            )
            .set_encode(x_field_name="category", y_field_name="value")
        )
        assert_snapshot_match(chart, "interval_basic")

    def test_snapshot_interval_stacked(self):
        """Interval 堆叠柱状图快照（Transform: stackY）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "type": "X", "value": 30},
                    {"category": "A", "type": "Y", "value": 20},
                    {"category": "B", "type": "X", "value": 50},
                    {"category": "B", "type": "Y", "value": 40},
                ]
            )
            .set_encode(
                x_field_name="category",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
        )
        assert_snapshot_match(chart, "interval_stacked")

    def test_snapshot_interval_grouped(self):
        """Interval 分组柱状图快照（Transform: dodgeX）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "type": "X", "value": 30},
                    {"category": "A", "type": "Y", "value": 20},
                    {"category": "B", "type": "X", "value": 50},
                    {"category": "B", "type": "Y", "value": 40},
                ]
            )
            .set_encode(
                x_field_name="category",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformDodgeXOpts()])
        )
        assert_snapshot_match(chart, "interval_grouped")

    def test_snapshot_pie_chart(self):
        """Interval 饼图快照（stackY + theta 坐标系）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "A", "count": 40},
                    {"item": "B", "count": 30},
                    {"item": "C", "count": 20},
                    {"item": "D", "count": 10},
                ]
            )
            .set_encode(
                y_field_name="count",
                color_field="item",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts())
        )
        assert_snapshot_match(chart, "pie_chart")

    def test_snapshot_donut_chart(self):
        """Interval 环形图快照（stackY + theta + innerRadius）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "A", "count": 40},
                    {"item": "B", "count": 30},
                    {"item": "C", "count": 20},
                ]
            )
            .set_encode(
                y_field_name="count",
                color_field="item",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts(inner_radius=0.5))
        )
        assert_snapshot_match(chart, "donut_chart")

    def test_snapshot_point_basic(self):
        """Point 基础散点图快照。"""
        chart = (
            Point()
            .set_data(
                data=[
                    {"x": 1, "y": 2, "size": 10},
                    {"x": 3, "y": 4, "size": 20},
                    {"x": 5, "y": 6, "size": 15},
                ]
            )
            .set_encode(
                x_field_name="x",
                y_field_name="y",
                size_field="size",
            )
        )
        assert_snapshot_match(chart, "point_basic")

    def test_snapshot_area_basic(self):
        """Area 基础面积图快照。"""
        chart = (
            Area()
            .set_data(
                data=[
                    {"year": "2020", "value": 100},
                    {"year": "2021", "value": 200},
                    {"year": "2022", "value": 150},
                ]
            )
            .set_encode(x_field_name="year", y_field_name="value")
        )
        assert_snapshot_match(chart, "area_basic")

    def test_snapshot_with_title(self):
        """带 Title 组件的图表快照。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 3, "y": 4}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(
                title_opts=TitleOpts(
                    title="Revenue Trend",
                    subtitle="2020-2022",
                    align="center",
                )
            )
        )
        assert_snapshot_match(chart, "line_with_title")

    def test_snapshot_with_animate(self):
        """带动画配置的图表快照。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}, {"x": 3, "y": 4}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_animate(
                animate_opts=AnimateOpts(
                    enter_opts=AnimatePropertiesOpts(
                        type_="fadeIn",
                        duration=800,
                        easing="ease-in-out",
                    ),
                    exit_opts=AnimatePropertiesOpts(
                        type_="fadeOut",
                        duration=300,
                    ),
                )
            )
        )
        assert_snapshot_match(chart, "line_with_animate")

    def test_snapshot_with_scale(self):
        """带 Scale 配置的图表快照。"""
        chart = (
            Line()
            .set_data(data=[{"x": 1, "y": 100}, {"x": 2, "y": 200}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_scale(
                x_scale_opts=ScaleLinearOpts(),
                color_scale_opts=ScaleOrdinalOpts(),
            )
        )
        assert_snapshot_match(chart, "line_with_scale")

    def test_snapshot_with_labels(self):
        """带 Label 配置的图表快照。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"category": "A", "value": 30},
                    {"category": "B", "value": 70},
                ]
            )
            .set_encode(x_field_name="category", y_field_name="value")
            .set_labels(label_opts=LabelOpts(font_size=14, position="top"))
        )
        assert_snapshot_match(chart, "interval_with_labels")

    def test_snapshot_polar_bar(self):
        """极坐标柱状图快照（polar + stackY）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"item": "A", "value": 40},
                    {"item": "B", "value": 60},
                    {"item": "C", "value": 30},
                ]
            )
            .set_encode(
                x_field_name="item",
                y_field_name="value",
                color_field="item",
            )
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(
                coordinate_opts=CoordinatePolarOpts(inner_radius=0.3, outer_radius=0.9)
            )
        )
        assert_snapshot_match(chart, "polar_bar")

    def test_snapshot_full_pipeline(self):
        """完整配置管线快照（data + encode + scale + transform + coordinate + title + animate）。"""
        chart = (
            Interval()
            .set_data(
                data=[
                    {"month": "Jan", "type": "Sales", "value": 100},
                    {"month": "Jan", "type": "Profit", "value": 40},
                    {"month": "Feb", "type": "Sales", "value": 150},
                    {"month": "Feb", "type": "Profit", "value": 60},
                ]
            )
            .set_encode(
                x_field_name="month",
                y_field_name="value",
                color_field="type",
            )
            .set_transform(transform_opts=[TransformDodgeXOpts()])
            .set_scale(x_scale_opts=ScaleLinearOpts())
            .set_global_options(
                title_opts=TitleOpts(title="Monthly Report"),
                animate_opts=AnimateOpts(
                    enter_opts=AnimatePropertiesOpts(type_="growInY", duration=600)
                ),
            )
            .set_legend(legend_opts=False)
            .set_tooltip(tooltip_opts=False)
        )
        assert_snapshot_match(chart, "full_pipeline")

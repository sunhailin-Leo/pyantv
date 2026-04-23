"""图表全局配置选项测试。"""

import unittest

from pyantv.options.chart_options import (
    EMADataTransformOpts,
    FilterDataTransformOpts,
    FoldDataTransformOpts,
    JoinDataTransformOpts,
    KdeDataTransformOpts,
    LogDataTransformOpts,
    MapDataTransformOpts,
    PickDataTransformOpts,
    RenameDataTransformOpts,
    SliceDataTransformOpts,
    SortDataTransformOpts,
    SortByDataTransformOpts,
    CustomDataTransformOpts,
    FeatureDataTransformOpts,
    CustomDataOpts,
    FetchDataOpts,
    InlineDataOpts,
)
from pyantv.options.global_options import (
    TransformBinYOpts,
    TransformNormalizeXOpts,
    TransformStackXOpts,
    CoordinateHelixOpts,
)


class TestChartOptions(unittest.TestCase):

    def test_ema_data_transform_opts(self):
        obj = EMADataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "ema",
                "field": None,
                "alpha": None,
                "as": None,
            },
        )

    def test_filter_data_transform_opts(self):
        obj = FilterDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "filter",
                "callback": None,
            },
        )

    def test_fold_data_transform_opts(self):
        obj = FoldDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "fold",
                "fields": None,
                "key": None,
                "value": None,
            },
        )

    def test_join_data_transform_opts(self):
        obj = JoinDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "join",
                "join": None,
                "on": None,
                "select": None,
            },
        )

    def test_kde_data_transform_opts(self):
        obj = KdeDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "kde",
                "join": None,
                "field": None,
                "groupBy": None,
                "as": None,
                "size": None,
            },
        )

    def test_log_data_transform_opts(self):
        obj = LogDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "log",
            },
        )

    def test_map_data_transform_opts(self):
        obj = MapDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "map",
                "callback": None,
            },
        )

    def test_pick_data_transform_opts(self):
        obj = PickDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "pick",
                "fields": None,
            },
        )

    def test_rename_data_transform_opts(self):
        obj = RenameDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "rename",
            },
        )
        obj = RenameDataTransformOpts(rename_map={"old_name": "new_name"})
        self.assertEqual(
            obj.opts,
            {
                "type": "rename",
                "old_name": "new_name",
            },
        )

    def test_slice_data_transform_opts(self):
        obj = SliceDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "slice",
                "start": None,
                "end": None,
            },
        )

    def test_sort_data_transform_opts(self):
        obj = SortDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sort",
                "callback": None,
            },
        )

    def test_sort_by_data_transform_opts(self):
        obj = SortByDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sortBy",
                "fields": None,
            },
        )

    def test_custom_data_transform_opts(self):
        obj = CustomDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "custom",
                "callback": None,
            },
        )

    def test_feature_data_transform_opts(self):
        obj = FeatureDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "feature",
                "name": None,
            },
        )

    def test_custom_data_opts(self):
        obj = CustomDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "custom",
                "callback": None,
            },
        )

    def test_fetch_data_opts(self):
        obj = FetchDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "fetch",
                "value": None,
                "format": None,
                "delimiter": None,
                "autoType": None,
                "transform": None,
            },
        )

    def test_inline_data_opts(self):
        obj = InlineDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "inline",
                "value": None,
                "transform": None,
            },
        )

    def test_transform_stack_x_opts_default(self):
        """验证 TransformStackXOpts 默认参数生成正确的 opts 字典。"""
        obj = TransformStackXOpts()
        self.assertEqual(obj.opts["type"], "stackX")
        self.assertIsNone(obj.opts["groupBy"])
        self.assertIsNone(obj.opts["orderBy"])
        self.assertIsNone(obj.opts["x"])
        self.assertIsNone(obj.opts["x1"])
        self.assertIsNone(obj.opts["reverse"])
        self.assertIsNone(obj.opts["series"])

    def test_transform_stack_x_opts_with_params(self):
        """验证 TransformStackXOpts 带参数时 opts 字典正确映射。"""
        obj = TransformStackXOpts(
            group_by="color",
            order_by="value",
            x_="x",
            x1_="x1",
            is_reverse=True,
            is_series=False,
        )
        self.assertEqual(
            obj.opts,
            {
                "type": "stackX",
                "groupBy": "color",
                "orderBy": "value",
                "x": "x",
                "x1": "x1",
                "reverse": True,
                "series": False,
            },
        )

    def test_transform_normalize_x_opts_default(self):
        """验证 TransformNormalizeXOpts 默认参数生成正确的 opts 字典。"""
        obj = TransformNormalizeXOpts()
        self.assertEqual(obj.opts["type"], "normalizeX")
        self.assertIsNone(obj.opts["groupBy"])
        self.assertIsNone(obj.opts["basis"])

    def test_transform_normalize_x_opts_with_params(self):
        """验证 TransformNormalizeXOpts 带参数时 opts 字典正确映射。"""
        obj = TransformNormalizeXOpts(group_by="color", basis="max")
        self.assertEqual(
            obj.opts,
            {
                "type": "normalizeX",
                "groupBy": "color",
                "basis": "max",
            },
        )

    def test_transform_bin_y_opts_default(self):
        """验证 TransformBinYOpts 默认参数生成正确的 opts 字典。"""
        obj = TransformBinYOpts()
        self.assertEqual(obj.opts["type"], "binY")
        self.assertIsNone(obj.opts["thresholds"])
        self.assertNotIn("count", obj.opts)

    def test_transform_bin_y_opts_with_channel(self):
        """验证 TransformBinYOpts 带 channel 参数时 opts 字典正确映射。"""
        obj = TransformBinYOpts(
            thresholds=10,
            channel_name="count",
            channel_transform="sum",
        )
        self.assertEqual(obj.opts["type"], "binY")
        self.assertEqual(obj.opts["thresholds"], 10)
        self.assertEqual(obj.opts["count"], "sum")

    def test_coordinate_helix_opts_default(self):
        """验证 CoordinateHelixOpts 默认参数生成正确的 opts 字典。"""
        obj = CoordinateHelixOpts()
        self.assertEqual(obj.opts["type"], "helix")
        self.assertIsNone(obj.opts["startAngle"])
        self.assertIsNone(obj.opts["endAngle"])
        self.assertIsNone(obj.opts["innerRadius"])
        self.assertIsNone(obj.opts["outerRadius"])

    def test_coordinate_helix_opts_with_params(self):
        """验证 CoordinateHelixOpts 带参数时 opts 字典正确映射。"""
        obj = CoordinateHelixOpts(
            start_angle=-3.14,
            end_angle=3.14,
            inner_radius=0.2,
            outer_radius=0.8,
        )
        self.assertEqual(
            obj.opts,
            {
                "type": "helix",
                "startAngle": -3.14,
                "endAngle": 3.14,
                "innerRadius": 0.2,
                "outerRadius": 0.8,
            },
        )

    def test_encode_new_channels(self):
        """验证 set_encode 新增编码通道正确映射到 encode 字典。"""
        from pyantv.charts import Line

        line = Line().set_encode(
            x_field_name="year",
            y_field_name="value",
            opacity_field="weight",
            fill_field="category",
            stroke_field="border",
            stroke_width_field="thickness",
            font_size_field="importance",
            font_weight_field="bold",
            dx_field="offsetX",
            dy_field="offsetY",
            title_field="label",
            href_field="link",
            src_field="image",
        )
        encode = line.options.get("encode")
        self.assertEqual(encode["x"], "year")
        self.assertEqual(encode["y"], "value")
        self.assertEqual(encode["opacity"], "weight")
        self.assertEqual(encode["fill"], "category")
        self.assertEqual(encode["stroke"], "border")
        self.assertEqual(encode["strokeWidth"], "thickness")
        self.assertEqual(encode["fontSize"], "importance")
        self.assertEqual(encode["fontWeight"], "bold")
        self.assertEqual(encode["dx"], "offsetX")
        self.assertEqual(encode["dy"], "offsetY")
        self.assertEqual(encode["title"], "label")
        self.assertEqual(encode["href"], "link")
        self.assertEqual(encode["src"], "image")

    def test_encode_new_channels_default_none(self):
        """验证新增编码通道默认值为 None，不影响现有调用。"""
        from pyantv.charts import Line

        line = Line().set_encode(
            x_field_name="year",
            y_field_name="value",
        )
        encode = line.options.get("encode")
        self.assertEqual(encode["x"], "year")
        self.assertEqual(encode["y"], "value")
        self.assertIsNone(encode["opacity"])
        self.assertIsNone(encode["fill"])
        self.assertIsNone(encode["stroke"])
        self.assertIsNone(encode["strokeWidth"])
        self.assertIsNone(encode["fontSize"])
        self.assertIsNone(encode["fontWeight"])
        self.assertIsNone(encode["dx"])
        self.assertIsNone(encode["dy"])
        self.assertIsNone(encode["title"])
        self.assertIsNone(encode["href"])
        self.assertIsNone(encode["src"])

    def test_animate_properties_opts_default(self):
        """验证 AnimatePropertiesOpts 默认参数生成正确的 opts 字典。"""
        from pyantv.options.global_options import AnimatePropertiesOpts

        obj = AnimatePropertiesOpts()
        self.assertIsNone(obj.opts["type"])
        self.assertIsNone(obj.opts["duration"])
        self.assertIsNone(obj.opts["delay"])
        self.assertIsNone(obj.opts["easing"])

    def test_animate_properties_opts_with_params(self):
        """验证 AnimatePropertiesOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AnimatePropertiesOpts

        obj = AnimatePropertiesOpts(
            type_="fadeIn", duration=1000, delay=200, easing="ease-in-out"
        )
        self.assertEqual(obj.opts["type"], "fadeIn")
        self.assertEqual(obj.opts["duration"], 1000)
        self.assertEqual(obj.opts["delay"], 200)
        self.assertEqual(obj.opts["easing"], "ease-in-out")

    def test_animate_opts_default(self):
        """验证 AnimateOpts 默认参数生成正确的 opts 字典。"""
        from pyantv.options.global_options import AnimateOpts

        obj = AnimateOpts()
        self.assertIsNone(obj.opts["enter"])
        self.assertIsNone(obj.opts["update"])
        self.assertIsNone(obj.opts["exit"])

    def test_animate_opts_with_params(self):
        """验证 AnimateOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AnimateOpts, AnimatePropertiesOpts

        enter = AnimatePropertiesOpts(type_="fadeIn", duration=500)
        obj = AnimateOpts(enter_opts=enter)
        self.assertEqual(obj.opts["enter"].opts["type"], "fadeIn")
        self.assertEqual(obj.opts["enter"].opts["duration"], 500)
        self.assertIsNone(obj.opts["update"])
        self.assertIsNone(obj.opts["exit"])

    def test_title_opts_default(self):
        """验证 TitleOpts 默认参数生成正确的 opts 字典。"""
        from pyantv.options.global_options import TitleOpts

        obj = TitleOpts()
        self.assertIsNone(obj.opts["size"])
        self.assertIsNone(obj.opts["title"])
        self.assertIsNone(obj.opts["subtitle"])
        self.assertIsNone(obj.opts["align"])
        self.assertIsNone(obj.opts["spacing"])
        self.assertIsNone(obj.opts["titleFontSize"])
        self.assertIsNone(obj.opts["titleFontFamily"])
        self.assertIsNone(obj.opts["titleFontWeight"])
        self.assertIsNone(obj.opts["titleFill"])
        self.assertIsNone(obj.opts["titleFillOpacity"])
        self.assertIsNone(obj.opts["titleStroke"])
        self.assertIsNone(obj.opts["titleLineWidth"])
        self.assertIsNone(obj.opts["titleStrokeOpacity"])
        self.assertIsNone(obj.opts["subtitleFontSize"])
        self.assertIsNone(obj.opts["subtitleFontFamily"])
        self.assertIsNone(obj.opts["subtitleFontWeight"])
        self.assertIsNone(obj.opts["subtitleFill"])
        self.assertIsNone(obj.opts["subtitleFillOpacity"])
        self.assertIsNone(obj.opts["subtitleStroke"])
        self.assertIsNone(obj.opts["subtitleLineWidth"])
        self.assertIsNone(obj.opts["subtitleStrokeOpacity"])

    def test_title_opts_with_params(self):
        """验证 TitleOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import TitleOpts

        obj = TitleOpts(
            title="My Chart", subtitle="Sub", align="center", title_font_size=16
        )
        self.assertEqual(obj.opts["title"], "My Chart")
        self.assertEqual(obj.opts["subtitle"], "Sub")
        self.assertEqual(obj.opts["align"], "center")
        self.assertEqual(obj.opts["titleFontSize"], 16)

    def test_axis_title_opts_with_params(self):
        """验证 AxisTitleOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AxisTitleOpts

        obj = AxisTitleOpts(title="X Axis", title_spacing=10, title_position="center")
        self.assertEqual(obj.opts["title"], "X Axis")
        self.assertEqual(obj.opts["titleSpacing"], 10)
        self.assertEqual(obj.opts["titlePosition"], "center")

    def test_axis_line_opts_with_params(self):
        """验证 AxisLineOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AxisLineOpts

        obj = AxisLineOpts(is_show_line=True, line_stroke="#000", line_width=2)
        self.assertEqual(obj.opts["line"], True)
        self.assertEqual(obj.opts["lineStroke"], "#000")
        self.assertEqual(obj.opts["lineLineWidth"], 2)

    def test_axis_tick_opts_with_params(self):
        """验证 AxisTickOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AxisTickOpts

        obj = AxisTickOpts(is_show_tick=True, tick_length=5, tick_direction="positive")
        self.assertEqual(obj.opts["tick"], True)
        self.assertEqual(obj.opts["tickLength"], 5)
        self.assertEqual(obj.opts["tickDirection"], "positive")

    def test_axis_label_opts_with_params(self):
        """验证 AxisLabelOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AxisLabelOpts

        obj = AxisLabelOpts(
            is_show_label=True, label_font_size=12, label_align="horizontal"
        )
        self.assertEqual(obj.opts["label"], True)
        self.assertEqual(obj.opts["labelFontSize"], 12)
        self.assertEqual(obj.opts["labelAlign"], "horizontal")

    def test_axis_grid_opts_with_params(self):
        """验证 AxisGridOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import AxisGridOpts

        obj = AxisGridOpts(is_show_grid=True, grid_stroke="#eee", grid_line_width=1)
        self.assertEqual(obj.opts["grid"], True)
        self.assertEqual(obj.opts["gridStroke"], "#eee")
        self.assertEqual(obj.opts["gridLineWidth"], 1)

    def test_state_opts_with_params(self):
        """验证 StateOpts 带参数时 opts 字典正确映射。"""
        from pyantv.options.global_options import StateOpts, BaseChartStyleOpts

        active = BaseChartStyleOpts()
        active.opts = {"fill": "red"}
        obj = StateOpts(active_style_opts=active)
        self.assertEqual(obj.opts["active"].opts["fill"], "red")
        self.assertIsNone(obj.opts["inactive"])
        self.assertIsNone(obj.opts["selected"])
        self.assertIsNone(obj.opts["unselected"])

    def test_set_scale_new_channels(self):
        """验证 set_scale 新增的 shape/opacity 通道正确映射。"""
        from pyantv.charts import Line
        from pyantv.options import ScaleLinearOpts

        shape_scale = ScaleLinearOpts()
        opacity_scale = ScaleLinearOpts()
        line = Line().set_scale(
            x_scale_opts=ScaleLinearOpts(),
            shape_scale_opts=shape_scale,
            opacity_scale_opts=opacity_scale,
        )
        scale = line.options.get("scale")
        self.assertIsNotNone(scale["x"])
        self.assertIs(scale["shape"], shape_scale)
        self.assertIs(scale["opacity"], opacity_scale)

    def test_set_scale_ext_scale(self):
        """验证 set_scale 的 ext_scale 扩展字典正确合并。"""
        from pyantv.charts import Line
        from pyantv.options import ScaleLinearOpts

        line = Line().set_scale(
            x_scale_opts=ScaleLinearOpts(),
            ext_scale={"customChannel": {"type": "band"}},
        )
        scale = line.options.get("scale")
        self.assertIsNotNone(scale["x"])
        self.assertEqual(scale["customChannel"], {"type": "band"})

    def test_set_scale_default_none(self):
        """验证 set_scale 新增通道默认值为 None，不影响现有调用。"""
        from pyantv.charts import Line

        line = Line().set_scale(x_scale_opts=None)
        scale = line.options.get("scale")
        self.assertIsNone(scale["shape"])
        self.assertIsNone(scale["opacity"])

    def test_animate_integration_with_global_options(self):
        """验证通过 set_global_options 设置动画后 options 字典正确。"""
        from pyantv.charts import Line
        from pyantv.options import AnimateOpts, AnimatePropertiesOpts

        enter = AnimatePropertiesOpts(
            type_="fadeIn", duration=500, delay=100, easing="ease-in-out"
        )
        exit_ = AnimatePropertiesOpts(type_="fadeOut", duration=300)
        animate = AnimateOpts(enter_opts=enter, exit_opts=exit_)

        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_encode(x_field_name="x", y_field_name="y")
            .set_global_options(animate_opts=animate)
        )
        options = line.options
        anim = options.get("animate")
        self.assertIsNotNone(anim)
        self.assertEqual(anim.opts["enter"].opts["type"], "fadeIn")
        self.assertEqual(anim.opts["enter"].opts["duration"], 500)
        self.assertEqual(anim.opts["enter"].opts["delay"], 100)
        self.assertEqual(anim.opts["enter"].opts["easing"], "ease-in-out")
        self.assertEqual(anim.opts["exit"].opts["type"], "fadeOut")
        self.assertEqual(anim.opts["exit"].opts["duration"], 300)
        self.assertIsNone(anim.opts["update"])

    def test_animate_disable(self):
        """验证 animate 设置为 False 可以禁用动画。"""
        from pyantv.charts import Line

        line = (
            Line()
            .set_data(data=[{"x": 1, "y": 2}])
            .set_global_options(animate_opts=False)
        )
        self.assertFalse(line.options.get("animate"))

    def test_set_transform_independent(self):
        """验证独立的 set_transform 方法正确设置 transform。"""
        from pyantv.charts import Interval
        from pyantv.options import TransformStackYOpts

        interval = (
            Interval()
            .set_data(data=[{"x": "A", "y": 10}])
            .set_transform(transform_opts=[TransformStackYOpts()])
        )
        transform = interval.options.get("transform")
        self.assertIsNotNone(transform)
        self.assertIsInstance(transform, list)

    def test_set_coordinate_independent(self):
        """验证独立的 set_coordinate 方法正确设置坐标系。"""
        from pyantv.charts import Interval
        from pyantv.options import CoordinatePolarOpts

        interval = (
            Interval()
            .set_data(data=[{"x": "A", "y": 10}])
            .set_coordinate(coordinate_opts=CoordinatePolarOpts(inner_radius=0.5))
        )
        coord = interval.options.get("coordinate")
        self.assertIsNotNone(coord)
        self.assertEqual(coord.opts["type"], "polar")
        self.assertEqual(coord.opts["innerRadius"], 0.5)

    def test_set_interaction_independent(self):
        """验证独立的 set_interaction 方法正确设置交互。"""
        from pyantv.charts import Line

        line = Line().set_interaction(interaction_opts={"tooltip": {}})
        self.assertEqual(line.options.get("interaction"), {"tooltip": {}})

    def test_set_animate_independent(self):
        """验证独立的 set_animate 方法正确设置动画。"""
        from pyantv.charts import Line
        from pyantv.options import AnimateOpts, AnimatePropertiesOpts

        enter = AnimatePropertiesOpts(type_="fadeIn", duration=500)
        animate = AnimateOpts(enter_opts=enter)
        line = Line().set_animate(animate_opts=animate)
        anim = line.options.get("animate")
        self.assertIsNotNone(anim)
        self.assertEqual(anim.opts["enter"].opts["type"], "fadeIn")

    def test_set_style_independent(self):
        """验证独立的 set_style 方法正确设置样式。"""
        from pyantv.charts import Line
        from pyantv.options import BaseChartStyleOpts

        style = BaseChartStyleOpts(fill="red", stroke="#000")
        line = Line().set_style(style_opts=style)
        self.assertIsNotNone(line.options.get("style"))

    def test_set_tooltip_independent(self):
        """验证独立的 set_tooltip 方法正确设置提示框。"""
        from pyantv.charts import Line
        from pyantv.options import TooltipOpts

        tooltip = TooltipOpts(title="Tooltip Title")
        line = Line().set_tooltip(tooltip_opts=tooltip)
        self.assertIsNotNone(line.options.get("tooltip"))

    def test_set_axis_independent(self):
        """验证独立的 set_axis 方法正确设置坐标轴。"""
        from pyantv.charts import Line

        line = Line().set_axis(axis_opts={"x": {"title": "X Axis"}})
        self.assertEqual(line.options.get("axis"), {"x": {"title": "X Axis"}})

    def test_set_legend_independent(self):
        """验证独立的 set_legend 方法正确设置图例。"""
        from pyantv.charts import Line

        line = Line().set_legend(legend_opts=False)
        self.assertFalse(line.options.get("legend"))

    def test_set_labels_independent(self):
        """验证独立的 set_labels 方法正确设置标签。"""
        from pyantv.charts import Line
        from pyantv.options import LabelOpts

        label = LabelOpts(font_size=12, position="top")
        line = Line().set_labels(label_opts=label)
        self.assertIsNotNone(line.options.get("labels"))

    def test_independent_methods_chaining(self):
        """验证所有独立方法支持链式调用。"""
        from pyantv.charts import Interval
        from pyantv.options import (
            TransformStackYOpts,
            CoordinateThetaOpts,
            AnimateOpts,
            AnimatePropertiesOpts,
        )

        chart = (
            Interval()
            .set_data(data=[{"x": "A", "y": 30}, {"x": "B", "y": 70}])
            .set_encode(x_field_name="x", y_field_name="y", color_field="x")
            .set_transform(transform_opts=[TransformStackYOpts()])
            .set_coordinate(coordinate_opts=CoordinateThetaOpts())
            .set_animate(
                animate_opts=AnimateOpts(
                    enter_opts=AnimatePropertiesOpts(type_="waveIn")
                )
            )
            .set_legend(legend_opts=False)
            .set_tooltip(tooltip_opts=False)
        )
        self.assertEqual(chart.options.get("type"), "interval")
        self.assertIsNotNone(chart.options.get("transform"))
        self.assertIsNotNone(chart.options.get("coordinate"))
        self.assertIsNotNone(chart.options.get("animate"))
        self.assertFalse(chart.options.get("legend"))
        self.assertFalse(chart.options.get("tooltip"))

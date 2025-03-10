import unittest

from pyantv.commons.utils import remove_key_with_none_value
from pyantv.options.global_options import (
    BaseChartStyleOpts,
    BaseChartRadiusInsetStyleOpts,
    InitOpts,
    RenderOpts,
    ScaleBaseOpts,
    ScaleBandOpts,
    ScaleLinearOpts,
    ScaleLogOpts,
    ScaleOrdinalOpts,
    ScalePointOpts,
    ScalePowOpts,
    ScaleQuantileOpts,
    ScaleQuantizeOpts,
    ScaleSqrtOpts,
    ScaleThresholdOpts,
    ScaleTimeOpts,
    TransformBinOpts,
    TransformBinXOpts,
    TransformDiffXOpts,
    TransformDodgeXOpts,
    TransformFlexXOpts,
    TransformGroupOpts,
    TransformGroupColorOpts,
    TransformGroupXOpts,
    TransformGroupYOpts,
    TransformJitterOpts,
    TransformJitterXOpts,
    TransformJitterYOpts,
    TransformNormalizeYOpts,
    TransformPackOpts,
    TransformSampleOpts,
    TransformSelectOpts,
    TransformSelectXOpts,
    TransformSelectYOpts,
    TransformSortColorOpts,
    TransformSortXOpts,
    TransformSortYOpts,
    TransformStackEnterOpts,
    TransformStackYOpts,
    TransformSymmetryYOpts,
    CoordinateFishEyeOpts,
    CoordinateParallelOpts,
    CoordinatePolarOpts,
    CoordinateRadialOpts,
    CoordinateThetaOpts,
    CoordinateTransposeOpts,
    CoordinateCartesian3DOpts,
    AnimatePropertiesOpts,
    AnimateOpts,
    TitleOpts,
    AxisTitleOpts,
    AxisLineOpts,
    AxisTickOpts,
    AxisLabelOpts,
    AxisGridOpts,
    EffectTimingOpts,
    AxisCfgOpts,
    AxisOpts,
    StateOpts,
    ScrollBarStyleOpts,
    ScrollBarCfgOpts,
    ScrollBarOpts,
    SliderStyleOpts,
    SliderCfgOpts,
    SliderOpts,
    LegendTitleOpts,
    LegendLayoutOpts,
    LegendCategoryCfgOpts,
    LegendCategoryOpts,
    LegendAxisOpts,
    LegendContinuousOpts,
    TooltipItemOpts,
    TooltipOpts,
    LabelTransformContrastReverseOpts,
    LabelTransformOverflowHideOpts,
    LabelTransformOverlapDodgeYOpts,
    LabelTransformOverlapHideOpts,
    LabelTransformExceedAdjustOpts,
    LabelOpts,
    InteractionMaskStyleOpts,
    InteractionBrushAxisHighlightOpts,
    InteractionBrushFilterOpts,
    InteractionBrushHighlightOpts,
    InteractionBrushXFilterOpts,
    InteractionBrushXHighlightOpts,
    InteractionBrushYFilterOpts,
    InteractionBrushYHighlightOpts,
    InteractionRuleStyleOpts,
    InteractionLabelStyleOpts,
    InteractionChartIndexOpts,
    InteractionBackgroundStyleOpts,
    InteractionElementHighlightOpts,
    InteractionLinkStyleOpts,
    InteractionElementHighlightByColorOpts,
    InteractionElementHighlightByXOpts,
    InteractionElementSelectOpts,
    InteractionElementSelectByColorOpts,
    InteractionElementSelectByXOpts,
    InteractionFishEyeOpts,
    InteractionLegendFilterOpts,
    InteractionLegendHighlightOpts,
    InteractionTipStyleOpts,
    InteractionPopTipOpts,
    InteractionTooltipBBoxOpts,
    InteractionCrossHairsStyleOpts,
    InteractionCrossHairsXStyleOpts,
    InteractionCrossHairsYStyleOpts,
    InteractionMarkerStyleOpts,
    InteractionTooltipOpts,
    InteractionOpts,
)


class TestGlobalOptions(unittest.TestCase):
    def test_base_chart_style_opts(self):
        obj = BaseChartStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "text": None,
                "textAlign": None,
                "position": None,
                "fill": None,
                "fillOpacity": None,
                "stroke": None,
                "strokeOpacity": None,
                "lineWidth": None,
                "lineDash": None,
                "lineCap": None,
                "opacity": None,
                "shadowColor": None,
                "shadowOffsetX": None,
                "shadowOffsetY": None,
                "cursor": None,
                "dx": None,
                "dy": None,
                "inset": None,
                "radius": None,
                "background": None,
                "backgroundFill": None,
                "fontWeight": None,
                "fontSize": None,
                "spacing": None,
            },
        )

    def test_base_chart_radius_inset_style_opts(self):
        obj = BaseChartRadiusInsetStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "radius": None,
                "radiusTopLeft": None,
                "radiusTopRight": None,
                "radiusBottomLeft": None,
                "radiusBottomRight": None,
                "innerRadiusTopLeft": None,
                "innerRadiusTopRight": None,
                "innerRadiusBottomLeft": None,
                "innerRadiusBottomRight": None,
                "inset": None,
                "insetLeft": None,
                "insetRight": None,
                "insetBottom": None,
                "insetTop": None,
            },
        )

    def test_init_opts(self):
        obj = InitOpts()
        self.assertEqual(
            obj.opts,
            {
                "width": "900px",
                "height": "500px",
                "is_horizontal_center": False,
                "page_title": "Awesome-pyantv",
                "bg_color": None,
                "fill_bg": False,
                "js_host": "",
                "is_embed_js": False,
            },
        )

    def test_render_opts(self):
        obj = RenderOpts()
        self.assertEqual(
            obj.opts,
            {
                "container": None,
                "autoFit": None,
                "theme": None,
                "padding": None,
                "paddingLeft": None,
                "paddingRight": None,
                "paddingTop": None,
                "paddingBottom": None,
                "margin": None,
                "marginLeft": None,
                "marginRight": None,
                "marginTop": None,
                "marginBottom": None,
                "ratio": None,
                "direction": None,
                "iterationCount": None,
                "duration": None,
                "insetLeft": None,
                "insetRight": None,
            },
        )

    def test_scale_base_opts(self):
        obj = ScaleBaseOpts()
        self.assertEqual(
            obj.opts,
            {
                "padding": None,
                "independent": None,
                "key": None,
                "range": None,
                "zero": None,
            },
        )

    def test_scale_band_opts(self):
        obj = ScaleBandOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "band",
                "domain": None,
                "range": None,
                "unknown": None,
                "round": None,
                "paddingInner": None,
                "paddingOuter": None,
                "align": None,
                "compare": None,
                "flex": None,
            },
        )

    def test_scale_linear_opts(self):
        obj = ScaleLinearOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "linear",
                "domain": None,
                "domainMin": None,
                "domainMax": None,
                "range": None,
                "rangeMin": None,
                "rangeMax": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "round": None,
                "clamp": None,
                "nice": None,
                "interpolate": None,
            },
        )

    def test_scale_log_opts(self):
        obj = ScaleLogOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "log",
                "domain": None,
                "domainMin": None,
                "domainMax": None,
                "range": None,
                "rangeMin": None,
                "rangeMax": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "round": None,
                "clamp": None,
                "nice": None,
                "interpolate": None,
                "base": 10,
            },
        )

    def test_scale_ordinal_opts(self):
        obj = ScaleOrdinalOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "ordinal",
                "domain": None,
                "range": None,
                "unknown": None,
                "compare": None,
            },
        )

    def test_scale_point_opts(self):
        obj = ScalePointOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "point",
                "domain": None,
                "range": None,
                "unknown": None,
                "round": None,
                "paddingInner": None,
                "paddingOuter": None,
                "padding": None,
                "align": None,
                "compare": None,
            },
        )

    def test_scale_pow_opts(self):
        obj = ScalePowOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "pow",
                "domain": None,
                "domainMin": None,
                "domainMax": None,
                "range": None,
                "rangeMin": None,
                "rangeMax": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "round": None,
                "clamp": None,
                "nice": None,
                "interpolate": None,
                "exponent": 2,
            },
        )

    def test_scale_quantile_opts(self):
        obj = ScaleQuantileOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "quantile",
                "domain": None,
                "range": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "nice": None,
            },
        )

    def test_scale_quantize_opts(self):
        obj = ScaleQuantizeOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "quantize",
                "domain": None,
                "range": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "nice": None,
            },
        )

    def test_scale_sqrt_opts(self):
        obj = ScaleSqrtOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sqrt",
                "domain": None,
                "domainMin": None,
                "domainMax": None,
                "range": None,
                "rangeMin": None,
                "rangeMax": None,
                "unknown": None,
                "tickCount": None,
                "tickMethod": None,
                "round": None,
                "clamp": None,
                "nice": None,
                "interpolate": None,
                "exponent": 0.5,
            },
        )

    def test_scale_threshold_opts(self):
        obj = ScaleThresholdOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "threshold",
                "domain": None,
                "range": None,
                "unknown": None,
            },
        )

    def test_scale_time_opts(self):
        obj = ScaleTimeOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "time",
                "domain": None,
                "domainMin": None,
                "domainMax": None,
                "range": None,
                "rangeMin": None,
                "rangeMax": None,
                "unknown": None,
                "tickCount": None,
                "tickInterval": None,
                "tickMethod": None,
                "round": None,
                "clamp": None,
                "nice": None,
                "mask": None,
                "utc": None,
                "interpolate": None,
            },
        )

    def test_transform_bin_opts(self):
        obj = TransformBinOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "bin",
                "thresholdsX": None,
                "thresholdsY": None,
            },
        )

        obj = TransformBinOpts(
            channel_name="x",
            channel_transform="mean",
        )
        self.assertEqual(
            obj.opts,
            {
                "type": "bin",
                "thresholdsX": None,
                "thresholdsY": None,
                "x": "mean",
            },
        )

    def test_transform_bin_x_opts(self):
        obj = TransformBinXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "binX",
                "thresholds": None,
            },
        )

    def test_transform_diff_x_opts(self):
        obj = TransformDiffXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "diffY",
                "groupBy": None,
                "series": None,
            },
        )

    def test_transform_dodge_x_opts(self):
        obj = TransformDodgeXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "dodgeX",
                "groupBy": None,
                "reverse": None,
                "orderBy": None,
                "padding": None,
            },
        )

    def test_transform_flex_x_opts(self):
        obj = TransformFlexXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "flexX",
                "field": None,
                "channel": None,
                "reducer": None,
            },
        )

    def test_transform_group_opts(self):
        obj = TransformGroupOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "group",
                "channels": None,
            },
        )

    def test_transform_group_color_opts(self):
        obj = TransformGroupColorOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "groupColor",
            },
        )

    def test_transform_group_x_opts(self):
        obj = TransformGroupXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "groupX",
            },
        )

    def test_transform_group_y_opts(self):
        obj = TransformGroupYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "groupY",
            },
        )

        obj = TransformGroupYOpts(
            channel_name="x",
            channel_transform="mean",
        )
        self.assertEqual(
            obj.opts,
            {
                "type": "groupY",
                "x": "mean",
            },
        )

    def test_transform_jitter_opts(self):
        obj = TransformJitterOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "jitter",
                "padding": None,
                "paddingX": None,
                "paddingY": None,
                "random": None,
            },
        )

    def test_transform_jitter_x_opts(self):
        obj = TransformJitterXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "jitterX",
                "padding": None,
                "random": None,
            },
        )

    def test_transform_jitter_y_opts(self):
        obj = TransformJitterYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "jitterY",
                "padding": None,
                "random": None,
            },
        )

    def test_transform_normalize_y_opts(self):
        obj = TransformNormalizeYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "normalizeY",
                "groupBy": None,
                "basis": None,
            },
        )

    def test_transform_pack_opts(self):
        obj = TransformPackOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "pack",
                "padding": None,
                "direction": None,
            },
        )

    def test_transform_sample_opts(self):
        obj = TransformSampleOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sample",
                "groupBy": None,
                "thresholds": None,
                "strategy": None,
            },
        )

    def test_transform_select_opts(self):
        obj = TransformSelectOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "select",
                "groupBy": None,
                "channel": None,
                "selector": None,
            },
        )

    def test_transform_select_x_opts(self):
        obj = TransformSelectXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "selectX",
                "groupBy": None,
                "selector": None,
            },
        )

    def test_transform_select_y_opts(self):
        obj = TransformSelectYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "selectY",
                "groupBy": None,
                "selector": None,
            },
        )

    def test_transform_sort_color_opts(self):
        obj = TransformSortColorOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sortColor",
                "reverse": None,
                "by": None,
                "slice": None,
                "reducer": None,
            },
        )

    def test_transform_sort_x_opts(self):
        obj = TransformSortXOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sortX",
                "reverse": None,
                "by": None,
                "slice": None,
                "reducer": None,
                "ordinal": None,
            },
        )

    def test_transform_sort_y_opts(self):
        obj = TransformSortYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sortY",
                "reverse": None,
                "by": None,
                "slice": None,
                "reducer": None,
            },
        )

    def test_transform_stack_enter_opts(self):
        obj = TransformStackEnterOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "stackEnter",
                "groupBy": None,
                "orderBy": None,
                "reverse": None,
                "duration": None,
                "reducer": None,
            },
        )

    def test_transform_stack_y_opts(self):
        obj = TransformStackYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "stackY",
                "groupBy": None,
                "orderBy": None,
                "y": None,
                "y1": None,
                "reverse": None,
                "series": None,
            },
        )

    def test_transform_symmetry_y_opts(self):
        obj = TransformSymmetryYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "symmetryY",
                "groupBy": None,
            },
        )

    def test_coordinate_fisheye_opts(self):
        obj = CoordinateFishEyeOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "fisheye",
                "focusX": None,
                "focusY": None,
                "distortionX": None,
                "distortionY": None,
                "visual": None,
            },
        )

    def test_coordinate_parallel_opts(self):
        obj = CoordinateParallelOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "parallel",
            },
        )

    def test_coordinate_polar_opts(self):
        obj = CoordinatePolarOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "polar",
                "startAngle": None,
                "endAngle": None,
                "innerRadius": None,
                "outerRadius": None,
            },
        )

    def test_coordinate_radial_opts(self):
        obj = CoordinateRadialOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "radial",
                "startAngle": None,
                "endAngle": None,
                "innerRadius": None,
                "outerRadius": None,
            },
        )

    def test_coordinate_theta_opts(self):
        obj = CoordinateThetaOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "theta",
                "startAngle": None,
                "endAngle": None,
                "innerRadius": None,
                "outerRadius": None,
            },
        )

    def test_coordinate_transpose_opts(self):
        obj = CoordinateTransposeOpts()
        self.assertEqual(
            obj.opts,
            {
                "transform": [{"type": "transpose"}],
            },
        )

    def test_coordinate_cartesian3d_opts(self):
        obj = CoordinateCartesian3DOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "cartesian3D",
            },
        )

    def test_animate_properties_opts(self):
        obj = AnimatePropertiesOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": None,
                "duration": None,
                "delay": None,
                "easing": None,
            },
        )

    def test_animate_opts(self):
        obj = AnimateOpts()
        self.assertEqual(
            obj.opts,
            {
                "enter": None,
                "update": None,
                "exit": None,
            },
        )

    def test_title_opts(self):
        obj = TitleOpts()
        self.assertEqual(
            obj.opts,
            {
                "size": None,
                "title": None,
                "subtitle": None,
                "align": None,
                "spacing": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleFill": None,
                "titleFillOpacity": None,
                "titleStroke": None,
                "titleLineWidth": None,
                "titleStrokeOpacity": None,
                "subtitleFontSize": None,
                "subtitleFontFamily": None,
                "subtitleFontWeight": None,
                "subtitleFill": None,
                "subtitleFillOpacity": None,
                "subtitleStroke": None,
                "subtitleLineWidth": None,
                "subtitleStrokeOpacity": None,
            },
        )

    def test_axis_title_opts(self):
        # Test with all parameters
        axis_title_opts = AxisTitleOpts(
            title="Test Title",
            title_spacing=10,
            title_position="left",
            title_font_size=14,
            title_font_family="Arial",
            title_font_weight=600,
            title_stroke="black",
            title_stroke_opacity=0.5,
        )
        self.assertEqual(
            axis_title_opts.opts,
            {
                "title": "Test Title",
                "titleSpacing": 10,
                "titlePosition": "left",
                "titleFontSize": 14,
                "titleFontFamily": "Arial",
                "titleFontWeight": 600,
                "titleStroke": "black",
                "titleStrokeOpacity": 0.5,
            },
        )

        # Test with some parameters
        axis_title_opts = AxisTitleOpts(title="Test Title", title_spacing=10)
        self.assertEqual(
            axis_title_opts.opts,
            {
                "title": "Test Title",
                "titleSpacing": 10,
                "titlePosition": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleStroke": None,
                "titleStrokeOpacity": None,
            },
        )

        # Test with no parameters
        axis_title_opts = AxisTitleOpts()
        self.assertEqual(
            axis_title_opts.opts,
            {
                "title": None,
                "titleSpacing": None,
                "titlePosition": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleStroke": None,
                "titleStrokeOpacity": None,
            },
        )

    def test_axis_line_opts(self):
        # Test with all parameters
        axis_line_opts = AxisLineOpts(
            is_show_line=True,
            is_show_arrow=False,
            line_extension=[1, 2],
            line_arrow="arrow_func",
            line_arrow_offset=5,
            line_arrow_size=10,
            line_width=2,
            line_dash=[3, 4],
            line_stroke="blue",
            line_stroke_opacity=0.8,
        )
        self.assertEqual(
            axis_line_opts.opts,
            {
                "line": True,
                "arrow": False,
                "lineExtension": [1, 2],
                "lineArrow": "arrow_func",
                "lineArrowOffset": 5,
                "lineArrowSize": 10,
                "lineLineWidth": 2,
                "lineLineDash": [3, 4],
                "lineStroke": "blue",
                "lineStrokeOpacity": 0.8,
            },
        )

        # Test with some parameters
        axis_line_opts = AxisLineOpts(is_show_line=True, line_width=2)
        self.assertEqual(
            axis_line_opts.opts,
            {
                "line": True,
                "arrow": None,
                "lineExtension": None,
                "lineArrow": None,
                "lineArrowOffset": None,
                "lineArrowSize": None,
                "lineLineWidth": 2,
                "lineLineDash": None,
                "lineStroke": None,
                "lineStrokeOpacity": None,
            },
        )

        # Test with no parameters
        axis_line_opts = AxisLineOpts()
        self.assertEqual(
            axis_line_opts.opts,
            {
                "line": None,
                "arrow": None,
                "lineExtension": None,
                "lineArrow": None,
                "lineArrowOffset": None,
                "lineArrowSize": None,
                "lineLineWidth": None,
                "lineLineDash": None,
                "lineStroke": None,
                "lineStrokeOpacity": None,
            },
        )

    def test_axis_tick_opts(self):
        # Test with all parameters
        axis_tick_opts = AxisTickOpts(
            is_show_tick=True,
            tick_filter="filter_func",
            tick_formatter="formatter_func",
            tick_direction="up",
            tick_length=5,
            tick_line_width=2,
            tick_line_dash=[3, 4],
            tick_stroke="green",
            tick_stroke_opacity=0.7,
        )
        self.assertEqual(
            axis_tick_opts.opts,
            {
                "tick": True,
                "tickFilter": "filter_func",
                "tickFormatter": "formatter_func",
                "tickDirection": "up",
                "tickLength": 5,
                "tickLineWidth": 2,
                "tickLineDash": [3, 4],
                "tickStroke": "green",
                "tickStrokeOpacity": 0.7,
            },
        )

        # Test with some parameters
        axis_tick_opts = AxisTickOpts(is_show_tick=True, tick_length=5)
        self.assertEqual(
            axis_tick_opts.opts,
            {
                "tick": True,
                "tickFilter": None,
                "tickFormatter": None,
                "tickDirection": None,
                "tickLength": 5,
                "tickLineWidth": None,
                "tickLineDash": None,
                "tickStroke": None,
                "tickStrokeOpacity": None,
            },
        )

        # Test with no parameters
        axis_tick_opts = AxisTickOpts()
        self.assertEqual(
            axis_tick_opts.opts,
            {
                "tick": None,
                "tickFilter": None,
                "tickFormatter": None,
                "tickDirection": None,
                "tickLength": None,
                "tickLineWidth": None,
                "tickLineDash": None,
                "tickStroke": None,
                "tickStrokeOpacity": None,
            },
        )

    def test_axis_label_opts(self):
        # Test with all parameters
        axis_label_opts = AxisLabelOpts(
            is_show_label=True,
            label_opacity=0.9,
            label_filter="filter_func",
            label_formatter="formatter_func",
            transform=[1, 2, 3],
            label_auto_hide=True,
            label_auto_rotate=False,
            label_auto_ellipsis=True,
            label_auto_wrap=False,
            label_align="center",
            label_direction="horizontal",
            label_spacing=10,
            label_line_width=2,
            label_line_dash=[3, 4],
            label_font_size=12,
            label_font_family="Arial",
            label_font_weight=500,
            label_fill="red",
            label_fill_opacity=0.8,
            label_stroke="black",
            label_stroke_opacity=0.7,
        )
        self.assertEqual(
            axis_label_opts.opts,
            {
                "label": True,
                "labelOpacity": 0.9,
                "labelFilter": "filter_func",
                "labelFormatter": "formatter_func",
                "transform": [1, 2, 3],
                "labelAutoHide": True,
                "labelAutoRotate": False,
                "labelAutoEllipsis": True,
                "labelAutoWrap": False,
                "labelAlign": "center",
                "labelDirection": "horizontal",
                "labelSpacing": 10,
                "labelLineWidth": 2,
                "labelLineDash": [3, 4],
                "labelFontSize": 12,
                "labelFontFamily": "Arial",
                "labelFontWeight": 500,
                "labelFill": "red",
                "labelFillOpacity": 0.8,
                "labelStroke": "black",
                "labelStrokeOpacity": 0.7,
            },
        )

        # Test with some parameters
        axis_label_opts = AxisLabelOpts(is_show_label=True, label_opacity=0.9)
        self.assertEqual(
            axis_label_opts.opts,
            {
                "label": True,
                "labelOpacity": 0.9,
                "labelFilter": None,
                "labelFormatter": None,
                "transform": None,
                "labelAutoHide": None,
                "labelAutoRotate": None,
                "labelAutoEllipsis": None,
                "labelAutoWrap": None,
                "labelAlign": None,
                "labelDirection": None,
                "labelSpacing": None,
                "labelLineWidth": None,
                "labelLineDash": None,
                "labelFontSize": None,
                "labelFontFamily": None,
                "labelFontWeight": None,
                "labelFill": None,
                "labelFillOpacity": None,
                "labelStroke": None,
                "labelStrokeOpacity": None,
            },
        )

        # Test with no parameters
        axis_label_opts = AxisLabelOpts()
        self.assertEqual(
            axis_label_opts.opts,
            {
                "label": None,
                "labelOpacity": None,
                "labelFilter": None,
                "labelFormatter": None,
                "transform": None,
                "labelAutoHide": None,
                "labelAutoRotate": None,
                "labelAutoEllipsis": None,
                "labelAutoWrap": None,
                "labelAlign": None,
                "labelDirection": None,
                "labelSpacing": None,
                "labelLineWidth": None,
                "labelLineDash": None,
                "labelFontSize": None,
                "labelFontFamily": None,
                "labelFontWeight": None,
                "labelFill": None,
                "labelFillOpacity": None,
                "labelStroke": None,
                "labelStrokeOpacity": None,
            },
        )

    def test_axis_grid_opts(self):
        # Test with all parameters
        axis_grid_opts = AxisGridOpts(
            is_show_grid=True,
            grid_filter="filter_func",
            grid_length=5,
            grid_area_fill="fill_func",
            grid_line_width=2,
            grid_line_dash=[3, 4],
            grid_stroke="blue",
            grid_stroke_opacity=0.8,
        )
        self.assertEqual(
            axis_grid_opts.opts,
            {
                "grid": True,
                "gridFilter": "filter_func",
                "gridLength": 5,
                "gridAreaFill": "fill_func",
                "gridLineWidth": 2,
                "gridLineDash": [3, 4],
                "gridStroke": "blue",
                "gridStrokeOpacity": 0.8,
            },
        )

        # Test with some parameters
        axis_grid_opts = AxisGridOpts(is_show_grid=True, grid_length=5)
        self.assertEqual(
            axis_grid_opts.opts,
            {
                "grid": True,
                "gridFilter": None,
                "gridLength": 5,
                "gridAreaFill": None,
                "gridLineWidth": None,
                "gridLineDash": None,
                "gridStroke": None,
                "gridStrokeOpacity": None,
            },
        )

        # Test with no parameters
        axis_grid_opts = AxisGridOpts()
        self.assertEqual(
            axis_grid_opts.opts,
            {
                "grid": None,
                "gridFilter": None,
                "gridLength": None,
                "gridAreaFill": None,
                "gridLineWidth": None,
                "gridLineDash": None,
                "gridStroke": None,
                "gridStrokeOpacity": None,
            },
        )

    def test_effect_timing_opts(self):
        # Test with all parameters
        effect_timing_opts = EffectTimingOpts(
            delay=100,
            duration=500,
            easing="ease-in-out",
            end_delay=200,
            fill="fill_func",
        )
        self.assertEqual(
            effect_timing_opts.opts,
            {
                "delay": 100,
                "duration": 500,
                "easing": "ease-in-out",
                "endDelay": 200,
                "fill": "fill_func",
            },
        )

        # Test with some parameters
        effect_timing_opts = EffectTimingOpts(delay=100, duration=500)
        self.assertEqual(
            effect_timing_opts.opts,
            {
                "delay": 100,
                "duration": 500,
                "easing": None,
                "endDelay": None,
                "fill": None,
            },
        )

        # Test with no parameters
        effect_timing_opts = EffectTimingOpts()
        self.assertEqual(
            effect_timing_opts.opts,
            {
                "delay": None,
                "duration": None,
                "easing": None,
                "endDelay": None,
                "fill": None,
            },
        )

    def test_axis_cfg_opts(self):
        obj = AxisCfgOpts(
            axis_title_opts=AxisTitleOpts(title="X Axis"),
            axis_line_opts=AxisLineOpts(is_show_line=True),
            axis_tick_opts=AxisTickOpts(is_show_tick=True),
            axis_label_opts=AxisLabelOpts(is_show_label=True),
            axis_grid_opts=AxisGridOpts(is_show_grid=True),
            animate_opts=True,
        )
        self.assertEqual(
            obj.opts,
            {
                "title": "X Axis",
                "titleSpacing": None,
                "titlePosition": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleStroke": None,
                "titleStrokeOpacity": None,
                "line": True,
                "arrow": None,
                "lineExtension": None,
                "lineArrow": None,
                "lineArrowOffset": None,
                "lineArrowSize": None,
                "lineLineWidth": None,
                "lineLineDash": None,
                "lineStroke": None,
                "lineStrokeOpacity": None,
                "tick": True,
                "tickFilter": None,
                "tickFormatter": None,
                "tickDirection": None,
                "tickLength": None,
                "tickLineWidth": None,
                "tickLineDash": None,
                "tickStroke": None,
                "tickStrokeOpacity": None,
                "label": True,
                "labelOpacity": None,
                "labelFilter": None,
                "labelFormatter": None,
                "transform": None,
                "labelAutoHide": None,
                "labelAutoRotate": None,
                "labelAutoEllipsis": None,
                "labelAutoWrap": None,
                "labelAlign": None,
                "labelDirection": None,
                "labelSpacing": None,
                "labelLineWidth": None,
                "labelLineDash": None,
                "labelFontSize": None,
                "labelFontFamily": None,
                "labelFontWeight": None,
                "labelFill": None,
                "labelFillOpacity": None,
                "labelStroke": None,
                "labelStrokeOpacity": None,
                "grid": True,
                "gridFilter": None,
                "gridLength": None,
                "gridAreaFill": None,
                "gridLineWidth": None,
                "gridLineDash": None,
                "gridStroke": None,
                "gridStrokeOpacity": None,
                "animate": True,
            },
        )

    def test_axis_opts(self):
        xaxis_opts = AxisCfgOpts()
        yaxis_opts = AxisCfgOpts()
        obj = AxisOpts(x_axis_opts=xaxis_opts, y_axis_opts=yaxis_opts)
        self.assertEqual(obj.opts, {"x": xaxis_opts, "y": yaxis_opts})

    def test_state_opts(self):
        obj = StateOpts(
            active_style_opts=None,
            inactive_style_opts=None,
            selected_style_opts=None,
            unselected_style_opts=None,
        )
        self.assertEqual(
            obj.opts,
            {
                "active": None,
                "inactive": None,
                "selected": None,
                "unselected": None,
            },
        )

    def test_scroll_bar_style_opts(self):
        obj = ScrollBarStyleOpts(is_round=True, padding=10)
        self.assertEqual(
            obj.opts,
            {
                "isRound": True,
                "padding": 10,
                "thumbFill": None,
                "thumbFillOpacity": None,
                "thumbStroke": None,
                "thumbStrokeOpacity": None,
                "trackSize": None,
                "trackFill": None,
                "trackFillOpacity": None,
                "trackStroke": None,
                "trackStrokeOpacity": None,
            },
        )

    def test_scroll_bar_cfg_opts(self):
        obj = ScrollBarCfgOpts(
            ratio=0.5, value=20, is_slidable=True, is_scrollable=True
        )
        self.assertEqual(
            obj.opts,
            {
                "ratio": 0.5,
                "value": 20,
                "slidable": True,
                "scrollable": True,
                "style": None,
            },
        )

    def test_scroll_bar_opts(self):
        xscroll_bar_opts = ScrollBarCfgOpts()
        yscroll_bar_opts = ScrollBarCfgOpts()
        obj = ScrollBarOpts(
            x_scroll_bar_opts=xscroll_bar_opts,
            y_scroll_bar_opts=yscroll_bar_opts,
        )
        self.assertEqual(
            obj.opts,
            {"x": xscroll_bar_opts, "y": yscroll_bar_opts},
        )

    def test_slider_style_opts(self):
        obj = SliderStyleOpts(padding=10, selection_fill="red")
        self.assertEqual(
            obj.opts,
            {
                "padding": 10,
                "selectionFill": "red",
                "selectionFillOpacity": None,
                "selectionStroke": None,
                "selectionStrokeOpacity": None,
                "trackFill": None,
                "trackFillOpacity": None,
                "trackStroke": None,
                "trackStrokeOpacity": None,
                "handleIconSize": None,
                "handleIconFill": None,
                "handleIconFillOpacity": None,
                "handleIconStroke": None,
                "handleIconStrokeOpacity": None,
                "handleLabelFontSize": None,
                "handleLabelFontWeight": None,
                "handleLabelStroke": None,
                "handleLabelStrokeOpacity": None,
            },
        )

    def test_slider_cfg_opts(self):
        obj = SliderCfgOpts(values=10, is_slidable=True, is_brushable=True)
        self.assertEqual(
            obj.opts,
            {
                "values": 10,
                "slidable": True,
                "brushable": True,
                "showHandle": None,
                "showLabel": None,
                "showLabelOnInteraction": None,
                "autoFitLabel": None,
                "formatter": None,
                "sparklineType": None,
                "sparklineIsStack": None,
                "sparklineRange": None,
                "sparklineColor": None,
                "sparklineSmooth": None,
                "sparklineLineStroke": None,
                "sparklineLineStrokeOpacity": None,
                "sparklineLineLineDash": None,
                "sparklineAreaFill": None,
                "sparklineAreaFillOpacity": None,
                "sparklineColumnFill": None,
                "sparklineColumnFillOpacity": None,
                "sparklineIsGroup": None,
                "sparklineSpacing": None,
                "style": None,
            },
        )

    def test_slider_opts(self):
        x_slider_opts = SliderCfgOpts()
        y_slider_opts = SliderCfgOpts()
        obj = SliderOpts(x_slider_opts=x_slider_opts, y_slider_opts=y_slider_opts)
        self.assertEqual(obj.opts, {"x": x_slider_opts, "y": y_slider_opts})

    def test_legend_title_opts(self):
        obj = LegendTitleOpts()
        self.assertEqual(
            obj.opts,
            {
                "title": None,
                "titleSpacing": None,
                "titleInset": None,
                "titlePosition": None,
                "titleFontSize": None,
                "titleFontFamily": None,
                "titleFontWeight": None,
                "titleFill": None,
                "titleFillOpacity": None,
                "titleStroke": None,
                "titleStrokeOpacity": None,
            },
        )

    def test_legend_layout_opts(self):
        obj = LegendLayoutOpts()
        self.assertEqual(
            obj.opts,
            {
                "cols": None,
                "colPadding": None,
                "rowPadding": None,
                "maxRows": None,
                "maxCols": None,
                "justifyContent": None,
                "alignItems": None,
                "flexDirection": None,
            },
        )

    def test_legend_category_cfg_opts(self):
        obj = LegendCategoryCfgOpts()
        self.assertEqual(
            obj.opts,
            {
                "position": None,
                "itemMarker": None,
                "itemMarkerFill": None,
                "itemMarkerFillOpacity": None,
                "itemMarkerStroke": None,
                "itemMarkerStrokeOpacity": None,
                "itemLabelText": None,
                "itemLabelFontSize": None,
                "itemLabelFontFamily": None,
                "itemLabelFontWeight": None,
                "itemLabelFill": None,
                "itemLabelFillOpacity": None,
                "itemLabelStroke": None,
                "itemLabelStrokeOpacity": None,
                "itemValueText": None,
                "itemValueFontSize": None,
                "itemValueFontFamily": None,
                "itemValueFontWeight": None,
                "itemValueFill": None,
                "itemValueFillOpacity": None,
                "itemValueStroke": None,
                "itemValueStrokeOpacity": None,
                "itemSpan": None,
                "itemSpacing": None,
                "itemBackgroundFill": None,
                "itemBackgroundFillOpacity": None,
                "navEffect": None,
                "navDuration": None,
                "navOrientation": None,
                "navDefaultPage": None,
                "navLoop": None,
                "navPageNumFill": None,
                "navPageNumFontSize": None,
                "navPageNumOpacity": None,
                "navPageNumStroke": None,
                "navPageNumStrokeOpacity": None,
                "navButtonFill": None,
                "navButtonOpacity": None,
                "navButtonStroke": None,
                "navButtonStrokeOpacity": None,
                "navFormatter": None,
            },
        )

        obj = LegendCategoryCfgOpts(
            title_opts=LegendTitleOpts(title_spacing=1),
            layout_opts=LegendLayoutOpts(justify_content="center"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "title": {"titleSpacing": 1},
                "layout": {"justifyContent": "center"},
            },
        )

    def test_legend_category_opts(self):
        obj = LegendCategoryOpts()
        self.assertEqual(
            obj.opts,
            {
                "color": None,
                "size": None,
            },
        )

    def test_legend_axis_opts(self):
        obj = LegendAxisOpts()
        self.assertEqual(
            obj.opts,
            {
                "color": None,
                "block": None,
                "type": None,
                "ribbonSize": None,
                "ribbonFill": None,
                "ribbonFillOpacity": None,
                "ribbonStroke": None,
                "ribbonStrokeOpacity": None,
                "handle": None,
                "handleLabel": None,
                "handleFormatter": None,
                "slidable": None,
                "range": None,
                "step": None,
                "handleMarkerFill": None,
                "handleMarkerFillOpacity": None,
                "handleMarkerStroke": None,
                "handleMarkerStrokeOpacity": None,
                "handleLabelFontSize": None,
                "handleLabelFontFamily": None,
                "handleLabelFontWeight": None,
                "handleLabelFill": None,
                "handleLabelFillOpacity": None,
                "handleLabelStroke": None,
                "handleLabelStrokeOpacity": None,
                "label": None,
                "labelFormatter": None,
                "labelFilter": None,
                "labelDirection": None,
                "labelSpacing": None,
                "labelAlign": None,
                "labelFontSize": None,
                "labelFontFamily": None,
                "labelFontWeight": None,
                "labelStroke": None,
                "labelStrokeOpacity": None,
                "indicator": None,
                "indicatorFormatter": None,
                "indicatorLabelFontSize": None,
                "indicatorLabelFontFamily": None,
                "indicatorLabelFontWeight": None,
                "indicatorLabelStroke": None,
                "indicatorLabelStrokeOpacity": None,
                "indicatorBackgroundFill": None,
                "indicatorBackgroundFillOpacity": None,
                "indicatorBackgroundStroke": None,
                "indicatorBackgroundStrokeOpacity": None,
            },
        )

        obj = LegendAxisOpts(
            title_opts=LegendTitleOpts(title_spacing=1),
            layout_opts=LegendLayoutOpts(justify_content="center"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "title": {"titleSpacing": 1},
                "layout": {"justifyContent": "center"},
            },
        )

    def test_legend_continuous_opts(self):
        obj = LegendContinuousOpts()
        self.assertEqual(
            obj.opts,
            {
                "x": None,
                "y": None,
            },
        )

    def test_tooltip_item_opts(self):
        obj = TooltipItemOpts()
        self.assertEqual(
            obj.opts,
            {
                "field": None,
                "channel": None,
                "valueFormatter": None,
                "name": None,
            },
        )

    def test_tooltip_opts(self):
        obj = TooltipOpts()
        self.assertEqual(
            obj.opts,
            {
                "title": None,
                "items": None,
            },
        )

    def test_label_transform_contrast_reverse_opts(self):
        obj = LabelTransformContrastReverseOpts()
        self.assertEqual(
            obj.opts, {"type": "contrastReverse", "threshold": None, "palette": None}
        )

    def test_label_transform_overflow_hide_opts(self):
        obj = LabelTransformOverflowHideOpts()
        self.assertEqual(obj.opts, {"type": "overflowHide"})

    def test_label_transform_overlap_dodge_y_opts(self):
        obj = LabelTransformOverlapDodgeYOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "overlapDodgeY",
                "maxIterations": None,
                "padding": None,
                "maxError": None,
            },
        )

    def test_label_transform_overlap_hide_opts(self):
        obj = LabelTransformOverlapHideOpts()
        self.assertEqual(obj.opts, {"type": "overflowHide"})

    def test_label_transform_exceed_adjust_opts(self):
        obj = LabelTransformExceedAdjustOpts()
        self.assertEqual(obj.opts, {"type": "exceedAdjust"})

    def test_label_opts(self):
        obj = LabelOpts()
        self.assertEqual(
            obj.opts,
            {
                "text": None,
                "fontSize": None,
                "fontFamily": None,
                "fontWeight": None,
                "lineHeight": None,
                "textAlign": None,
                "textBaseline": None,
                "fill": None,
                "fillOpacity": None,
                "stroke": None,
                "strokeOpacity": None,
                "lineWidth": None,
                "lineDash": None,
                "opacity": None,
                "shadowColor": None,
                "shadowBlur": None,
                "shadowOffsetX": None,
                "shadowOffsetY": None,
                "cursor": None,
                "position": None,
                "connector": None,
                "background": None,
                "transform": None,
                "formatter": None,
                "selector": None,
                "render": None,
                "style": None,
            },
        )

        obj = LabelOpts(
            connector_style_opts=BaseChartStyleOpts(opacity=0.75),
            background_style_opts=BaseChartStyleOpts(opacity=0.75),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "connectorOpacity": 0.75,
                "backgroundOpacity": 0.75,
            }
        )

    def test_interaction_mask_style_opts(self):
        obj = InteractionMaskStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "maskFill": None,
                "maskFillOpacity": None,
                "maskStroke": None,
                "maskStrokeOpacity": None,
                "maskLineWidth": None,
                "maskLineDash": None,
                "maskOpacity": None,
                "maskShadowColor": None,
                "maskShadowOffsetX": None,
                "maskShadowOffsetY": None,
                "maskCursor": None,
            },
        )

    def test_interaction_brush_axis_highlight_opts(self):
        obj = InteractionBrushAxisHighlightOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
            },
        )

        obj = InteractionBrushAxisHighlightOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_filter_opts(self):
        obj = InteractionBrushFilterOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
            },
        )

        obj = InteractionBrushFilterOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_highlight_opts(self):
        obj = InteractionBrushHighlightOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
                "series": None,
                "facet": None,
            },
        )

        obj = InteractionBrushHighlightOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_x_filter_opts(self):
        obj = InteractionBrushXFilterOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
            },
        )

        obj = InteractionBrushXFilterOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_x_highlight_opts(self):
        obj = InteractionBrushXHighlightOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
                "series": None,
                "facet": None,
            },
        )

        obj = InteractionBrushXHighlightOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_y_filter_opts(self):
        obj = InteractionBrushYFilterOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
            },
        )

        obj = InteractionBrushYFilterOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_brush_y_highlight_opts(self):
        obj = InteractionBrushYHighlightOpts()
        self.assertEqual(
            obj.opts,
            {
                "reverse": None,
                "series": None,
                "facet": None,
            },
        )

        obj = InteractionBrushYHighlightOpts(
            mask_style_opts=InteractionMaskStyleOpts(mask_fill="black"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "maskFill": "black",
            },
        )

    def test_interaction_rule_style_opts(self):
        obj = InteractionRuleStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "ruleFill": None,
                "ruleFillOpacity": None,
                "ruleStroke": None,
                "ruleStrokeOpacity": None,
                "ruleLineWidth": None,
                "ruleLineDash": None,
                "ruleOpacity": None,
                "ruleShadowColor": None,
                "ruleShadowOffsetX": None,
                "ruleShadowOffsetY": None,
                "ruleCursor": None,
            },
        )

    def test_interaction_label_style_opts(self):
        obj = InteractionLabelStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "labelFill": None,
                "labelFillOpacity": None,
                "labelStroke": None,
                "labelStrokeOpacity": None,
                "labelLineWidth": None,
                "labelLineDash": None,
                "labelOpacity": None,
                "labelShadowColor": None,
                "labelShadowOffsetX": None,
                "labelShadowOffsetY": None,
                "labelCursor": None,
            },
        )

    def test_interaction_chart_index_opts(self):
        obj = InteractionChartIndexOpts()
        self.assertEqual(
            obj.opts,
            {
                "labelFormatter": None,
            },
        )

        obj = InteractionChartIndexOpts(
            rule_style_opts=InteractionRuleStyleOpts(rule_fill="#000"),
            label_style_opts=InteractionLabelStyleOpts(label_fill="#000"),
        )

        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "labelFill": "#000",
                "ruleFill": "#000",
            },
        )

    def test_interaction_background_style_opts(self):
        obj = InteractionBackgroundStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "backgroundFill": None,
                "backgroundFillOpacity": None,
                "backgroundStroke": None,
                "backgroundStrokeOpacity": None,
                "backgroundLineWidth": None,
                "backgroundLineDash": None,
                "backgroundOpacity": None,
                "backgroundShadowColor": None,
                "backgroundShadowOffsetX": None,
                "backgroundShadowOffsetY": None,
                "backgroundCursor": None,
            },
        )

    def test_interaction_element_highlight_opts(self):
        obj = InteractionElementHighlightOpts()
        self.assertEqual(
            obj.opts,
            {
                "background": None,
                "offset": None,
            },
        )

        obj = InteractionElementHighlightOpts(
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000"
            ),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
            },
        )

    def test_interaction_link_style_opts(self):
        obj = InteractionLinkStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "linkFill": None,
                "linkFillOpacity": None,
                "linkStroke": None,
                "linkStrokeOpacity": None,
                "linkLineWidth": None,
                "linkLineDash": None,
                "linkOpacity": None,
                "linkShadowColor": None,
                "linkShadowOffsetX": None,
                "linkShadowOffsetY": None,
                "linkCursor": None,
            },
        )

    def test_interaction_element_highlight_by_color_opts(self):
        obj = InteractionElementHighlightByColorOpts()
        self.assertEqual(
            obj.opts,
            {
                "link": None,
                "background": None,
                "offset": None,
            },
        )

        obj = InteractionElementHighlightByColorOpts(
            link_style_opts=InteractionLinkStyleOpts(link_fill="#000"),
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000",
            ),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
                "linkFill": "#000",
            },
        )

    def test_interaction_element_highlight_by_x_opts(self):
        obj = InteractionElementHighlightByXOpts()
        self.assertEqual(
            obj.opts,
            {
                "background": None,
                "offset": None,
            },
        )

        obj = InteractionElementHighlightByXOpts(
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000",
            )
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
            },
        )

    def test_interaction_element_select_opts(self):
        obj = InteractionElementSelectOpts()
        self.assertEqual(
            obj.opts,
            {
                "background": None,
                "offset": None,
                "single": None,
            },
        )

        obj = InteractionElementSelectOpts(
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000",
            )
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
            },
        )

    def test_interaction_element_select_by_color_opts(self):
        obj = InteractionElementSelectByColorOpts()
        self.assertEqual(
            obj.opts,
            {
                "link": None,
                "background": None,
                "offset": None,
            },
        )

        obj = InteractionElementSelectByColorOpts(
            link_style_opts=InteractionLinkStyleOpts(link_fill="#000"),
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000",
            ),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
                "linkFill": "#000",
            },
        )

    def test_interaction_element_select_by_x_opts(self):
        obj = InteractionElementSelectByXOpts()
        self.assertEqual(
            obj.opts,
            {
                "link": None,
                "background": None,
                "offset": None,
                "single": None,
            },
        )

        obj = InteractionElementSelectByXOpts(
            link_style_opts=InteractionLinkStyleOpts(link_fill="#000"),
            background_style_opts=InteractionBackgroundStyleOpts(
                background_fill="#000",
            ),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "backgroundFill": "#000",
                "linkFill": "#000",
            },
        )

    def test_interaction_fish_eye_opts(self):
        obj = InteractionFishEyeOpts()
        self.assertEqual(
            obj.opts,
            {
                "wait": None,
                "leading": None,
                "trailing": None,
            },
        )

    def test_interaction_legend_filter_opts(self):
        obj = InteractionLegendFilterOpts()
        self.assertEqual(obj.opts, {})

    def test_interaction_legend_highlight_opts(self):
        obj = InteractionLegendHighlightOpts()
        self.assertEqual(obj.opts, {})

    def test_interaction_tip_style_opts(self):
        obj = InteractionTipStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "tipFill": None,
                "tipFillOpacity": None,
                "tipStroke": None,
                "tipStrokeOpacity": None,
                "tipLineWidth": None,
                "tipLineDash": None,
                "tipOpacity": None,
                "tipShadowColor": None,
                "tipShadowOffsetX": None,
                "tipShadowOffsetY": None,
                "tipCursor": None,
            },
        )

    def test_interaction_pop_tip_opts(self):
        obj = InteractionPopTipOpts()
        self.assertEqual(
            obj.opts,
            {
                "offsetX": None,
                "offsetY": None,
            },
        )

        obj = InteractionPopTipOpts(
            tip_style_opts=InteractionTipStyleOpts(tip_fill="#000"),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "tipFill": "#000",
            },
        )

    def test_interaction_tooltip_bbox_opts(self):
        obj = InteractionTooltipBBoxOpts()
        self.assertEqual(
            obj.opts,
            {
                "x": None,
                "y": None,
                "width": None,
                "height": None,
            },
        )

    def test_interaction_cross_hairs_style_opts(self):
        obj = InteractionCrossHairsStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "crosshairsFill": None,
                "crosshairsFillOpacity": None,
                "crosshairsStroke": None,
                "crosshairsStrokeOpacity": None,
                "crosshairsLineWidth": None,
                "crosshairsLineDash": None,
                "crosshairsOpacity": None,
                "crosshairsShadowColor": None,
                "crosshairsShadowOffsetX": None,
                "crosshairsShadowOffsetY": None,
                "crosshairsCursor": None,
            },
        )

    def test_interaction_cross_hairs_x_style_opts(self):
        obj = InteractionCrossHairsXStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "crosshairsXFill": None,
                "crosshairsXFillOpacity": None,
                "crosshairsXStroke": None,
                "crosshairsXStrokeOpacity": None,
                "crosshairsXLineWidth": None,
                "crosshairsXLineDash": None,
                "crosshairsXOpacity": None,
                "crosshairsXShadowColor": None,
                "crosshairsXShadowOffsetX": None,
                "crosshairsXShadowOffsetY": None,
                "crosshairsXCursor": None,
            },
        )

    def test_interaction_cross_hairs_y_style_opts(self):
        obj = InteractionCrossHairsYStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "crosshairsYFill": None,
                "crosshairsYFillOpacity": None,
                "crosshairsYStroke": None,
                "crosshairsYStrokeOpacity": None,
                "crosshairsYLineWidth": None,
                "crosshairsYLineDash": None,
                "crosshairsYOpacity": None,
                "crosshairsYShadowColor": None,
                "crosshairsYShadowOffsetX": None,
                "crosshairsYShadowOffsetY": None,
                "crosshairsYCursor": None,
            },
        )

    def test_interaction_marker_style_opts(self):
        obj = InteractionMarkerStyleOpts()
        self.assertEqual(
            obj.opts,
            {
                "markerFill": None,
                "markerFillOpacity": None,
                "markerStroke": None,
                "markerStrokeOpacity": None,
                "markerLineWidth": None,
                "markerLineDash": None,
                "markerOpacity": None,
                "markerShadowColor": None,
                "markerShadowOffsetX": None,
                "markerShadowOffsetY": None,
                "markerCursor": None,
            },
        )

    def test_interaction_tooltip_opts(self):
        obj = InteractionTooltipOpts()
        self.assertEqual(
            obj.opts,
            {
                "wait": None,
                "leading": None,
                "trailing": None,
                "shared": None,
                "series": None,
                "body": None,
                "marker": None,
                "groupName": None,
                "position": None,
                "mount": None,
                "bounding": None,
                "offset": None,
                "crosshairs": None,
                "crosshairsX": None,
                "crosshairsY": None,
                "markerType": None,
                "render": None,
                "sort": None,
                "filter": None,
                "disableNative": None,
                "css": None,
            },
        )

        obj = InteractionTooltipOpts(
            crosshairs_style_opts=InteractionCrossHairsStyleOpts(
                crosshairs_fill="#000",
            ),
        )
        self.assertEqual(
            remove_key_with_none_value(obj.opts),
            {
                "crosshairsFill": "#000",
            },
        )

    def test_interaction_opts(self):
        # Test with no options provided
        obj = InteractionOpts()
        self.assertEqual(
            obj.opts,
            {
                "brushAxisHighlight": None,
                "brushFilter": None,
                "brushHighlight": None,
                "brushXFilter": None,
                "brushXHighlight": None,
                "brushYFilter": None,
                "brushYHighlight": None,
                "chartIndex": None,
                "elementHighlight": None,
                "elementHighlightByColor": None,
                "elementHighlightByX": None,
                "elementSelect": None,
                "elementSelectByColor": None,
                "elementSelectByX": None,
                "fisheye": None,
                "legendFilter": None,
                "legendHighlight": None,
                "poptip": None,
                "tooltip": None,
            },
        )

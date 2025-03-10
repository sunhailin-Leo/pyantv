from ..globals import CurrentConfig
from ..options.series_options import (
    BasicOpts,
    JSFunc,
    Numeric,
    Optional,
    Union,
    Sequence,
)


class BaseChartStyleOpts(BasicOpts):
    def __init__(
        self,
        text: Optional[JSFunc] = None,
        text_align: Optional[JSFunc] = None,
        position: Optional[JSFunc] = None,
        fill: Optional[JSFunc] = None,
        fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        stroke: Optional[JSFunc] = None,
        stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        line_width: Optional[Union[Numeric, JSFunc]] = None,
        line_dash: Optional[Union[Sequence, JSFunc]] = None,
        line_cap: Optional[JSFunc] = None,
        opacity: Optional[Union[Numeric, JSFunc]] = None,
        shadow_color: Optional[JSFunc] = None,
        shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        cursor: Optional[JSFunc] = None,
        dx: Optional[Union[Numeric, JSFunc]] = None,
        dy: Optional[Union[Numeric, JSFunc]] = None,
        inset: Optional[Numeric] = None,
        radius: Optional[Numeric] = None,
        background: Optional[Union[bool, JSFunc]] = None,
        background_fill: Optional[JSFunc] = None,
        font_weight: Optional[Union[Numeric, JSFunc]] = None,
        font_size: Optional[Union[Numeric, JSFunc]] = None,
        spacing: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "text": text,
            "textAlign": text_align,
            "position": position,
            "fill": fill,
            "fillOpacity": fill_opacity,
            "stroke": stroke,
            "strokeOpacity": stroke_opacity,
            "lineWidth": line_width,
            "lineDash": line_dash,
            "lineCap": line_cap,
            "opacity": opacity,
            "shadowColor": shadow_color,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "cursor": cursor,
            "dx": dx,
            "dy": dy,
            "inset": inset,
            "radius": radius,
            "background": background,
            "backgroundFill": background_fill,
            "fontWeight": font_weight,
            "fontSize": font_size,
            "spacing": spacing,
        }


class BaseChartRadiusInsetStyleOpts(BasicOpts):
    def __init__(
        self,
        radius: Optional[Union[Numeric, JSFunc]] = None,
        radius_top_left: Optional[Union[Numeric, JSFunc]] = None,
        radius_top_right: Optional[Union[Numeric, JSFunc]] = None,
        radius_bottom_left: Optional[Union[Numeric, JSFunc]] = None,
        radius_bottom_right: Optional[Union[Numeric, JSFunc]] = None,
        inner_radius_top_left: Optional[Union[Numeric, JSFunc]] = None,
        inner_radius_top_right: Optional[Union[Numeric, JSFunc]] = None,
        inner_radius_bottom_left: Optional[Union[Numeric, JSFunc]] = None,
        inner_radius_bottom_right: Optional[Union[Numeric, JSFunc]] = None,
        inset: Optional[Union[Numeric, JSFunc]] = None,
        inset_left: Optional[Union[Numeric, JSFunc]] = None,
        inset_right: Optional[Union[Numeric, JSFunc]] = None,
        inset_bottom: Optional[Union[Numeric, JSFunc]] = None,
        inset_top: Optional[Union[Numeric, JSFunc]] = None,
    ):
        self.opts: dict = {
            "radius": radius,
            "radiusTopLeft": radius_top_left,
            "radiusTopRight": radius_top_right,
            "radiusBottomLeft": radius_bottom_left,
            "radiusBottomRight": radius_bottom_right,
            "innerRadiusTopLeft": inner_radius_top_left,
            "innerRadiusTopRight": inner_radius_top_right,
            "innerRadiusBottomLeft": inner_radius_bottom_left,
            "innerRadiusBottomRight": inner_radius_bottom_right,
            "inset": inset,
            "insetLeft": inset_left,
            "insetRight": inset_right,
            "insetBottom": inset_bottom,
            "insetTop": inset_top,
        }


class InitOpts(BasicOpts):
    def __init__(
        self,
        width: str = "900px",
        height: str = "500px",
        is_horizontal_center: bool = False,
        page_title: str = CurrentConfig.PAGE_TITLE,
        bg_color: Union[str, dict] = None,
        is_fill_bg_color: bool = False,
        js_host: str = "",
        is_embed_js: bool = False,
    ):
        self.opts: dict = {
            "width": width,
            "height": height,
            "is_horizontal_center": is_horizontal_center,
            "page_title": page_title,
            "bg_color": bg_color,
            "fill_bg": is_fill_bg_color,
            "js_host": js_host,
            "is_embed_js": is_embed_js,
        }


class RenderOpts(BasicOpts):
    def __init__(
        self,
        container: JSFunc = None,
        is_auto_fit: Optional[bool] = None,
        theme: Optional[Union[JSFunc, dict]] = None,
        padding: Optional[Numeric] = None,
        padding_left: Optional[Numeric] = None,
        padding_right: Optional[Numeric] = None,
        padding_top: Optional[Numeric] = None,
        padding_bottom: Optional[Numeric] = None,
        margin: Optional[Numeric] = None,
        margin_left: Optional[Numeric] = None,
        margin_right: Optional[Numeric] = None,
        margin_top: Optional[Numeric] = None,
        margin_bottom: Optional[Numeric] = None,
        ratio: Optional[Sequence[Numeric]] = None,
        direction: Optional[str] = None,
        iteration_count: Optional[Numeric] = None,
        duration: Optional[Numeric] = None,
        inset_left: Optional[Numeric] = None,
        inset_right: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "container": container,
            "autoFit": is_auto_fit,
            "theme": theme,
            "padding": padding,
            "paddingLeft": padding_left,
            "paddingRight": padding_right,
            "paddingTop": padding_top,
            "paddingBottom": padding_bottom,
            "margin": margin,
            "marginLeft": margin_left,
            "marginRight": margin_right,
            "marginTop": margin_top,
            "marginBottom": margin_bottom,
            "ratio": ratio,
            "direction": direction,
            "iterationCount": iteration_count,
            "duration": duration,
            "insetLeft": inset_left,
            "insetRight": inset_right,
        }


class ScaleBaseOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Numeric] = None,
        is_independent: Optional[bool] = None,
        key: Optional[str] = None,
        range_: Optional[Sequence] = None,
        is_zero: Optional[bool] = None,
    ):
        self.opts: dict = {
            "padding": padding,
            "independent": is_independent,
            "key": key,
            "range": range_,
            "zero": is_zero,
        }


class ScaleBandOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence] = None,
        range_: Optional[Sequence] = None,
        unknown: Optional[str] = None,
        is_round: Optional[bool] = None,
        padding_inner: Optional[Numeric] = None,
        padding_outer: Optional[Numeric] = None,
        align: Optional[Numeric] = None,
        compare: Optional[JSFunc] = None,
        flex: Optional[Sequence[Numeric]] = None,
    ):
        self.opts: dict = {
            "type": "band",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
            "round": is_round,
            "paddingInner": padding_inner,
            "paddingOuter": padding_outer,
            "align": align,
            "compare": compare,
            "flex": flex,
        }


class ScaleLinearOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        domain_min: Optional[Numeric] = None,
        domain_max: Optional[Numeric] = None,
        range_: Optional[Sequence] = None,
        range_min: Optional[Union[Numeric, str]] = None,
        range_max: Optional[Union[Numeric, str]] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_round: Optional[bool] = None,
        is_clamp: Optional[bool] = None,
        is_nice: Optional[bool] = None,
        interpolate: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "linear",
            "domain": domain,
            "domainMin": domain_min,
            "domainMax": domain_max,
            "range": range_,
            "rangeMin": range_min,
            "rangeMax": range_max,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "round": is_round,
            "clamp": is_clamp,
            "nice": is_nice,
            "interpolate": interpolate,
        }


class ScaleLogOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        domain_min: Optional[Numeric] = None,
        domain_max: Optional[Numeric] = None,
        range_: Optional[Sequence] = None,
        range_min: Optional[Union[Numeric, str]] = None,
        range_max: Optional[Union[Numeric, str]] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_round: Optional[bool] = None,
        is_clamp: Optional[bool] = None,
        is_nice: Optional[bool] = None,
        interpolate: Optional[JSFunc] = None,
        base: Optional[Numeric] = 10,
    ):
        self.opts: dict = {
            "type": "log",
            "domain": domain,
            "domainMin": domain_min,
            "domainMax": domain_max,
            "range": range_,
            "rangeMin": range_min,
            "rangeMax": range_max,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "round": is_round,
            "clamp": is_clamp,
            "nice": is_nice,
            "interpolate": interpolate,
            "base": base,
        }


class ScaleOrdinalOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Union[Sequence]] = None,
        range_: Optional[Union[Sequence]] = None,
        unknown: Optional[str] = None,
        compare: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "ordinal",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
            "compare": compare,
        }


class ScalePointOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence] = None,
        range_: Optional[Sequence] = None,
        unknown: Optional[str] = None,
        is_round: Optional[bool] = None,
        padding_inner: Optional[Numeric] = None,
        padding_outer: Optional[Numeric] = None,
        padding: Optional[Numeric] = None,
        align: Optional[Numeric] = None,
        compare: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "point",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
            "round": is_round,
            "paddingInner": padding_inner,
            "paddingOuter": padding_outer,
            "padding": padding,
            "align": align,
            "compare": compare,
        }


class ScalePowOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        domain_min: Optional[Numeric] = None,
        domain_max: Optional[Numeric] = None,
        range_: Optional[Sequence] = None,
        range_min: Optional[Union[Numeric, str]] = None,
        range_max: Optional[Union[Numeric, str]] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_round: Optional[bool] = None,
        is_clamp: Optional[bool] = None,
        is_nice: Optional[bool] = None,
        interpolate: Optional[JSFunc] = None,
        exponent: Optional[Numeric] = 2,
    ):
        self.opts: dict = {
            "type": "pow",
            "domain": domain,
            "domainMin": domain_min,
            "domainMax": domain_max,
            "range": range_,
            "rangeMin": range_min,
            "rangeMax": range_max,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "round": is_round,
            "clamp": is_clamp,
            "nice": is_nice,
            "interpolate": interpolate,
            "exponent": exponent,
        }


class ScaleQuantileOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        range_: Optional[Sequence] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_nice: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "quantile",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "nice": is_nice,
        }


class ScaleQuantizeOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        range_: Optional[Sequence] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_nice: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "quantize",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "nice": is_nice,
        }


class ScaleSqrtOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        domain_min: Optional[Numeric] = None,
        domain_max: Optional[Numeric] = None,
        range_: Optional[Sequence] = None,
        range_min: Optional[Union[Numeric, str]] = None,
        range_max: Optional[Union[Numeric, str]] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_round: Optional[bool] = None,
        is_clamp: Optional[bool] = None,
        is_nice: Optional[bool] = None,
        interpolate: Optional[JSFunc] = None,
        exponent: Optional[Numeric] = 0.5,
    ):
        self.opts: dict = {
            "type": "sqrt",
            "domain": domain,
            "domainMin": domain_min,
            "domainMax": domain_max,
            "range": range_,
            "rangeMin": range_min,
            "rangeMax": range_max,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickMethod": tick_method,
            "round": is_round,
            "clamp": is_clamp,
            "nice": is_nice,
            "interpolate": interpolate,
            "exponent": exponent,
        }


class ScaleThresholdOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        range_: Optional[Sequence] = None,
        unknown: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "threshold",
            "domain": domain,
            "range": range_,
            "unknown": unknown,
        }


class ScaleTimeOpts(BasicOpts):
    def __init__(
        self,
        domain: Optional[Sequence[Numeric]] = None,
        domain_min: Optional[Numeric] = None,
        domain_max: Optional[Numeric] = None,
        range_: Optional[Sequence] = None,
        range_min: Optional[Union[Numeric, str]] = None,
        range_max: Optional[Union[Numeric, str]] = None,
        unknown: Optional[str] = None,
        tick_count: Optional[Numeric] = None,
        tick_interval: Optional[Numeric] = None,
        tick_method: Optional[JSFunc] = None,
        is_round: Optional[bool] = None,
        is_clamp: Optional[bool] = None,
        is_nice: Optional[bool] = None,
        mask: Optional[str] = None,
        is_utc: Optional[bool] = None,
        interpolate: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "time",
            "domain": domain,
            "domainMin": domain_min,
            "domainMax": domain_max,
            "range": range_,
            "rangeMin": range_min,
            "rangeMax": range_max,
            "unknown": unknown,
            "tickCount": tick_count,
            "tickInterval": tick_interval,
            "tickMethod": tick_method,
            "round": is_round,
            "clamp": is_clamp,
            "nice": is_nice,
            "mask": mask,
            "utc": is_utc,
            "interpolate": interpolate,
        }


class TransformBinOpts(BasicOpts):
    def __init__(
        self,
        thresholds_x: Optional[Numeric] = None,
        thresholds_y: Optional[Numeric] = None,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "bin",
            "thresholdsX": thresholds_x,
            "thresholdsY": thresholds_y,
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformBinXOpts(BasicOpts):
    def __init__(
        self,
        thresholds: Optional[Numeric] = None,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "binX",
            "thresholds": thresholds,
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformDiffXOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        is_series: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "diffY",
            "groupBy": group_by,
            "series": is_series,
        }


class TransformDodgeXOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        is_reverse: Optional[bool] = None,
        order_by: Optional[JSFunc] = None,
        padding: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "dodgeX",
            "groupBy": group_by,
            "reverse": is_reverse,
            "orderBy": order_by,
            "padding": padding,
        }


class TransformFlexXOpts(BasicOpts):
    def __init__(
        self,
        field: Optional[JSFunc] = None,
        channel: Optional[str] = None,
        reducer: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "flexX",
            "field": field,
            "channel": channel,
            "reducer": reducer,
        }


class TransformGroupOpts(BasicOpts):
    def __init__(
        self,
        channels: Optional[Union[str, Sequence[str]]] = None,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "group",
            "channels": channels,
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformGroupColorOpts(BasicOpts):
    def __init__(
        self,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "groupColor",
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformGroupXOpts(BasicOpts):
    def __init__(
        self,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "groupX",
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformGroupYOpts(BasicOpts):
    def __init__(
        self,
        channel_name: Optional[str] = None,
        channel_transform: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "groupY",
        }
        if channel_name:
            self.opts[channel_name] = channel_transform


class TransformJitterOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Numeric] = None,
        padding_x: Optional[Numeric] = None,
        padding_y: Optional[Numeric] = None,
        random: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "jitter",
            "padding": padding,
            "paddingX": padding_x,
            "paddingY": padding_y,
            "random": random,
        }


class TransformJitterXOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Numeric] = None,
        random: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "jitterX",
            "padding": padding,
            "random": random,
        }


class TransformJitterYOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Numeric] = None,
        random: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "jitterY",
            "padding": padding,
            "random": random,
        }


class TransformNormalizeYOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        basis: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "normalizeY",
            "groupBy": group_by,
            "basis": basis,
        }


class TransformPackOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Numeric] = None,
        direction: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "pack",
            "padding": padding,
            "direction": direction,
        }


class TransformSampleOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        thresholds: Optional[Numeric] = None,
        strategy: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "sample",
            "groupBy": group_by,
            "thresholds": thresholds,
            "strategy": strategy,
        }


class TransformSelectOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        channel: Optional[str] = None,
        selector: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "select",
            "groupBy": group_by,
            "channel": channel,
            "selector": selector,
        }


class TransformSelectXOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        selector: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "selectX",
            "groupBy": group_by,
            "selector": selector,
        }


class TransformSelectYOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        selector: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "selectY",
            "groupBy": group_by,
            "selector": selector,
        }


class TransformSortColorOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        by: Optional[str] = None,
        slice_: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        reducer: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "sortColor",
            "reverse": is_reverse,
            "by": by,
            "slice": slice_,
            "reducer": reducer,
        }


class TransformSortXOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        by: Optional[str] = None,
        slice_: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        reducer: Optional[str] = None,
        is_ordinal: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "sortX",
            "reverse": is_reverse,
            "by": by,
            "slice": slice_,
            "reducer": reducer,
            "ordinal": is_ordinal,
        }


class TransformSortYOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        by: Optional[str] = None,
        slice_: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        reducer: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "sortY",
            "reverse": is_reverse,
            "by": by,
            "slice": slice_,
            "reducer": reducer,
        }


class TransformStackEnterOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        order_by: Optional[str] = None,
        is_reverse: Optional[bool] = None,
        duration: Optional[Numeric] = None,
        reducer: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "stackEnter",
            "groupBy": group_by,
            "orderBy": order_by,
            "reverse": is_reverse,
            "duration": duration,
            "reducer": reducer,
        }


class TransformStackYOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
        order_by: Optional[str] = None,
        y_: Optional[str] = None,
        y1_: Optional[str] = None,
        is_reverse: Optional[bool] = None,
        is_series: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "stackY",
            "groupBy": group_by,
            "orderBy": order_by,
            "y": y_,
            "y1": y1_,
            "reverse": is_reverse,
            "series": is_series,
        }


class TransformSymmetryYOpts(BasicOpts):
    def __init__(
        self,
        group_by: Optional[Union[str, Sequence[str]]] = None,
    ):
        self.opts: dict = {
            "type": "symmetryY",
            "groupBy": group_by,
        }


class CoordinateFishEyeOpts(BasicOpts):
    def __init__(
        self,
        focus_x: Optional[Numeric] = None,
        focus_y: Optional[Numeric] = None,
        distortion_x: Optional[Numeric] = None,
        distortion_y: Optional[Numeric] = None,
        is_visual: Optional[bool] = None,
    ):
        self.opts: dict = {
            "type": "fisheye",
            "focusX": focus_x,
            "focusY": focus_y,
            "distortionX": distortion_x,
            "distortionY": distortion_y,
            "visual": is_visual,
        }


class CoordinateParallelOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {
            "type": "parallel",
        }


class CoordinatePolarOpts(BasicOpts):
    def __init__(
        self,
        start_angle: Optional[Numeric] = None,
        end_angle: Optional[Numeric] = None,
        inner_radius: Optional[Numeric] = None,
        outer_radius: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "polar",
            "startAngle": start_angle,
            "endAngle": end_angle,
            "innerRadius": inner_radius,
            "outerRadius": outer_radius,
        }


class CoordinateRadialOpts(BasicOpts):
    def __init__(
        self,
        start_angle: Optional[Numeric] = None,
        end_angle: Optional[Numeric] = None,
        inner_radius: Optional[Numeric] = None,
        outer_radius: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "radial",
            "startAngle": start_angle,
            "endAngle": end_angle,
            "innerRadius": inner_radius,
            "outerRadius": outer_radius,
        }


class CoordinateThetaOpts(BasicOpts):
    def __init__(
        self,
        start_angle: Optional[Numeric] = None,
        end_angle: Optional[Numeric] = None,
        inner_radius: Optional[Numeric] = None,
        outer_radius: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "theta",
            "startAngle": start_angle,
            "endAngle": end_angle,
            "innerRadius": inner_radius,
            "outerRadius": outer_radius,
        }


class CoordinateTransposeOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {
            "transform": [{"type": "transpose"}],
        }


class CoordinateCartesian3DOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {
            "type": "cartesian3D",
        }


class AnimatePropertiesOpts(BasicOpts):
    def __init__(
        self,
        type_: Optional[str] = None,
        duration: Optional[Numeric] = None,
        delay: Optional[Numeric] = None,
        easing: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": type_,
            "duration": duration,
            "delay": delay,
            "easing": easing,
        }


class AnimateOpts(BasicOpts):
    def __init__(
        self,
        enter_opts: Optional[AnimatePropertiesOpts] = None,
        update_opts: Optional[AnimatePropertiesOpts] = None,
        exit_opts: Optional[AnimatePropertiesOpts] = None,
    ):
        self.opts: dict = {
            "enter": enter_opts,
            "update": update_opts,
            "exit": exit_opts,
        }


class TitleOpts(BasicOpts):
    def __init__(
        self,
        size: Optional[Numeric] = None,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        align: Optional[str] = None,
        spacing: Optional[Numeric] = None,
        title_font_size: Optional[Numeric] = None,
        title_font_family: Optional[str] = None,
        title_font_weight: Optional[Numeric] = None,
        title_fill: Optional[JSFunc] = None,
        title_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        title_stroke: Optional[JSFunc] = None,
        title_line_width: Optional[Union[Numeric, JSFunc]] = None,
        title_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        subtitle_font_size: Optional[Numeric] = None,
        subtitle_font_family: Optional[Numeric] = None,
        subtitle_font_weight: Optional[Numeric] = None,
        subtitle_fill: Optional[JSFunc] = None,
        subtitle_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        subtitle_stroke: Optional[JSFunc] = None,
        subtitle_line_width: Optional[Union[Numeric, JSFunc]] = None,
        subtitle_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
    ):
        self.opts: dict = {
            "size": size,
            "title": title,
            "subtitle": subtitle,
            "align": align,
            "spacing": spacing,
            "titleFontSize": title_font_size,
            "titleFontFamily": title_font_family,
            "titleFontWeight": title_font_weight,
            "titleFill": title_fill,
            "titleFillOpacity": title_fill_opacity,
            "titleStroke": title_stroke,
            "titleLineWidth": title_line_width,
            "titleStrokeOpacity": title_stroke_opacity,
            "subtitleFontSize": subtitle_font_size,
            "subtitleFontFamily": subtitle_font_family,
            "subtitleFontWeight": subtitle_font_weight,
            "subtitleFill": subtitle_fill,
            "subtitleFillOpacity": subtitle_fill_opacity,
            "subtitleStroke": subtitle_stroke,
            "subtitleLineWidth": subtitle_line_width,
            "subtitleStrokeOpacity": subtitle_stroke_opacity,
        }


class AxisTitleOpts(BasicOpts):
    def __init__(
        self,
        title: Optional[Union[bool, Numeric, JSFunc]] = None,
        title_spacing: Optional[Numeric] = None,
        title_position: Optional[str] = None,
        title_font_size: Optional[Numeric] = None,
        title_font_family: Optional[str] = None,
        title_font_weight: Optional[Numeric] = None,
        title_stroke: Optional[str] = None,
        title_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "title": title,
            "titleSpacing": title_spacing,
            "titlePosition": title_position,
            "titleFontSize": title_font_size,
            "titleFontFamily": title_font_family,
            "titleFontWeight": title_font_weight,
            "titleStroke": title_stroke,
            "titleStrokeOpacity": title_stroke_opacity,
        }


class AxisLineOpts(BasicOpts):
    def __init__(
        self,
        is_show_line: Optional[bool] = None,
        is_show_arrow: Optional[bool] = None,
        line_extension: Optional[Sequence[Numeric]] = None,
        line_arrow: Optional[JSFunc] = None,
        line_arrow_offset: Optional[Numeric] = None,
        line_arrow_size: Optional[Numeric] = None,
        line_width: Optional[Numeric] = None,
        line_dash: Optional[Sequence[Numeric]] = None,
        line_stroke: Optional[str] = None,
        line_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "line": is_show_line,
            "arrow": is_show_arrow,
            "lineExtension": line_extension,
            "lineArrow": line_arrow,
            "lineArrowOffset": line_arrow_offset,
            "lineArrowSize": line_arrow_size,
            "lineLineWidth": line_width,
            "lineLineDash": line_dash,
            "lineStroke": line_stroke,
            "lineStrokeOpacity": line_stroke_opacity,
        }


class AxisTickOpts(BasicOpts):
    def __init__(
        self,
        is_show_tick: Optional[bool] = None,
        tick_filter: Optional[JSFunc] = None,
        tick_formatter: Optional[JSFunc] = None,
        tick_direction: Optional[str] = None,
        tick_length: Optional[Union[JSFunc, Numeric]] = None,
        tick_line_width: Optional[Union[JSFunc, Numeric]] = None,
        tick_line_dash: Optional[Union[JSFunc, Sequence[Numeric]]] = None,
        tick_stroke: Optional[Union[JSFunc]] = None,
        tick_stroke_opacity: Optional[Union[JSFunc, Numeric]] = None,
    ):
        self.opts: dict = {
            "tick": is_show_tick,
            "tickFilter": tick_filter,
            "tickFormatter": tick_formatter,
            "tickDirection": tick_direction,
            "tickLength": tick_length,
            "tickLineWidth": tick_line_width,
            "tickLineDash": tick_line_dash,
            "tickStroke": tick_stroke,
            "tickStrokeOpacity": tick_stroke_opacity,
        }


class AxisLabelOpts(BasicOpts):
    def __init__(
        self,
        is_show_label: Optional[bool] = None,
        label_opacity: Optional[Union[JSFunc, Numeric]] = None,
        label_filter: Optional[JSFunc] = None,
        label_formatter: Optional[JSFunc] = None,
        transform: Optional[Sequence] = None,
        label_auto_hide: Optional[Union[bool, dict]] = None,
        label_auto_rotate: Optional[Union[bool, dict]] = None,
        label_auto_ellipsis: Optional[Union[bool, dict]] = None,
        label_auto_wrap: Optional[Union[bool, dict]] = None,
        label_align: Optional[str] = None,
        label_direction: Optional[str] = None,
        label_spacing: Optional[Numeric] = None,
        label_line_width: Optional[Union[JSFunc, Numeric]] = None,
        label_line_dash: Optional[Union[JSFunc, Sequence[Numeric]]] = None,
        label_font_size: Optional[Union[JSFunc, Numeric]] = None,
        label_font_family: Optional[JSFunc] = None,
        label_font_weight: Optional[Union[JSFunc, Numeric]] = None,
        label_fill: Optional[Union[JSFunc]] = None,
        label_fill_opacity: Optional[Union[JSFunc, Numeric]] = None,
        label_stroke: Optional[Union[JSFunc]] = None,
        label_stroke_opacity: Optional[Union[JSFunc, Numeric]] = None,
    ):
        self.opts: dict = {
            "label": is_show_label,
            "labelOpacity": label_opacity,
            "labelFilter": label_filter,
            "labelFormatter": label_formatter,
            "transform": transform,
            "labelAutoHide": label_auto_hide,
            "labelAutoRotate": label_auto_rotate,
            "labelAutoEllipsis": label_auto_ellipsis,
            "labelAutoWrap": label_auto_wrap,
            "labelAlign": label_align,
            "labelDirection": label_direction,
            "labelSpacing": label_spacing,
            "labelLineWidth": label_line_width,
            "labelLineDash": label_line_dash,
            "labelFontSize": label_font_size,
            "labelFontFamily": label_font_family,
            "labelFontWeight": label_font_weight,
            "labelFill": label_fill,
            "labelFillOpacity": label_fill_opacity,
            "labelStroke": label_stroke,
            "labelStrokeOpacity": label_stroke_opacity,
        }


class AxisGridOpts(BasicOpts):
    def __init__(
        self,
        is_show_grid: Optional[bool] = None,
        grid_filter: Optional[JSFunc] = None,
        grid_length: Optional[Union[JSFunc, Numeric]] = None,
        grid_area_fill: Optional[JSFunc] = None,
        grid_line_width: Optional[Numeric] = None,
        grid_line_dash: Optional[Sequence[Numeric]] = None,
        grid_stroke: Optional[str] = None,
        grid_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "grid": is_show_grid,
            "gridFilter": grid_filter,
            "gridLength": grid_length,
            "gridAreaFill": grid_area_fill,
            "gridLineWidth": grid_line_width,
            "gridLineDash": grid_line_dash,
            "gridStroke": grid_stroke,
            "gridStrokeOpacity": grid_stroke_opacity,
        }


class EffectTimingOpts(BasicOpts):
    def __init__(
        self,
        delay: Optional[Numeric] = None,
        duration: Optional[Numeric] = None,
        easing: Optional[str] = None,
        end_delay: Optional[Numeric] = None,
        fill: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "delay": delay,
            "duration": duration,
            "easing": easing,
            "endDelay": end_delay,
            "fill": fill,
        }


class AxisCfgOpts(BasicOpts):
    def __init__(
        self,
        axis_title_opts: Optional[Union[AxisTitleOpts, bool]] = None,
        axis_line_opts: Optional[Union[AxisLineOpts, bool]] = None,
        axis_tick_opts: Optional[Union[AxisTickOpts, bool]] = None,
        axis_label_opts: Optional[Union[AxisLabelOpts, bool]] = None,
        axis_grid_opts: Optional[Union[AxisGridOpts, bool]] = None,
        animate_opts: Optional[Union[EffectTimingOpts, bool]] = None,
    ):
        self.opts: dict = {"animate": animate_opts}

        if axis_title_opts:
            self.opts.update(axis_title_opts.opts)
        if axis_line_opts:
            self.opts.update(axis_line_opts.opts)
        if axis_tick_opts:
            self.opts.update(axis_tick_opts.opts)
        if axis_label_opts:
            self.opts.update(axis_label_opts.opts)
        if axis_grid_opts:
            self.opts.update(axis_grid_opts.opts)


class AxisOpts(BasicOpts):
    def __init__(
        self,
        x_axis_opts: Optional[Union[AxisCfgOpts, bool]] = None,
        y_axis_opts: Optional[Union[AxisCfgOpts, bool]] = None,
    ):
        self.opts: dict = {
            "x": x_axis_opts,
            "y": y_axis_opts,
        }


class StateOpts(BasicOpts):
    def __init__(
        self,
        active_style_opts: Optional[BaseChartStyleOpts] = None,
        inactive_style_opts: Optional[BaseChartStyleOpts] = None,
        selected_style_opts: Optional[BaseChartStyleOpts] = None,
        unselected_style_opts: Optional[BaseChartStyleOpts] = None,
    ):
        self.opts: dict = {
            "active": active_style_opts,
            "inactive": inactive_style_opts,
            "selected": selected_style_opts,
            "unselected": unselected_style_opts,
        }


class ScrollBarStyleOpts(BasicOpts):
    def __init__(
        self,
        is_round: Optional[bool] = None,
        padding: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        thumb_fill: Optional[str] = None,
        thumb_fill_opacity: Optional[Numeric] = None,
        thumb_stroke: Optional[str] = None,
        thumb_stroke_opacity: Optional[Numeric] = None,
        track_size: Optional[Numeric] = None,
        track_fill: Optional[str] = None,
        track_fill_opacity: Optional[Numeric] = None,
        track_stroke: Optional[str] = None,
        track_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "isRound": is_round,
            "padding": padding,
            "thumbFill": thumb_fill,
            "thumbFillOpacity": thumb_fill_opacity,
            "thumbStroke": thumb_stroke,
            "thumbStrokeOpacity": thumb_stroke_opacity,
            "trackSize": track_size,
            "trackFill": track_fill,
            "trackFillOpacity": track_fill_opacity,
            "trackStroke": track_stroke,
            "trackStrokeOpacity": track_stroke_opacity,
        }


class ScrollBarCfgOpts(BasicOpts):
    def __init__(
        self,
        ratio: Optional[Numeric] = None,
        value: Optional[Numeric] = None,
        is_slidable: Optional[bool] = None,
        is_scrollable: Optional[bool] = None,
        style_opts: Optional[ScrollBarStyleOpts] = None,
    ):
        self.opts: dict = {
            "ratio": ratio,
            "value": value,
            "slidable": is_slidable,
            "scrollable": is_scrollable,
            "style": style_opts,
        }


class ScrollBarOpts(BasicOpts):
    def __init__(
        self,
        x_scroll_bar_opts: Optional[ScrollBarCfgOpts] = None,
        y_scroll_bar_opts: Optional[ScrollBarCfgOpts] = None,
    ):
        self.opts: dict = {
            "x": x_scroll_bar_opts,
            "y": y_scroll_bar_opts,
        }


class SliderStyleOpts(BasicOpts):
    def __init__(
        self,
        padding: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        selection_fill: Optional[str] = None,
        selection_fill_opacity: Optional[Numeric] = None,
        selection_stroke: Optional[str] = None,
        selection_stroke_opacity: Optional[Numeric] = None,
        track_fill: Optional[str] = None,
        track_fill_opacity: Optional[Numeric] = None,
        track_stroke: Optional[str] = None,
        track_stroke_opacity: Optional[Numeric] = None,
        handle_icon_size: Optional[Numeric] = None,
        handle_icon_fill: Optional[Numeric] = None,
        handle_icon_fill_opacity: Optional[Numeric] = None,
        handle_icon_stroke: Optional[str] = None,
        handle_icon_stroke_opacity: Optional[Numeric] = None,
        handle_label_font_size: Optional[Numeric] = None,
        handle_label_font_weight: Optional[Union[Numeric, str]] = None,
        handle_label_stroke: Optional[str] = None,
        handle_label_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "padding": padding,
            "selectionFill": selection_fill,
            "selectionFillOpacity": selection_fill_opacity,
            "selectionStroke": selection_stroke,
            "selectionStrokeOpacity": selection_stroke_opacity,
            "trackFill": track_fill,
            "trackFillOpacity": track_fill_opacity,
            "trackStroke": track_stroke,
            "trackStrokeOpacity": track_stroke_opacity,
            "handleIconSize": handle_icon_size,
            "handleIconFill": handle_icon_fill,
            "handleIconFillOpacity": handle_icon_fill_opacity,
            "handleIconStroke": handle_icon_stroke,
            "handleIconStrokeOpacity": handle_icon_stroke_opacity,
            "handleLabelFontSize": handle_label_font_size,
            "handleLabelFontWeight": handle_label_font_weight,
            "handleLabelStroke": handle_label_stroke,
            "handleLabelStrokeOpacity": handle_label_stroke_opacity,
        }


class SliderCfgOpts(BasicOpts):
    def __init__(
        self,
        values: Optional[Numeric] = None,
        is_slidable: Optional[bool] = None,
        is_brushable: Optional[bool] = None,
        is_show_handle: Optional[bool] = None,
        is_show_handle_label: Optional[bool] = None,
        is_show_label_on_interaction: Optional[bool] = None,
        is_auto_fit_label: Optional[bool] = None,
        formatter: Optional[JSFunc] = None,
        spark_line_type: Optional[str] = None,
        spark_line_is_stack: Optional[bool] = None,
        spark_line_range: Optional[Sequence[Numeric]] = None,
        spark_line_color: Optional[Union[Sequence[str], JSFunc]] = None,
        is_spark_line_smooth: Optional[bool] = None,
        spark_line_stroke: Optional[str] = None,
        spark_line_stroke_opacity: Optional[Numeric] = None,
        spark_line_dash: Optional[Sequence[Numeric]] = None,
        spark_line_area_fill: Optional[str] = None,
        spark_line_area_fill_opacity: Optional[Numeric] = None,
        spark_line_column_fill: Optional[str] = None,
        spark_line_column_fill_opacity: Optional[Numeric] = None,
        spark_line_is_group: Optional[bool] = None,
        spark_line_spacing: Optional[Numeric] = None,
        style_opts: Optional[SliderStyleOpts] = None,
    ):
        self.opts: dict = {
            "values": values,
            "slidable": is_slidable,
            "brushable": is_brushable,
            "showHandle": is_show_handle,
            "showLabel": is_show_handle_label,
            "showLabelOnInteraction": is_show_label_on_interaction,
            "autoFitLabel": is_auto_fit_label,
            "formatter": formatter,
            "sparklineType": spark_line_type,
            "sparklineIsStack": spark_line_is_stack,
            "sparklineRange": spark_line_range,
            "sparklineColor": spark_line_color,
            "sparklineSmooth": is_spark_line_smooth,
            "sparklineLineStroke": spark_line_stroke,
            "sparklineLineStrokeOpacity": spark_line_stroke_opacity,
            "sparklineLineLineDash": spark_line_dash,
            "sparklineAreaFill": spark_line_area_fill,
            "sparklineAreaFillOpacity": spark_line_area_fill_opacity,
            "sparklineColumnFill": spark_line_column_fill,
            "sparklineColumnFillOpacity": spark_line_column_fill_opacity,
            "sparklineIsGroup": spark_line_is_group,
            "sparklineSpacing": spark_line_spacing,
            "style": style_opts,
        }


class SliderOpts(BasicOpts):
    def __init__(
        self,
        x_slider_opts: Optional[SliderCfgOpts] = None,
        y_slider_opts: Optional[SliderCfgOpts] = None,
    ):
        self.opts: dict = {
            "x": x_slider_opts,
            "y": y_slider_opts,
        }


class LegendTitleOpts(BasicOpts):
    def __init__(
        self,
        title: Optional[Union[bool, str]] = None,
        title_spacing: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        title_inset: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        title_position: Optional[str] = None,
        title_font_size: Optional[Numeric] = None,
        title_font_family: Optional[str] = None,
        title_font_weight: Optional[Numeric] = None,
        title_fill: Optional[str] = None,
        title_fill_opacity: Optional[Numeric] = None,
        title_stroke: Optional[str] = None,
        title_stroke_opacity: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "title": title,
            "titleSpacing": title_spacing,
            "titleInset": title_inset,
            "titlePosition": title_position,
            "titleFontSize": title_font_size,
            "titleFontFamily": title_font_family,
            "titleFontWeight": title_font_weight,
            "titleFill": title_fill,
            "titleFillOpacity": title_fill_opacity,
            "titleStroke": title_stroke,
            "titleStrokeOpacity": title_stroke_opacity,
        }


class LegendLayoutOpts(BasicOpts):
    def __init__(
        self,
        cols: Optional[Numeric] = None,
        col_padding: Optional[Numeric] = None,
        row_padding: Optional[Numeric] = None,
        max_rows: Optional[Numeric] = None,
        max_cols: Optional[Numeric] = None,
        justify_content: Optional[str] = None,
        align_items: Optional[str] = None,
        flex_direction: Optional[str] = None,
    ):
        self.opts: dict = {
            "cols": cols,
            "colPadding": col_padding,
            "rowPadding": row_padding,
            "maxRows": max_rows,
            "maxCols": max_cols,
            "justifyContent": justify_content,
            "alignItems": align_items,
            "flexDirection": flex_direction,
        }


class LegendCategoryCfgOpts(BasicOpts):
    def __init__(
        self,
        position: Optional[str] = None,
        item_marker: Optional[JSFunc] = None,
        item_marker_fill: Optional[JSFunc] = None,
        item_marker_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_marker_stroke: Optional[JSFunc] = None,
        item_marker_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_label_text: Optional[JSFunc] = None,
        item_label_font_size: Optional[Union[Numeric, JSFunc]] = None,
        item_label_font_family: Optional[JSFunc] = None,
        item_label_font_weight: Optional[Union[Numeric, JSFunc]] = None,
        item_label_fill: Optional[JSFunc] = None,
        item_label_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_label_stroke: Optional[JSFunc] = None,
        item_label_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_value_text: Optional[JSFunc] = None,
        item_value_font_size: Optional[Union[Numeric, JSFunc]] = None,
        item_value_font_family: Optional[JSFunc] = None,
        item_value_font_weight: Optional[Union[Numeric, JSFunc]] = None,
        item_value_fill: Optional[JSFunc] = None,
        item_value_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_value_stroke: Optional[JSFunc] = None,
        item_value_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        item_span: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        item_spacing: Optional[Union[Numeric, Sequence[Numeric]]] = None,
        item_background_fill: Optional[str] = None,
        item_background_fill_opacity: Optional[Numeric] = None,
        nav_effect: Optional[JSFunc] = None,
        nav_duration: Optional[Numeric] = None,
        nav_orientation: Optional[str] = None,
        nav_default_page: Optional[Numeric] = None,
        is_nav_loop: Optional[bool] = None,
        nav_page_num_fill: Optional[str] = None,
        nav_page_num_font_size: Optional[Numeric] = None,
        nav_page_num_opacity: Optional[Numeric] = None,
        nav_page_num_stroke: Optional[str] = None,
        nav_page_num_stroke_opacity: Optional[Numeric] = None,
        nav_button_fill: Optional[str] = None,
        nav_button_opacity: Optional[Numeric] = None,
        nav_button_stroke: Optional[str] = None,
        nav_button_stroke_opacity: Optional[Numeric] = None,
        nav_formatter: Optional[JSFunc] = None,
        title_opts: Optional[LegendTitleOpts] = None,
        layout_opts: Optional[LegendLayoutOpts] = None,
    ):
        self.opts: dict = {
            "position": position,
            "itemMarker": item_marker,
            "itemMarkerFill": item_marker_fill,
            "itemMarkerFillOpacity": item_marker_fill_opacity,
            "itemMarkerStroke": item_marker_stroke,
            "itemMarkerStrokeOpacity": item_marker_stroke_opacity,
            "itemLabelText": item_label_text,
            "itemLabelFontSize": item_label_font_size,
            "itemLabelFontFamily": item_label_font_family,
            "itemLabelFontWeight": item_label_font_weight,
            "itemLabelFill": item_label_fill,
            "itemLabelFillOpacity": item_label_fill_opacity,
            "itemLabelStroke": item_label_stroke,
            "itemLabelStrokeOpacity": item_label_stroke_opacity,
            "itemValueText": item_value_text,
            "itemValueFontSize": item_value_font_size,
            "itemValueFontFamily": item_value_font_family,
            "itemValueFontWeight": item_value_font_weight,
            "itemValueFill": item_value_fill,
            "itemValueFillOpacity": item_value_fill_opacity,
            "itemValueStroke": item_value_stroke,
            "itemValueStrokeOpacity": item_value_stroke_opacity,
            "itemSpan": item_span,
            "itemSpacing": item_spacing,
            "itemBackgroundFill": item_background_fill,
            "itemBackgroundFillOpacity": item_background_fill_opacity,
            "navEffect": nav_effect,
            "navDuration": nav_duration,
            "navOrientation": nav_orientation,
            "navDefaultPage": nav_default_page,
            "navLoop": is_nav_loop,
            "navPageNumFill": nav_page_num_fill,
            "navPageNumFontSize": nav_page_num_font_size,
            "navPageNumOpacity": nav_page_num_opacity,
            "navPageNumStroke": nav_page_num_stroke,
            "navPageNumStrokeOpacity": nav_page_num_stroke_opacity,
            "navButtonFill": nav_button_fill,
            "navButtonOpacity": nav_button_opacity,
            "navButtonStroke": nav_button_stroke,
            "navButtonStrokeOpacity": nav_button_stroke_opacity,
            "navFormatter": nav_formatter,
        }

        if title_opts:
            self.opts.update(title=title_opts.opts)
        if layout_opts:
            self.opts.update(layout=layout_opts.opts)


class LegendCategoryOpts(BasicOpts):
    def __init__(
        self,
        color_legend_opts: Optional[Union[LegendCategoryCfgOpts, bool]] = None,
        size_legend_opts: Optional[Union[LegendCategoryCfgOpts, bool]] = None,
    ):
        self.opts: dict = {
            "color": color_legend_opts,
            "size": size_legend_opts,
        }


class LegendAxisOpts(BasicOpts):
    def __init__(
        self,
        color: Optional[Union[Sequence[str], JSFunc]] = None,
        is_block: Optional[bool] = None,
        type_: Optional[str] = None,
        ribbon_size: Optional[Numeric] = None,
        ribbon_fill: Optional[str] = None,
        ribbon_fill_opacity: Optional[Numeric] = None,
        ribbon_stroke: Optional[str] = None,
        ribbon_stroke_opacity: Optional[Numeric] = None,
        is_show_handle: Optional[bool] = None,
        is_show_handle_label: Optional[bool] = None,
        handle_formatter: Optional[JSFunc] = None,
        is_slidable: Optional[bool] = None,
        range_: Optional[Sequence[Numeric]] = None,
        step: Optional[Numeric] = None,
        handle_marker_fill: Optional[JSFunc] = None,
        handle_marker_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        handle_marker_stroke: Optional[JSFunc] = None,
        handle_marker_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        handle_label_font_size: Optional[Union[Numeric, JSFunc]] = None,
        handle_label_font_family: Optional[JSFunc] = None,
        handle_label_font_weight: Optional[Union[Numeric, JSFunc]] = None,
        handle_label_fill: Optional[JSFunc] = None,
        handle_label_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        handle_label_stroke: Optional[JSFunc] = None,
        handle_label_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        is_show_label: Optional[bool] = None,
        label_formatter: Optional[JSFunc] = None,
        label_filter: Optional[JSFunc] = None,
        label_direction: Optional[str] = None,
        label_spacing: Optional[Numeric] = None,
        label_align: Optional[str] = None,
        label_font_size: Optional[Union[Numeric, JSFunc]] = None,
        label_font_family: Optional[JSFunc] = None,
        label_font_weight: Optional[Union[Numeric, JSFunc]] = None,
        label_stroke: Optional[JSFunc] = None,
        label_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        is_show_indicator: Optional[bool] = None,
        indicator_formatter: Optional[JSFunc] = None,
        indicator_label_font_size: Optional[Union[Numeric, JSFunc]] = None,
        indicator_label_font_family: Optional[JSFunc] = None,
        indicator_label_font_weight: Optional[Union[Numeric, JSFunc]] = None,
        indicator_label_stroke: Optional[JSFunc] = None,
        indicator_label_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        indicator_background_fill: Optional[JSFunc] = None,
        indicator_background_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        indicator_background_stroke: Optional[JSFunc] = None,
        indicator_background_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        title_opts: Optional[LegendTitleOpts] = None,
        layout_opts: Optional[LegendLayoutOpts] = None,
    ):
        self.opts: dict = {
            "color": color,
            "block": is_block,
            "type": type_,
            "ribbonSize": ribbon_size,
            "ribbonFill": ribbon_fill,
            "ribbonFillOpacity": ribbon_fill_opacity,
            "ribbonStroke": ribbon_stroke,
            "ribbonStrokeOpacity": ribbon_stroke_opacity,
            "handle": is_show_handle,
            "handleLabel": is_show_handle_label,
            "handleFormatter": handle_formatter,
            "slidable": is_slidable,
            "range": range_,
            "step": step,
            "handleMarkerFill": handle_marker_fill,
            "handleMarkerFillOpacity": handle_marker_fill_opacity,
            "handleMarkerStroke": handle_marker_stroke,
            "handleMarkerStrokeOpacity": handle_marker_stroke_opacity,
            "handleLabelFontSize": handle_label_font_size,
            "handleLabelFontFamily": handle_label_font_family,
            "handleLabelFontWeight": handle_label_font_weight,
            "handleLabelFill": handle_label_fill,
            "handleLabelFillOpacity": handle_label_fill_opacity,
            "handleLabelStroke": handle_label_stroke,
            "handleLabelStrokeOpacity": handle_label_stroke_opacity,
            "label": is_show_label,
            "labelFormatter": label_formatter,
            "labelFilter": label_filter,
            "labelDirection": label_direction,
            "labelSpacing": label_spacing,
            "labelAlign": label_align,
            "labelFontSize": label_font_size,
            "labelFontFamily": label_font_family,
            "labelFontWeight": label_font_weight,
            "labelStroke": label_stroke,
            "labelStrokeOpacity": label_stroke_opacity,
            "indicator": is_show_indicator,
            "indicatorFormatter": indicator_formatter,
            "indicatorLabelFontSize": indicator_label_font_size,
            "indicatorLabelFontFamily": indicator_label_font_family,
            "indicatorLabelFontWeight": indicator_label_font_weight,
            "indicatorLabelStroke": indicator_label_stroke,
            "indicatorLabelStrokeOpacity": indicator_label_stroke_opacity,
            "indicatorBackgroundFill": indicator_background_fill,
            "indicatorBackgroundFillOpacity": indicator_background_fill_opacity,
            "indicatorBackgroundStroke": indicator_background_stroke,
            "indicatorBackgroundStrokeOpacity": indicator_background_stroke_opacity,
        }

        if title_opts:
            self.opts.update(title=title_opts.opts)
        if layout_opts:
            self.opts.update(layout=layout_opts.opts)


class LegendContinuousOpts(BasicOpts):
    def __init__(
        self,
        x_legend_opts: Optional[LegendAxisOpts] = None,
        y_legend_opts: Optional[LegendAxisOpts] = None,
    ):
        self.opts: dict = {
            "x": x_legend_opts,
            "y": y_legend_opts,
        }


class TooltipItemOpts(BasicOpts):
    def __init__(
        self,
        field: Optional[str] = None,
        channel: Optional[str] = None,
        value_formatter: Optional[str] = None,
        name: Optional[str] = None,
    ):
        self.opts: dict = {
            "field": field,
            "channel": channel,
            "valueFormatter": value_formatter,
            "name": name,
        }


class TooltipOpts(BasicOpts):
    def __init__(
        self,
        title: Optional[Union[JSFunc, dict]] = None,
        items: Optional[Sequence[Union[TooltipItemOpts, JSFunc]]] = None,
    ):
        self.opts: dict = {
            "title": title,
            "items": items,
        }


class LabelTransformContrastReverseOpts(BasicOpts):
    def __init__(
        self,
        threshold: Optional[Numeric] = None,
        palette: Optional[Union[str, Sequence[str]]] = None,
    ):
        self.opts: dict = {
            "type": "contrastReverse",
            "threshold": threshold,
            "palette": palette,
        }


class LabelTransformOverflowHideOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {"type": "overflowHide"}


class LabelTransformOverlapDodgeYOpts(BasicOpts):
    def __init__(
        self,
        max_iterations: Optional[Numeric] = None,
        padding: Optional[Numeric] = None,
        max_error: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "overlapDodgeY",
            "maxIterations": max_iterations,
            "padding": padding,
            "maxError": max_error,
        }


class LabelTransformOverlapHideOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {"type": "overflowHide"}


class LabelTransformExceedAdjustOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {"type": "exceedAdjust"}


LabelTransform = Union[
    LabelTransformContrastReverseOpts,
    LabelTransformOverflowHideOpts,
    LabelTransformOverlapDodgeYOpts,
    LabelTransformOverlapHideOpts,
    LabelTransformExceedAdjustOpts,
    dict,
]


class LabelOpts(BasicOpts):
    def __init__(
        self,
        text_opts: Optional[JSFunc] = None,
        font_size: Optional[Union[Numeric, JSFunc]] = None,
        font_family: Optional[JSFunc] = None,
        font_weight: Optional[Union[Numeric, JSFunc]] = None,
        line_height: Optional[Union[Numeric, JSFunc]] = None,
        text_align: Optional[JSFunc] = None,
        text_baseline: Optional[JSFunc] = None,
        fill: Optional[JSFunc] = None,
        fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        stroke: Optional[JSFunc] = None,
        stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        line_width: Optional[Union[Numeric, JSFunc]] = None,
        line_dash: Optional[Union[Sequence[Numeric], JSFunc]] = None,
        opacity: Optional[Union[Numeric, JSFunc]] = None,
        shadow_color: Optional[JSFunc] = None,
        shadow_blur: Optional[Union[Numeric, JSFunc]] = None,
        shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        cursor: Optional[JSFunc] = None,
        position: Optional[str] = None,
        is_connector: Optional[bool] = None,
        connector_style_opts: Optional[BaseChartStyleOpts] = None,
        is_background: Optional[bool] = None,
        background_style_opts: Optional[BaseChartStyleOpts] = None,
        transform: Optional[LabelTransform] = None,
        formatter: Optional[JSFunc] = None,
        selector: Optional[str] = None,
        render: Optional[JSFunc] = None,
        style_opts: Optional[BaseChartStyleOpts] = None,
    ):
        self.opts: dict = {
            "text": text_opts,
            "fontSize": font_size,
            "fontFamily": font_family,
            "fontWeight": font_weight,
            "lineHeight": line_height,
            "textAlign": text_align,
            "textBaseline": text_baseline,
            "fill": fill,
            "fillOpacity": fill_opacity,
            "stroke": stroke,
            "strokeOpacity": stroke_opacity,
            "lineWidth": line_width,
            "lineDash": line_dash,
            "opacity": opacity,
            "shadowColor": shadow_color,
            "shadowBlur": shadow_blur,
            "shadowOffsetX": shadow_offset_x,
            "shadowOffsetY": shadow_offset_y,
            "cursor": cursor,
            "position": position,
            "connector": is_connector,
            "background": is_background,
            "transform": transform,
            "formatter": formatter,
            "selector": selector,
            "render": render,
            "style": style_opts,
        }

        if connector_style_opts:
            connector_style_opts.opts = {
                f"connector{k[:1].upper() + k[1:]}": v
                for k, v in connector_style_opts.opts.items()
            }
            self.opts.update(connector_style_opts.opts)

        if background_style_opts:
            background_style_opts.opts = {
                f"background{k[:1].upper() + k[1:]}": v
                for k, v in background_style_opts.opts.items()
            }
            self.opts.update(background_style_opts.opts)


class InteractionMaskStyleOpts(BasicOpts):
    def __init__(
        self,
        mask_fill: Optional[JSFunc] = None,
        mask_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        mask_stroke: Optional[JSFunc] = None,
        mask_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        mask_line_width: Optional[Union[Numeric, JSFunc]] = None,
        mask_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        mask_opacity: Optional[Union[Numeric, JSFunc]] = None,
        mask_shadow_color: Optional[JSFunc] = None,
        mask_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        mask_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        mask_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "maskFill": mask_fill,
            "maskFillOpacity": mask_fill_opacity,
            "maskStroke": mask_stroke,
            "maskStrokeOpacity": mask_stroke_opacity,
            "maskLineWidth": mask_line_width,
            "maskLineDash": mask_line_dash,
            "maskOpacity": mask_opacity,
            "maskShadowColor": mask_shadow_color,
            "maskShadowOffsetX": mask_shadow_offset_x,
            "maskShadowOffsetY": mask_shadow_offset_y,
            "maskCursor": mask_cursor,
        }


class InteractionBrushAxisHighlightOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushFilterOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushHighlightOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        is_series: Optional[bool] = None,
        is_facet: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
            "series": is_series,
            "facet": is_facet,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushXFilterOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushXHighlightOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        is_series: Optional[bool] = None,
        is_facet: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
            "series": is_series,
            "facet": is_facet,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushYFilterOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionBrushYHighlightOpts(BasicOpts):
    def __init__(
        self,
        is_reverse: Optional[bool] = None,
        is_series: Optional[bool] = None,
        is_facet: Optional[bool] = None,
        mask_style_opts: Optional[InteractionMaskStyleOpts] = None,
    ):
        self.opts: dict = {
            "reverse": is_reverse,
            "series": is_series,
            "facet": is_facet,
        }

        if mask_style_opts:
            self.opts.update(mask_style_opts.opts)


class InteractionRuleStyleOpts(BasicOpts):
    def __init__(
        self,
        rule_fill: Optional[JSFunc] = None,
        rule_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        rule_stroke: Optional[JSFunc] = None,
        rule_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        rule_line_width: Optional[Union[Numeric, JSFunc]] = None,
        rule_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        rule_opacity: Optional[Union[Numeric, JSFunc]] = None,
        rule_shadow_color: Optional[JSFunc] = None,
        rule_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        rule_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        rule_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "ruleFill": rule_fill,
            "ruleFillOpacity": rule_fill_opacity,
            "ruleStroke": rule_stroke,
            "ruleStrokeOpacity": rule_stroke_opacity,
            "ruleLineWidth": rule_line_width,
            "ruleLineDash": rule_line_dash,
            "ruleOpacity": rule_opacity,
            "ruleShadowColor": rule_shadow_color,
            "ruleShadowOffsetX": rule_shadow_offset_x,
            "ruleShadowOffsetY": rule_shadow_offset_y,
            "ruleCursor": rule_cursor,
        }


class InteractionLabelStyleOpts(BasicOpts):
    def __init__(
        self,
        label_fill: Optional[JSFunc] = None,
        label_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        label_stroke: Optional[JSFunc] = None,
        label_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        label_line_width: Optional[Union[Numeric, JSFunc]] = None,
        label_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        label_opacity: Optional[Union[Numeric, JSFunc]] = None,
        label_shadow_color: Optional[JSFunc] = None,
        label_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        label_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        label_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "labelFill": label_fill,
            "labelFillOpacity": label_fill_opacity,
            "labelStroke": label_stroke,
            "labelStrokeOpacity": label_stroke_opacity,
            "labelLineWidth": label_line_width,
            "labelLineDash": label_line_dash,
            "labelOpacity": label_opacity,
            "labelShadowColor": label_shadow_color,
            "labelShadowOffsetX": label_shadow_offset_x,
            "labelShadowOffsetY": label_shadow_offset_y,
            "labelCursor": label_cursor,
        }


class InteractionChartIndexOpts(BasicOpts):
    def __init__(
        self,
        label_formatter: Optional[JSFunc] = None,
        rule_style_opts: Optional[InteractionRuleStyleOpts] = None,
        label_style_opts: Optional[InteractionLabelStyleOpts] = None,
    ):
        self.opts: dict = {
            "labelFormatter": label_formatter,
        }

        if rule_style_opts:
            self.opts.update(rule_style_opts.opts)
        if label_style_opts:
            self.opts.update(label_style_opts.opts)


class InteractionBackgroundStyleOpts(BasicOpts):
    def __init__(
        self,
        background_fill: Optional[JSFunc] = None,
        background_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        background_stroke: Optional[JSFunc] = None,
        background_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        background_line_width: Optional[Union[Numeric, JSFunc]] = None,
        background_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        background_opacity: Optional[Union[Numeric, JSFunc]] = None,
        background_shadow_color: Optional[JSFunc] = None,
        background_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        background_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        background_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "backgroundFill": background_fill,
            "backgroundFillOpacity": background_fill_opacity,
            "backgroundStroke": background_stroke,
            "backgroundStrokeOpacity": background_stroke_opacity,
            "backgroundLineWidth": background_line_width,
            "backgroundLineDash": background_line_dash,
            "backgroundOpacity": background_opacity,
            "backgroundShadowColor": background_shadow_color,
            "backgroundShadowOffsetX": background_shadow_offset_x,
            "backgroundShadowOffsetY": background_shadow_offset_y,
            "backgroundCursor": background_cursor,
        }


class InteractionElementHighlightOpts(BasicOpts):
    def __init__(
        self,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
    ):
        self.opts: dict = {
            "background": is_background,
            "offset": offset,
        }

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionLinkStyleOpts(BasicOpts):
    def __init__(
        self,
        link_fill: Optional[JSFunc] = None,
        link_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        link_stroke: Optional[JSFunc] = None,
        link_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        link_line_width: Optional[Union[Numeric, JSFunc]] = None,
        link_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        link_opacity: Optional[Union[Numeric, JSFunc]] = None,
        link_shadow_color: Optional[JSFunc] = None,
        link_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        link_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        link_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "linkFill": link_fill,
            "linkFillOpacity": link_fill_opacity,
            "linkStroke": link_stroke,
            "linkStrokeOpacity": link_stroke_opacity,
            "linkLineWidth": link_line_width,
            "linkLineDash": link_line_dash,
            "linkOpacity": link_opacity,
            "linkShadowColor": link_shadow_color,
            "linkShadowOffsetX": link_shadow_offset_x,
            "linkShadowOffsetY": link_shadow_offset_y,
            "linkCursor": link_cursor,
        }


class InteractionElementHighlightByColorOpts(BasicOpts):
    def __init__(
        self,
        is_link: Optional[bool] = None,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        link_style_opts: Optional[InteractionLinkStyleOpts] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
    ):
        self.opts: dict = {
            "link": is_link,
            "background": is_background,
            "offset": offset,
        }

        if link_style_opts:
            self.opts.update(link_style_opts.opts)

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionElementHighlightByXOpts(BasicOpts):
    def __init__(
        self,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
    ):
        self.opts: dict = {
            "background": is_background,
            "offset": offset,
        }

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionElementSelectOpts(BasicOpts):
    def __init__(
        self,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
        is_single: Optional[bool] = None,
    ):
        self.opts: dict = {
            "background": is_background,
            "offset": offset,
            "single": is_single,
        }

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionElementSelectByColorOpts(BasicOpts):
    def __init__(
        self,
        is_link: Optional[bool] = None,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        link_style_opts: Optional[InteractionLinkStyleOpts] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
    ):
        self.opts: dict = {
            "link": is_link,
            "background": is_background,
            "offset": offset,
        }

        if link_style_opts:
            self.opts.update(link_style_opts.opts)

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionElementSelectByXOpts(BasicOpts):
    def __init__(
        self,
        is_link: Optional[bool] = None,
        is_background: Optional[bool] = None,
        offset: Optional[Numeric] = None,
        link_style_opts: Optional[InteractionLinkStyleOpts] = None,
        background_style_opts: Optional[InteractionBackgroundStyleOpts] = None,
        is_single: Optional[bool] = None,
    ):
        self.opts: dict = {
            "link": is_link,
            "background": is_background,
            "offset": offset,
            "single": is_single,
        }

        if link_style_opts:
            self.opts.update(link_style_opts.opts)

        if background_style_opts:
            self.opts.update(background_style_opts.opts)


class InteractionFishEyeOpts(BasicOpts):
    def __init__(
        self,
        wait: Optional[Numeric] = None,
        is_leading: Optional[bool] = None,
        is_trailing: Optional[bool] = None,
    ):
        self.opts: dict = {
            "wait": wait,
            "leading": is_leading,
            "trailing": is_trailing,
        }


class InteractionLegendFilterOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {}


class InteractionLegendHighlightOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {}


class InteractionTipStyleOpts(BasicOpts):
    def __init__(
        self,
        tip_fill: Optional[JSFunc] = None,
        tip_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        tip_stroke: Optional[JSFunc] = None,
        tip_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        tip_line_width: Optional[Union[Numeric, JSFunc]] = None,
        tip_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        tip_opacity: Optional[Union[Numeric, JSFunc]] = None,
        tip_shadow_color: Optional[JSFunc] = None,
        tip_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        tip_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        tip_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "tipFill": tip_fill,
            "tipFillOpacity": tip_fill_opacity,
            "tipStroke": tip_stroke,
            "tipStrokeOpacity": tip_stroke_opacity,
            "tipLineWidth": tip_line_width,
            "tipLineDash": tip_line_dash,
            "tipOpacity": tip_opacity,
            "tipShadowColor": tip_shadow_color,
            "tipShadowOffsetX": tip_shadow_offset_x,
            "tipShadowOffsetY": tip_shadow_offset_y,
            "tipCursor": tip_cursor,
        }


class InteractionPopTipOpts(BasicOpts):
    def __init__(
        self,
        offset_x: Optional[Numeric] = None,
        offset_y: Optional[Numeric] = None,
        tip_style_opts: Optional[InteractionTipStyleOpts] = None,
    ):
        self.opts: dict = {
            "offsetX": offset_x,
            "offsetY": offset_y,
        }

        if tip_style_opts:
            self.opts.update(tip_style_opts.opts)


class InteractionTooltipBBoxOpts(BasicOpts):
    def __init__(
        self,
        x_: Optional[Numeric] = None,
        y_: Optional[Numeric] = None,
        width: Optional[Numeric] = None,
        height: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "x": x_,
            "y": y_,
            "width": width,
            "height": height,
        }


class InteractionCrossHairsStyleOpts(BasicOpts):
    def __init__(
        self,
        crosshairs_fill: Optional[JSFunc] = None,
        crosshairs_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_stroke: Optional[JSFunc] = None,
        crosshairs_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_line_width: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        crosshairs_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_shadow_color: Optional[JSFunc] = None,
        crosshairs_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        crosshairs_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "crosshairsFill": crosshairs_fill,
            "crosshairsFillOpacity": crosshairs_fill_opacity,
            "crosshairsStroke": crosshairs_stroke,
            "crosshairsStrokeOpacity": crosshairs_stroke_opacity,
            "crosshairsLineWidth": crosshairs_line_width,
            "crosshairsLineDash": crosshairs_line_dash,
            "crosshairsOpacity": crosshairs_opacity,
            "crosshairsShadowColor": crosshairs_shadow_color,
            "crosshairsShadowOffsetX": crosshairs_shadow_offset_x,
            "crosshairsShadowOffsetY": crosshairs_shadow_offset_y,
            "crosshairsCursor": crosshairs_cursor,
        }


class InteractionCrossHairsXStyleOpts(BasicOpts):
    def __init__(
        self,
        crosshairsx_fill: Optional[JSFunc] = None,
        crosshairsx_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_stroke: Optional[JSFunc] = None,
        crosshairsx_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_line_width: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        crosshairsx_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_shadow_color: Optional[JSFunc] = None,
        crosshairsx_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsx_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "crosshairsXFill": crosshairsx_fill,
            "crosshairsXFillOpacity": crosshairsx_fill_opacity,
            "crosshairsXStroke": crosshairsx_stroke,
            "crosshairsXStrokeOpacity": crosshairsx_stroke_opacity,
            "crosshairsXLineWidth": crosshairsx_line_width,
            "crosshairsXLineDash": crosshairsx_line_dash,
            "crosshairsXOpacity": crosshairsx_opacity,
            "crosshairsXShadowColor": crosshairsx_shadow_color,
            "crosshairsXShadowOffsetX": crosshairsx_shadow_offset_x,
            "crosshairsXShadowOffsetY": crosshairsx_shadow_offset_y,
            "crosshairsXCursor": crosshairsx_cursor,
        }


class InteractionCrossHairsYStyleOpts(BasicOpts):
    def __init__(
        self,
        crosshairsy_fill: Optional[JSFunc] = None,
        crosshairsy_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_stroke: Optional[JSFunc] = None,
        crosshairsy_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_line_width: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        crosshairsy_opacity: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_shadow_color: Optional[JSFunc] = None,
        crosshairsy_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        crosshairsy_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "crosshairsYFill": crosshairsy_fill,
            "crosshairsYFillOpacity": crosshairsy_fill_opacity,
            "crosshairsYStroke": crosshairsy_stroke,
            "crosshairsYStrokeOpacity": crosshairsy_stroke_opacity,
            "crosshairsYLineWidth": crosshairsy_line_width,
            "crosshairsYLineDash": crosshairsy_line_dash,
            "crosshairsYOpacity": crosshairsy_opacity,
            "crosshairsYShadowColor": crosshairsy_shadow_color,
            "crosshairsYShadowOffsetX": crosshairsy_shadow_offset_x,
            "crosshairsYShadowOffsetY": crosshairsy_shadow_offset_y,
            "crosshairsYCursor": crosshairsy_cursor,
        }


class InteractionMarkerStyleOpts(BasicOpts):
    def __init__(
        self,
        marker_fill: Optional[JSFunc] = None,
        marker_fill_opacity: Optional[Union[Numeric, JSFunc]] = None,
        marker_stroke: Optional[JSFunc] = None,
        marker_stroke_opacity: Optional[Union[Numeric, JSFunc]] = None,
        marker_line_width: Optional[Union[Numeric, JSFunc]] = None,
        marker_line_dash: Optional[Union[Sequence, JSFunc]] = None,
        marker_opacity: Optional[Union[Numeric, JSFunc]] = None,
        marker_shadow_color: Optional[JSFunc] = None,
        marker_shadow_offset_x: Optional[Union[Numeric, JSFunc]] = None,
        marker_shadow_offset_y: Optional[Union[Numeric, JSFunc]] = None,
        marker_cursor: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "markerFill": marker_fill,
            "markerFillOpacity": marker_fill_opacity,
            "markerStroke": marker_stroke,
            "markerStrokeOpacity": marker_stroke_opacity,
            "markerLineWidth": marker_line_width,
            "markerLineDash": marker_line_dash,
            "markerOpacity": marker_opacity,
            "markerShadowColor": marker_shadow_color,
            "markerShadowOffsetX": marker_shadow_offset_x,
            "markerShadowOffsetY": marker_shadow_offset_y,
            "markerCursor": marker_cursor,
        }


class InteractionTooltipOpts(BasicOpts):
    def __init__(
        self,
        wait: Optional[Numeric] = None,
        is_leading: Optional[bool] = None,
        is_trailing: Optional[bool] = None,
        is_shared: Optional[bool] = None,
        is_series: Optional[bool] = None,
        is_body: Optional[bool] = None,
        is_marker: Optional[bool] = None,
        is_group_name: Optional[bool] = None,
        position: Optional[str] = None,
        mount: Optional[JSFunc] = None,
        bounding: Optional[InteractionTooltipBBoxOpts] = None,
        offset: Optional[Sequence[Numeric]] = None,
        is_crosshairs: Optional[bool] = None,
        is_crosshairs_x: Optional[bool] = None,
        is_crosshairs_y: Optional[bool] = None,
        crosshairs_style_opts: Optional[InteractionCrossHairsStyleOpts] = None,
        marker_type: Optional[JSFunc] = None,
        render: Optional[JSFunc] = None,
        sort_: Optional[JSFunc] = None,
        filter_: Optional[JSFunc] = None,
        is_disable_native: Optional[bool] = None,
        css: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "wait": wait,
            "leading": is_leading,
            "trailing": is_trailing,
            "shared": is_shared,
            "series": is_series,
            "body": is_body,
            "marker": is_marker,
            "groupName": is_group_name,
            "position": position,
            "mount": mount,
            "bounding": bounding,
            "offset": offset,
            "crosshairs": is_crosshairs,
            "crosshairsX": is_crosshairs_x,
            "crosshairsY": is_crosshairs_y,
            "markerType": marker_type,
            "render": render,
            "sort": sort_,
            "filter": filter_,
            "disableNative": is_disable_native,
            "css": css,
        }

        if crosshairs_style_opts:
            self.opts.update(crosshairs_style_opts.opts)


InteractionCfg = Union[
    InteractionBrushAxisHighlightOpts,
    InteractionBrushFilterOpts,
    InteractionBrushHighlightOpts,
    InteractionBrushXFilterOpts,
    InteractionBrushXHighlightOpts,
    InteractionBrushYFilterOpts,
    InteractionBrushYHighlightOpts,
    InteractionChartIndexOpts,
    InteractionElementHighlightOpts,
    InteractionElementHighlightByColorOpts,
    InteractionElementHighlightByXOpts,
    InteractionElementSelectOpts,
    InteractionElementSelectByColorOpts,
    InteractionElementSelectByXOpts,
    InteractionFishEyeOpts,
    InteractionLegendFilterOpts,
    InteractionLegendHighlightOpts,
    InteractionPopTipOpts,
    InteractionTooltipOpts,
    dict,
]


class InteractionOpts(BasicOpts):
    def __init__(
        self,
        brush_axis_highlight_opts: Optional[InteractionBrushAxisHighlightOpts] = None,
        brush_filter_opts: Optional[InteractionBrushFilterOpts] = None,
        brush_highlight_opts: Optional[InteractionBrushHighlightOpts] = None,
        brush_x_filter_opts: Optional[InteractionBrushXFilterOpts] = None,
        brush_x_highlight_opts: Optional[InteractionBrushXHighlightOpts] = None,
        brush_y_filter_opts: Optional[InteractionBrushYFilterOpts] = None,
        brush_y_highlight_opts: Optional[InteractionBrushYHighlightOpts] = None,
        chart_index_opts: Optional[InteractionChartIndexOpts] = None,
        element_highlight_opts: Optional[InteractionElementHighlightOpts] = None,
        element_highlight_by_color_opts: Optional[
            InteractionElementHighlightByColorOpts
        ] = None,
        element_highlight_by_x_opts: Optional[
            InteractionElementHighlightByXOpts
        ] = None,
        element_select_opts: Optional[InteractionElementSelectOpts] = None,
        element_select_by_color_opts: Optional[
            InteractionElementSelectByColorOpts
        ] = None,
        element_select_by_x_opts: Optional[InteractionElementSelectByXOpts] = None,
        fisheye_opts: Optional[InteractionFishEyeOpts] = None,
        legend_filter_opts: Optional[InteractionLegendFilterOpts] = None,
        legend_highlight_opts: Optional[InteractionLegendHighlightOpts] = None,
        poptip_opts: Optional[InteractionPopTipOpts] = None,
        tooltip_opts: Optional[InteractionTooltipOpts] = None,
    ):
        self.opts: dict = {
            "brushAxisHighlight": brush_axis_highlight_opts,
            "brushFilter": brush_filter_opts,
            "brushHighlight": brush_highlight_opts,
            "brushXFilter": brush_x_filter_opts,
            "brushXHighlight": brush_x_highlight_opts,
            "brushYFilter": brush_y_filter_opts,
            "brushYHighlight": brush_y_highlight_opts,
            "chartIndex": chart_index_opts,
            "elementHighlight": element_highlight_opts,
            "elementHighlightByColor": element_highlight_by_color_opts,
            "elementHighlightByX": element_highlight_by_x_opts,
            "elementSelect": element_select_opts,
            "elementSelectByColor": element_select_by_color_opts,
            "elementSelectByX": element_select_by_x_opts,
            "fisheye": fisheye_opts,
            "legendFilter": legend_filter_opts,
            "legendHighlight": legend_highlight_opts,
            "poptip": poptip_opts,
            "tooltip": tooltip_opts,
        }

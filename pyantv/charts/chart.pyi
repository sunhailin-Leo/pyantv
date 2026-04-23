from typing import Any, Optional, Self, Sequence, Union

from ..commons.utils import JsCode
from ..options import InitOpts, RenderOpts
from ..options.global_options import (
    AnimateOpts,
    AxisOpts,
    BaseChartStyleOpts,
    InteractionOpts,
    LabelOpts,
    LegendCategoryOpts,
    LegendContinuousOpts,
    ScrollBarOpts,
    SliderOpts,
    StateOpts,
    TitleOpts,
    TooltipOpts,
)
from ..options.series_options import Numeric
from ..types import (
    Animate,
    Axis,
    BaseChartStyle,
    Coordinate,
    Data,
    Init,
    Interaction,
    JSFunc,
    Label,
    Legend,
    RenderInit,
    Scale,
    ScrollBar,
    Slider,
    State,
    Title,
    Tooltip,
    Transform,
)
from .base import Base

class Chart(Base):
    def __init__(
        self,
        init_opts: Init = ...,
        render_opts: RenderInit = ...,
    ) -> None: ...
    def set_data(
        self,
        data: Union[Sequence, Data],
    ) -> Self: ...
    def set_encode(
        self,
        x_field_name: Optional[Union[JSFunc, Sequence[str]]] = ...,
        y_field_name: Optional[Union[JSFunc, Sequence[str]]] = ...,
        z_field_name: Optional[Union[JSFunc, Sequence[str]]] = ...,
        color_field: Optional[Union[JSFunc, Sequence[str]]] = ...,
        shape_field: Optional[JSFunc] = ...,
        size_field: Optional[JSFunc] = ...,
        series_field: Optional[JSFunc] = ...,
        key_field: Optional[JSFunc] = ...,
        group_key_field: Optional[JSFunc] = ...,
        value_field: Optional[JSFunc] = ...,
        rotate_field: Optional[JSFunc] = ...,
        opacity_field: Optional[JSFunc] = ...,
        fill_field: Optional[JSFunc] = ...,
        stroke_field: Optional[JSFunc] = ...,
        stroke_width_field: Optional[JSFunc] = ...,
        font_size_field: Optional[JSFunc] = ...,
        font_weight_field: Optional[JSFunc] = ...,
        dx_field: Optional[JSFunc] = ...,
        dy_field: Optional[JSFunc] = ...,
        title_field: Optional[JSFunc] = ...,
        href_field: Optional[JSFunc] = ...,
        src_field: Optional[JSFunc] = ...,
        ext_field: Optional[dict] = ...,
    ) -> Self: ...
    def set_scale(
        self,
        x_scale_opts: Optional[Scale] = ...,
        y_scale_opts: Optional[Scale] = ...,
        color_scale_opts: Optional[Scale] = ...,
        size_scale_opts: Optional[Scale] = ...,
        shape_scale_opts: Optional[Scale] = ...,
        opacity_scale_opts: Optional[Scale] = ...,
        ext_scale: Optional[dict] = ...,
    ) -> Self: ...
    def set_theme(
        self,
        theme: Optional[Union[str, dict]] = ...,
    ) -> Self: ...
    def set_transform(
        self,
        transform_opts: Optional[
            Union[Transform, Sequence[Transform]]
        ] = ...,
    ) -> Self: ...
    def set_coordinate(
        self,
        coordinate_opts: Optional[Coordinate] = ...,
    ) -> Self: ...
    def set_interaction(
        self,
        interaction_opts: Optional[Interaction] = ...,
    ) -> Self: ...
    def set_animate(
        self,
        animate_opts: Optional[Animate] = ...,
    ) -> Self: ...
    def set_style(
        self,
        style_opts: Optional[BaseChartStyle] = ...,
    ) -> Self: ...
    def set_labels(
        self,
        label_opts: Optional[Label] = ...,
    ) -> Self: ...
    def set_tooltip(
        self,
        tooltip_opts: Optional[Tooltip] = ...,
    ) -> Self: ...
    def set_axis(
        self,
        axis_opts: Optional[Axis] = ...,
    ) -> Self: ...
    def set_legend(
        self,
        legend_opts: Optional[Legend] = ...,
    ) -> Self: ...
    def set_annotations(
        self,
        annotation_list: Optional[Sequence[Any]] = ...,
    ) -> Self: ...
    def set_global_options(
        self,
        x_: Optional[Numeric] = ...,
        y_: Optional[Numeric] = ...,
        width: Optional[Numeric] = ...,
        height: Optional[Numeric] = ...,
        is_auto_fit: Optional[bool] = ...,
        background: Optional[Union[str, dict]] = ...,
        transform_opts: Optional[
            Union[Transform, Sequence[Transform]]
        ] = ...,
        coordinate_opts: Optional[Coordinate] = ...,
        style_opts: Optional[BaseChartStyle] = ...,
        animate_opts: Optional[Animate] = ...,
        state_opts: Optional[State] = ...,
        interaction_opts: Optional[Interaction] = ...,
        title_opts: Optional[Title] = ...,
        axis_opts: Optional[Axis] = ...,
        legend_opts: Optional[Legend] = ...,
        scrollbar_opts: Optional[ScrollBar] = ...,
        slider_opts: Optional[Slider] = ...,
        tooltip_opts: Optional[Tooltip] = ...,
        label_opts: Optional[Label] = ...,
        inset: Optional[Numeric] = ...,
        inset_left: Optional[Numeric] = ...,
        inset_right: Optional[Numeric] = ...,
        padding: Optional[Numeric] = ...,
        padding_left: Optional[Numeric] = ...,
        padding_right: Optional[Numeric] = ...,
        padding_top: Optional[Numeric] = ...,
        padding_bottom: Optional[Numeric] = ...,
        ratio: Optional[Sequence[Numeric]] = ...,
        direction: Optional[str] = ...,
        iteration_count: Optional[Numeric] = ...,
    ) -> Self: ...

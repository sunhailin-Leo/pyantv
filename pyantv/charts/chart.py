from .. import options as opts
from .. import types
from ..charts.base import Base


class Chart(Base):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self._chart_type: types.Optional[str] = None

    def set_data(
        self,
        data: types.Union[types.Sequence, types.Data],
    ):
        self.options.update(data=data)
        return self

    def set_encode(
        self,
        x_field_name: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        y_field_name: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        z_field_name: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        color_field: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        shape_field: types.Optional[types.JSFunc] = None,
        size_field: types.Optional[types.JSFunc] = None,
        series_field: types.Optional[types.JSFunc] = None,
        key_field: types.Optional[types.JSFunc] = None,
        group_key_field: types.Optional[types.JSFunc] = None,
        value_field: types.Optional[types.JSFunc] = None,
        rotate_field: types.Optional[types.JSFunc] = None,
        ext_field: types.Optional[dict] = None,
    ):
        self.options.update(
            encode={
                "x": x_field_name,
                "y": y_field_name,
                "z": z_field_name,
                "color": color_field,
                "shape": shape_field,
                "size": size_field,
                "series": series_field,
                "key": key_field,
                "groupKey": group_key_field,
                "value": value_field,
                "rotate": rotate_field,
            }
        )
        if ext_field:
            self.options.get("encode").update(ext_field)

        return self

    def set_scale(
        self,
        x_scale_opts: types.Optional[types.Scale] = None,
        y_scale_opts: types.Optional[types.Scale] = None,
        color_scale_opts: types.Optional[types.Scale] = None,
        size_scale_opts: types.Optional[types.Scale] = None,
    ):
        self.options.update(
            scale={
                "x": x_scale_opts,
                "y": y_scale_opts,
                "color": color_scale_opts,
                "size": size_scale_opts,
            }
        )

        return self

    def set_global_options(
        self,
        x_: types.Optional[types.Numeric] = None,
        y_: types.Optional[types.Numeric] = None,
        width: types.Optional[types.Numeric] = None,
        height: types.Optional[types.Numeric] = None,
        is_auto_fit: types.Optional[bool] = None,
        background: types.Optional[types.Union[str, dict]] = None,
        transform_opts: types.Optional[
            types.Union[types.Transform, types.Sequence[types.Transform]]
        ] = None,
        coordinate_opts: types.Optional[types.Coordinate] = None,
        style_opts: types.Optional[types.BaseChartStyle] = None,
        animate_opts: types.Optional[types.Animate] = None,
        state_opts: types.Optional[types.State] = None,
        interaction_opts: types.Optional[types.Interaction] = None,
        title_opts: types.Optional[types.Title] = None,
        axis_opts: types.Optional[types.Axis] = None,
        legend_opts: types.Optional[types.Legend] = None,
        scrollbar_opts: types.Optional[types.ScrollBar] = None,
        slider_opts: types.Optional[types.Slider] = None,
        tooltip_opts: types.Optional[types.Tooltip] = None,
        label_opts: types.Optional[types.Label] = None,
        inset: types.Optional[types.Numeric] = None,
        inset_left: types.Optional[types.Numeric] = None,
        inset_right: types.Optional[types.Numeric] = None,
        padding: types.Optional[types.Numeric] = None,
        padding_left: types.Optional[types.Numeric] = None,
        padding_right: types.Optional[types.Numeric] = None,
        padding_top: types.Optional[types.Numeric] = None,
        padding_bottom: types.Optional[types.Numeric] = None,
        ratio: types.Optional[types.Sequence[types.Numeric]] = None,
        direction: types.Optional[str] = None,
        iteration_count: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            {
                "x": x_,
                "y": y_,
                "width": width,
                "height": height,
                "autoFit": is_auto_fit,
                "background": background,
                "transform": transform_opts,
                "coordinate": coordinate_opts,
                "style": style_opts,
                "animate": animate_opts,
                "state": state_opts,
                "interaction": interaction_opts,
                "title": title_opts,
                "axis": axis_opts,
                "legend": legend_opts,
                "scrollbar": scrollbar_opts,
                "slider": slider_opts,
                "tooltip": tooltip_opts,
                "labels": label_opts,
                "inset": inset,
                "insetLeft": inset_left,
                "insetRight": inset_right,
                "padding": padding,
                "paddingLeft": padding_left,
                "paddingRight": padding_right,
                "paddingTop": padding_top,
                "paddingBottom": padding_bottom,
                "ratio": ratio,
                "direction": direction,
                "iterationCount": iteration_count,
            }
        )

        return self

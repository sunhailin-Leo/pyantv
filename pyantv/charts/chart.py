from __future__ import annotations

import sys
from typing import Any, Optional

if sys.version_info >= (3, 11):
    from typing import Self
else:
    try:
        from typing_extensions import Self
    except ImportError:
        Self = Any  # type: ignore[assignment,misc]

from .. import options as opts
from .. import types
from ..charts.base import Base


class Chart(Base):
    """G2 图表基类，提供数据、编码、样式等配置的链式 API。

    所有具体图表类（如 Line、Interval、Area 等）均继承自本类。
    """

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
        sample_if_large: Optional[int] = None,
        sample_method: str = 'lttb',
        sample_x_field: Optional[str] = None,
        sample_y_field: Optional[str] = None,
    ) -> Self:
        """设置图表数据，支持大数据量自动降采样。

        支持直接传入 pandas DataFrame、Series 或 numpy ndarray，
        会自动转换为 G2 所需的字典列表格式。

        :param data: 数据列表、Data 配置对象、DataFrame、Series 或 ndarray。
        :param sample_if_large: 当数据点数超过此值时自动降采样，None 表示不采样。
        :param sample_method: 降采样方法，默认 'lttb'。支持 'lttb'、'uniform'、'random'。
        :param sample_x_field: LTTB 方法需要的 x 轴字段名。
        :param sample_y_field: LTTB 方法需要的 y 轴字段名。
        :returns: 图表对象自身，支持链式调用。
        :raises TypeError: 当 data 类型不被支持时。
        """
        from ..commons.utils import convert_data_if_needed
        from ..options.series_options import BasicOpts

        if data is not None and not isinstance(
            data, (list, dict, BasicOpts, int, float, str)
        ):
            converted = convert_data_if_needed(data)
            if converted is data:
                raise TypeError(
                    "set_data() expected list, dict, or Data opts, "
                    "got {!r} (type: {}). "
                    "Hint: pass a list of dicts like "
                    "[{{'x': 1, 'y': 2}}].".format(
                        data, type(data).__name__
                    )
                )
            converted_data = converted
        else:
            converted_data = convert_data_if_needed(data)

        if sample_if_large is not None and isinstance(converted_data, list):
            if len(converted_data) > sample_if_large:
                from ..data.pipeline import downsample
                import warnings

                warnings.warn(
                    f"Data size ({len(converted_data)}) exceeds sample_if_large "
                    f"({sample_if_large}). Downsampling to {sample_if_large} points "
                    f"using '{sample_method}' method.",
                    UserWarning,
                    stacklevel=2,
                )

                converted_data = downsample(
                    data=converted_data,
                    max_points=sample_if_large,
                    method=sample_method,
                    x_field=sample_x_field,
                    y_field=sample_y_field,
                )

        self.options.update(data=converted_data)
        return self

    @classmethod
    def from_data(
        cls,
        data: types.Union[types.Sequence, types.Data],
        x_field_name: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        y_field_name: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        color_field: types.Optional[
            types.Union[types.JSFunc, types.Sequence[str]]
        ] = None,
        size_field: types.Optional[types.JSFunc] = None,
        shape_field: types.Optional[types.JSFunc] = None,
        series_field: types.Optional[types.JSFunc] = None,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        """一行创建图表：设置数据和常用编码通道。

        快捷工厂方法，等价于 ``cls().set_data(data).set_encode(...)``。
        返回的实例仍可继续链式调用其他 ``set_*`` 方法进行精细配置。

        :param data: 图表数据，支持列表、字典或 Data 配置对象。
        :param x_field_name: x 轴编码字段。
        :param y_field_name: y 轴编码字段。
        :param color_field: 颜色编码字段。
        :param size_field: 大小编码字段。
        :param shape_field: 形状编码字段。
        :param series_field: 系列编码字段。
        :param init_opts: 初始化配置。
        :param render_opts: 渲染配置。
        :returns: 配置好数据和编码的图表实例。

        Examples:
            >>> from pyantv import Line
            >>> chart = Line.from_data(
            ...     data=[{"year": "2020", "value": 3}],
            ...     x_field_name="year",
            ...     y_field_name="value",
            ... )
        """
        chart = cls(init_opts=init_opts, render_opts=render_opts)
        chart.set_data(data=data)
        chart.set_encode(
            x_field_name=x_field_name,
            y_field_name=y_field_name,
            color_field=color_field,
            size_field=size_field,
            shape_field=shape_field,
            series_field=series_field,
        )
        return chart

    @classmethod
    def from_dataframe(
        cls,
        dataframe,
        x_field_name: types.Optional[str] = None,
        y_field_name: types.Optional[str] = None,
        color_field: types.Optional[str] = None,
        size_field: types.Optional[str] = None,
        shape_field: types.Optional[str] = None,
        series_field: types.Optional[str] = None,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        """从 pandas DataFrame 创建图表，自动推断编码字段。

        将 DataFrame 转换为 ``list[dict]`` 并设置数据和编码。
        如果未指定 ``x_field_name`` 和 ``y_field_name``，将自动推断：

        - **x 轴**：第一个字符串/分类/日期列
        - **y 轴**：第一个数值列

        :param dataframe: pandas DataFrame 对象。
        :param x_field_name: x 轴编码字段名，为 None 时自动推断。
        :param y_field_name: y 轴编码字段名，为 None 时自动推断。
        :param color_field: 颜色编码字段名。
        :param size_field: 大小编码字段名。
        :param shape_field: 形状编码字段名。
        :param series_field: 系列编码字段名。
        :param init_opts: 初始化配置。
        :param render_opts: 渲染配置。
        :returns: 配置好数据和编码的图表实例。
        :raises TypeError: 当 dataframe 不是 pandas DataFrame 时。

        Examples:
            >>> import pandas as pd
            >>> from pyantv import Line
            >>> df = pd.DataFrame({"year": [2020, 2021], "value": [3, 4]})
            >>> chart = Line.from_dataframe(df, x_field_name="year",
            ...                            y_field_name="value")
        """
        try:
            import pandas as pd
        except ImportError:
            raise ImportError(
                "from_dataframe() requires pandas. "
                "Install it with: pip install pandas"
            )

        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError(
                "from_dataframe() expected pandas DataFrame, "
                "got {!r} (type: {}).".format(
                    dataframe, type(dataframe).__name__
                )
            )

        if x_field_name is None or y_field_name is None:
            categorical_columns = []
            numeric_columns = []
            for col in dataframe.columns:
                if pd.api.types.is_numeric_dtype(dataframe[col]):
                    numeric_columns.append(col)
                else:
                    categorical_columns.append(col)

            if x_field_name is None and categorical_columns:
                x_field_name = categorical_columns[0]
            elif x_field_name is None and len(numeric_columns) >= 2:
                x_field_name = numeric_columns[0]

            if y_field_name is None and numeric_columns:
                inferred_y = (
                    numeric_columns[0]
                    if x_field_name not in numeric_columns
                    else (
                        numeric_columns[1]
                        if len(numeric_columns) >= 2
                        else numeric_columns[0]
                    )
                )
                y_field_name = inferred_y

        records = [
            {
                k: (None if pd.isna(v) else v)
                for k, v in row.items()
            }
            for row in dataframe.to_dict("records")
        ]

        return cls.from_data(
            data=records,
            x_field_name=x_field_name,
            y_field_name=y_field_name,
            color_field=color_field,
            size_field=size_field,
            shape_field=shape_field,
            series_field=series_field,
            init_opts=init_opts,
            render_opts=render_opts,
        )

    def _validate_field_against_data(self, field_value, field_label: str):
        """校验编码字段名是否在数据字段中存在，不存在时给出智能建议。

        仅当数据为 ``list[dict]`` 且字段值为字符串时才会校验。
        字段不存在时发出 ``UserWarning``，并附上最接近的候选字段。

        :param field_value: 编码字段的值。
        :param field_label: 编码通道名称（如 ``"x_field_name"``），用于提示信息。
        """
        if not isinstance(field_value, str):
            return
        data = self.options.get("data")
        if not isinstance(data, list) or not data:
            return
        first_item = data[0]
        if not isinstance(first_item, dict):
            return

        available_keys = list(first_item.keys())
        if field_value not in available_keys:
            import difflib
            import warnings

            suggestions = difflib.get_close_matches(
                field_value, available_keys, n=3, cutoff=0.4
            )
            message = (
                "set_encode(): field '{}' for {} not found in data keys {}."
            ).format(field_value, field_label, available_keys)
            if suggestions:
                message += " Did you mean: {}?".format(
                    ", ".join("'{}'".format(s) for s in suggestions)
                )
            warnings.warn(message, UserWarning, stacklevel=3)

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
        opacity_field: types.Optional[types.JSFunc] = None,
        fill_field: types.Optional[types.JSFunc] = None,
        stroke_field: types.Optional[types.JSFunc] = None,
        stroke_width_field: types.Optional[types.JSFunc] = None,
        font_size_field: types.Optional[types.JSFunc] = None,
        font_weight_field: types.Optional[types.JSFunc] = None,
        dx_field: types.Optional[types.JSFunc] = None,
        dy_field: types.Optional[types.JSFunc] = None,
        title_field: types.Optional[types.JSFunc] = None,
        href_field: types.Optional[types.JSFunc] = None,
        src_field: types.Optional[types.JSFunc] = None,
        ext_field: types.Optional[dict] = None,
    ) -> Self:
        """设置视觉编码通道，将数据字段映射到图形属性。

        当数据已通过 :meth:`set_data` 设置且字段名为字符串时，
        会自动校验字段名是否存在于数据中，不存在时发出警告并给出建议。

        :param x_field_name: x 轴编码字段。
        :param y_field_name: y 轴编码字段。
        :param z_field_name: z 轴编码字段（3D 图表）。
        :param color_field: 颜色编码字段。
        :param shape_field: 形状编码字段。
        :param size_field: 大小编码字段。
        :param series_field: 系列编码字段。
        :param key_field: 唯一标识编码字段。
        :param group_key_field: 分组标识编码字段。
        :param value_field: 值编码字段。
        :param ext_field: 扩展编码字段字典，用于自定义通道。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..commons.utils import JsCode

        if x_field_name is not None and not isinstance(
            x_field_name, (str, list, JsCode)
        ):
            raise TypeError(
                "set_encode() expected x_field_name to be "
                "str, list, or JsCode, got {!r} (type: "
                "{}).".format(
                    x_field_name,
                    type(x_field_name).__name__,
                )
            )
        if y_field_name is not None and not isinstance(
            y_field_name, (str, list, JsCode)
        ):
            raise TypeError(
                "set_encode() expected y_field_name to be "
                "str, list, or JsCode, got {!r} (type: "
                "{}).".format(
                    y_field_name,
                    type(y_field_name).__name__,
                )
            )

        field_checks = {
            "x_field_name": x_field_name,
            "y_field_name": y_field_name,
            "z_field_name": z_field_name,
            "color_field": color_field,
            "size_field": size_field,
            "shape_field": shape_field,
            "series_field": series_field,
        }
        for label, value in field_checks.items():
            if value is not None:
                self._validate_field_against_data(value, label)
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
                "opacity": opacity_field,
                "fill": fill_field,
                "stroke": stroke_field,
                "strokeWidth": stroke_width_field,
                "fontSize": font_size_field,
                "fontWeight": font_weight_field,
                "dx": dx_field,
                "dy": dy_field,
                "title": title_field,
                "href": href_field,
                "src": src_field,
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
        shape_scale_opts: types.Optional[types.Scale] = None,
        opacity_scale_opts: types.Optional[types.Scale] = None,
        ext_scale: types.Optional[dict] = None,
    ) -> Self:
        """设置比例尺配置，控制数据到视觉属性的映射规则。

        :param x_scale_opts: x 轴比例尺配置。
        :param y_scale_opts: y 轴比例尺配置。
        :param color_scale_opts: 颜色比例尺配置。
        :param size_scale_opts: 大小比例尺配置。
        :param shape_scale_opts: 形状比例尺配置。
        :param opacity_scale_opts: 透明度比例尺配置。
        :param ext_scale: 扩展比例尺字典，用于自定义通道。
        :returns: 图表对象自身，支持链式调用。
        """
        scale_dict = {
            "x": x_scale_opts,
            "y": y_scale_opts,
            "color": color_scale_opts,
            "size": size_scale_opts,
            "shape": shape_scale_opts,
            "opacity": opacity_scale_opts,
        }
        if ext_scale:
            scale_dict.update(ext_scale)
        self.options.update(scale=scale_dict)

        return self

    def set_theme(
        self,
        theme: types.Optional[types.Union[str, dict]] = None,
    ) -> Self:
        """设置图表主题。

        :param theme: 主题名称（如 ``"dark"``、``"academy"``）或自定义主题字典。
        :returns: 图表对象自身，支持链式调用。
        """
        if theme is not None and not isinstance(theme, (str, dict)):
            raise TypeError(
                "set_theme() expected str or dict, "
                "got {!r} (type: {}).".format(theme, type(theme).__name__)
            )
        self.render_options.update(theme=theme)
        return self

    def set_transform(
        self,
        transform_opts: types.Optional[
            types.Union[types.Transform, types.Sequence[types.Transform]]
        ] = None,
    ) -> Self:
        """设置数据转换配置。

        :param transform_opts: 单个或多个 Transform 配置。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if transform_opts is not None and not isinstance(
            transform_opts, (BasicOpts, dict, list)
        ):
            raise TypeError(
                "set_transform() expected opts, dict, "
                "or list, got {!r} (type: {}).".format(
                    transform_opts,
                    type(transform_opts).__name__,
                )
            )
        self.options.update(transform=transform_opts)
        return self

    def set_coordinate(
        self,
        coordinate_opts: types.Optional[types.Coordinate] = None,
    ) -> Self:
        """设置坐标系配置（如极坐标、平行坐标等）。

        :param coordinate_opts: 坐标系配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if coordinate_opts is not None and not isinstance(
            coordinate_opts, (BasicOpts, dict)
        ):
            raise TypeError(
                "set_coordinate() expected opts or dict, "
                "got {!r} (type: {}).".format(
                    coordinate_opts,
                    type(coordinate_opts).__name__,
                )
            )
        self.options.update(coordinate=coordinate_opts)
        return self

    def set_interaction(
        self,
        interaction_opts: types.Optional[types.Interaction] = None,
    ) -> Self:
        """设置交互配置（如 tooltip 跟随、框选等）。

        :param interaction_opts: 交互配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        self.options.update(interaction=interaction_opts)
        return self

    def set_animate(
        self,
        animate_opts: types.Optional[types.Animate] = None,
    ) -> Self:
        """设置动画配置。

        :param animate_opts: 动画配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        self.options.update(animate=animate_opts)
        return self

    def set_style(
        self,
        style_opts: types.Optional[types.BaseChartStyle] = None,
    ) -> Self:
        """设置图形样式配置（如填充色、描边等）。

        :param style_opts: 样式配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if style_opts is not None and not isinstance(
            style_opts, (BasicOpts, dict, bool)
        ):
            raise TypeError(
                "set_style() expected opts, dict, or "
                "bool, got {!r} (type: {}).".format(
                    style_opts,
                    type(style_opts).__name__,
                )
            )
        self.options.update(style=style_opts)
        return self

    def set_labels(
        self,
        label_opts: types.Optional[types.Label] = None,
    ) -> Self:
        """设置数据标签配置。

        :param label_opts: 标签配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if label_opts is not None and not isinstance(
            label_opts, (BasicOpts, dict, bool)
        ):
            raise TypeError(
                "set_labels() expected opts, dict, or "
                "bool, got {!r} (type: {}).".format(
                    label_opts,
                    type(label_opts).__name__,
                )
            )
        self.options.update(labels=label_opts)
        return self

    def set_tooltip(
        self,
        tooltip_opts: types.Optional[types.Tooltip] = None,
    ) -> Self:
        """设置提示框配置。

        :param tooltip_opts: 提示框配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if tooltip_opts is not None and not isinstance(
            tooltip_opts, (BasicOpts, dict, bool)
        ):
            raise TypeError(
                "set_tooltip() expected opts, dict, or "
                "bool, got {!r} (type: {}).".format(
                    tooltip_opts,
                    type(tooltip_opts).__name__,
                )
            )
        self.options.update(tooltip=tooltip_opts)
        return self

    def set_axis(
        self,
        axis_opts: types.Optional[types.Axis] = None,
    ) -> Self:
        """设置坐标轴配置。

        :param axis_opts: 坐标轴配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if axis_opts is not None and not isinstance(
            axis_opts, (BasicOpts, dict, bool)
        ):
            raise TypeError(
                "set_axis() expected opts, dict, or "
                "bool, got {!r} (type: {}).".format(
                    axis_opts,
                    type(axis_opts).__name__,
                )
            )
        self.options.update(axis=axis_opts)
        return self

    def set_legend(
        self,
        legend_opts: types.Optional[types.Legend] = None,
    ) -> Self:
        """设置图例配置。

        :param legend_opts: 图例配置对象。
        :returns: 图表对象自身，支持链式调用。
        """
        from ..options.series_options import BasicOpts

        if legend_opts is not None and not isinstance(
            legend_opts, (BasicOpts, dict, bool)
        ):
            raise TypeError(
                "set_legend() expected opts, dict, or "
                "bool, got {!r} (type: {}).".format(
                    legend_opts,
                    type(legend_opts).__name__,
                )
            )
        self.options.update(legend=legend_opts)
        return self

    def set_annotations(
        self,
        annotation_list: types.Optional[types.Sequence] = None,
    ) -> Self:
        """设置图表标注（参考线、区域标注、文本标注等）。

        标注会作为额外的子视图叠加在图表上。

        :param annotation_list: 标注配置列表。
        :returns: 图表对象自身，支持链式调用。
        """
        if annotation_list is not None:
            children = self.options.get("children", [])
            for annotation in annotation_list:
                if hasattr(annotation, "opts"):
                    children.append(annotation.opts)
                else:
                    children.append(annotation)
            self.options.update(children=children)
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
    ) -> Self:
        """一次性设置多个全局配置项。

        包含布局、组件、交互等所有顶层配置，适合在最后统一配置。
        各参数均为可选，仅传入需要设置的项即可。

        :param width: 图表宽度（像素）。
        :param height: 图表高度（像素）。
        :param is_auto_fit: 是否自适应容器大小。
        :param background: 背景色或背景配置。
        :param title_opts: 标题配置。
        :param axis_opts: 坐标轴配置。
        :param legend_opts: 图例配置。
        :param tooltip_opts: 提示框配置。
        :param padding: 内边距（统一设置四边）。
        :returns: 图表对象自身，支持链式调用。
        """
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

    def set_events(
        self,
        event_listeners: types.Optional[dict] = None,
    ) -> Self:
        """设置图表事件监听器。

        将事件类型与 JavaScript 回调函数绑定，生成 ``chart.on(type, callback)``
        代码并注入到渲染输出中。回调函数必须是 JavaScript 代码字符串或
        :class:`~pyantv.commons.utils.JsCode` 对象。

        可配合 :data:`~pyantv.globals.ChartEvent` 常量使用，避免手写事件名。

        :param event_listeners: 事件监听器字典，键为事件类型字符串，
            值为 JavaScript 回调函数代码（字符串或 JsCode）。
        :returns: 图表对象自身，支持链式调用。

        Examples:
            >>> from pyantv import Line
            >>> from pyantv.globals import ChartEvent
            >>> chart = (
            ...     Line()
            ...     .set_data(data=[{"x": 1, "y": 2}])
            ...     .set_encode(x_field_name="x", y_field_name="y")
            ...     .set_events({
            ...         ChartEvent.ELEMENT_CLICK:
            ...             "(ev) => { console.log(ev.data); }",
            ...         ChartEvent.PLOT_CLICK:
            ...             "(ev) => { console.log('plot clicked'); }",
            ...     })
            ... )
        """
        if not event_listeners:
            return self

        from ..commons.utils import JsCode, PLACEHOLDER

        chart_var = f"antv_chart_{self.chart_id}"
        for event_type, callback in event_listeners.items():
            if isinstance(callback, JsCode):
                callback_str = callback.js_code.replace(PLACEHOLDER, "")
            else:
                callback_str = callback
            js_code = f"{chart_var}.on('{event_type}', {callback_str});"
            self.add_js_events(js_code)

        return self

    def set_title(
        self,
        text: types.Optional[str] = None,
        subtitle: types.Optional[str] = None,
        align: types.Optional[str] = None,
    ) -> Self:
        """快捷设置图表标题。

        :param text: 标题文本。
        :param subtitle: 副标题文本。
        :param align: 对齐方式。
        :returns: 图表对象自身，支持链式调用。

        Examples:
            >>> chart = Line().set_title("销售趋势", subtitle="2024年")
        """
        title_opts = opts.TitleOpts(
            title=text,
            subtitle=subtitle,
            align=align,
        )
        self.options.update({"title": title_opts})
        return self

    def set_padding(
        self,
        top: types.Optional[types.Numeric] = None,
        right: types.Optional[types.Numeric] = None,
        bottom: types.Optional[types.Numeric] = None,
        left: types.Optional[types.Numeric] = None,
    ) -> Self:
        """快捷设置图表内边距。

        :param top: 上内边距。
        :param right: 右内边距。
        :param bottom: 下内边距。
        :param left: 左内边距。
        :returns: 图表对象自身，支持链式调用。

        Examples:
            >>> chart = Line().set_padding(top=20, bottom=20)
        """
        padding_dict = {
            "paddingTop": top,
            "paddingRight": right,
            "paddingBottom": bottom,
            "paddingLeft": left,
        }
        for key, value in padding_dict.items():
            if value is not None:
                self.options[key] = value
        return self

    def set_size(
        self,
        width: types.Optional[types.Numeric] = None,
        height: types.Optional[types.Numeric] = None,
        is_auto_fit: types.Optional[bool] = None,
    ) -> Self:
        """快捷设置图表尺寸。

        :param width: 图表宽度。
        :param height: 图表高度。
        :param is_auto_fit: 是否自适应容器大小。
        :returns: 图表对象自身，支持链式调用。

        Examples:
            >>> chart = Line().set_size(width=800, height=600)
            >>> chart = Line().set_size(is_auto_fit=True)
        """
        size_dict = {
            "width": width,
            "height": height,
            "autoFit": is_auto_fit,
        }
        for key, value in size_dict.items():
            if value is not None:
                self.options[key] = value
        return self

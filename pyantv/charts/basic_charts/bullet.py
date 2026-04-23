from ... import options as opts
from ... import types
from ...charts.basic_charts.interval import Interval
from ...charts.composition_charts.space_layer import SpaceLayer


class Bullet(SpaceLayer):
    """子弹图高级封装类。

    基于 G2 的 SpaceLayer + 多个 Interval mark 叠加实现。
    构造时自动创建 range（背景范围）和 measure（实际值）两层，
    可选添加 target（目标值）标记层。

    用户只需通过 :meth:`set_bullet_data` 传入数据和字段名，
    即可自动生成标准子弹图。

    Examples:
        >>> from pyantv import Bullet
        >>> bullet = Bullet().set_bullet_data(
        ...     data=[
        ...         {"title": "Revenue", "ranges": 300,
        ...          "actual": 270, "target": 250},
        ...     ],
        ...     title_field="title",
        ...     range_field="ranges",
        ...     measure_field="actual",
        ...     target_field="target",
        ... )
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self._range_style = {"fill": "#eee"}
        self._measure_style = {"fill": "#5B8FF9"}
        self._target_style = {"fill": "#5ad8a6"}
        self._measure_max_width = 20
        self._target_min_width = 20
        self._transpose = True
        self._hide_y_axis = True

    def set_bullet_data(
        self,
        data: types.Union[types.Sequence, types.Data],
        title_field: str = "title",
        range_field: str = "ranges",
        measure_field: str = "actual",
        target_field: types.Optional[str] = None,
    ) -> "Bullet":
        """设置子弹图数据和字段映射。

        自动创建 range（背景）、measure（实际值）和可选的 target（目标值）
        三个 Interval 层，并通过 SpaceLayer 叠加。

        :param data: 图表数据列表。
        :param title_field: 标题/分类字段名。
        :param range_field: 范围值字段名（背景条）。
        :param measure_field: 实际值字段名（前景条）。
        :param target_field: 目标值字段名（标记线），为 None 时不显示。
        :returns: 图表对象自身，支持链式调用。
        """
        coordinate_opts = (
            opts.CoordinateTransposeOpts() if self._transpose else None
        )
        axis_opts = (
            opts.AxisOpts(y_axis_opts=False) if self._hide_y_axis else None
        )

        range_bar = (
            Interval()
            .set_data(data=data)
            .set_encode(x_field_name=title_field, y_field_name=range_field)
            .set_global_options(
                coordinate_opts=coordinate_opts,
                style_opts=opts.BaseChartStyleOpts(**self._range_style),
                axis_opts=axis_opts,
            )
        )

        measure_bar = (
            Interval()
            .set_data(data=data)
            .set_encode(x_field_name=title_field, y_field_name=measure_field)
            .set_interval_style(max_width=self._measure_max_width)
            .set_global_options(
                coordinate_opts=coordinate_opts,
                style_opts=opts.BaseChartStyleOpts(**self._measure_style),
                axis_opts=axis_opts,
            )
        )

        children = [range_bar.get_options(), measure_bar.get_options()]

        if target_field is not None:
            target_bar = (
                Interval()
                .set_data(data=data)
                .set_encode(
                    x_field_name=title_field, y_field_name=target_field
                )
                .set_interval_style(min_width=self._target_min_width)
                .set_global_options(
                    coordinate_opts=coordinate_opts,
                    style_opts=opts.BaseChartStyleOpts(**self._target_style),
                    axis_opts=axis_opts,
                )
            )
            children.append(target_bar.get_options())

        self.set_space_layer_children(children=children)
        return self

    def set_bullet_style(
        self,
        range_fill: types.Optional[str] = None,
        measure_fill: types.Optional[str] = None,
        target_fill: types.Optional[str] = None,
        measure_max_width: types.Optional[types.Numeric] = None,
        target_min_width: types.Optional[types.Numeric] = None,
        transpose: types.Optional[bool] = None,
        hide_y_axis: types.Optional[bool] = None,
    ) -> "Bullet":
        """设置子弹图各层样式。

        应在 :meth:`set_bullet_data` 之前调用，以便样式生效。

        :param range_fill: 范围背景条填充色。
        :param measure_fill: 实际值前景条填充色。
        :param target_fill: 目标值标记填充色。
        :param measure_max_width: 实际值条最大宽度。
        :param target_min_width: 目标值标记最小宽度。
        :param transpose: 是否转置坐标系（水平子弹图）。
        :param hide_y_axis: 是否隐藏 Y 轴。
        :returns: 图表对象自身，支持链式调用。
        """
        if range_fill is not None:
            self._range_style["fill"] = range_fill
        if measure_fill is not None:
            self._measure_style["fill"] = measure_fill
        if target_fill is not None:
            self._target_style["fill"] = target_fill
        if measure_max_width is not None:
            self._measure_max_width = measure_max_width
        if target_min_width is not None:
            self._target_min_width = target_min_width
        if transpose is not None:
            self._transpose = transpose
        if hide_y_axis is not None:
            self._hide_y_axis = hide_y_axis
        return self

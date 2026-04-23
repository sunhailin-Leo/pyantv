from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Funnel(Chart):
    """漏斗图高级封装类。

    基于 G2 的 interval mark + symmetryY transform + transpose coordinate
    组合实现。构造时自动预置漏斗图所需的 transform、coordinate 配置，
    并在 set_encode 时自动注入漏斗形状。

    支持两种形状：
    - funnel（默认）：标准漏斗形状
    - pyramid：金字塔形状

    Examples:
        >>> from pyantv import Funnel
        >>> funnel = (
        ...     Funnel()
        ...     .set_data(data=[
        ...         {"action": "浏览网站", "pv": 50000},
        ...         {"action": "放入购物车", "pv": 35000},
        ...         {"action": "生成订单", "pv": 25000},
        ...         {"action": "支付订单", "pv": 15000},
        ...         {"action": "完成交易", "pv": 8000},
        ...     ])
        ...     .set_encode(x_field_name="action", y_field_name="pv",
        ...                 color_field="action")
        ... )
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.INTERVAL)
        self._funnel_shape = "funnel"
        self.options.update(transform=[{"type": "symmetryY"}])
        self.options.update(
            coordinate={"transform": [{"type": "transpose"}]}
        )

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
    ):
        """重写父类 set_encode，自动注入漏斗 shape。

        签名与父类完全一致，保留类型提示和 IDE 补全。
        如果用户未显式传入 shape_field，则自动使用当前漏斗形状
        （默认 ``"funnel"``，可通过 :meth:`set_funnel_shape` 修改）。

        :returns: 图表对象自身，支持链式调用。
        """
        if shape_field is None:
            shape_field = self._funnel_shape
        return super().set_encode(
            x_field_name=x_field_name,
            y_field_name=y_field_name,
            z_field_name=z_field_name,
            color_field=color_field,
            shape_field=shape_field,
            size_field=size_field,
            series_field=series_field,
            key_field=key_field,
            group_key_field=group_key_field,
            value_field=value_field,
            rotate_field=rotate_field,
            opacity_field=opacity_field,
            fill_field=fill_field,
            stroke_field=stroke_field,
            stroke_width_field=stroke_width_field,
            font_size_field=font_size_field,
            font_weight_field=font_weight_field,
            dx_field=dx_field,
            dy_field=dy_field,
            title_field=title_field,
            href_field=href_field,
            src_field=src_field,
            ext_field=ext_field,
        )

    def set_funnel_shape(
        self,
        shape: str = "funnel",
    ) -> "Funnel":
        """设置漏斗图形状。

        :param shape: 形状类型，``"funnel"``（标准漏斗）或 ``"pyramid"``（金字塔）。
        :returns: 图表对象自身，支持链式调用。
        """
        self._funnel_shape = shape
        encode = self.options.get("encode", {})
        if isinstance(encode, dict):
            encode["shape"] = shape
            self.options.update(encode=encode)
        return self

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Area(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.AREA)

    def set_area_style(
        self,
        is_connect: types.Optional[bool] = None,
        connect_style_opts: types.Optional[types.BaseChartStyle] = None,
        is_defined: types.Optional[bool] = None,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {
            "connect": is_connect,
            "defined": is_defined,
        }

        if base_style_opts:
            _inner_opts.update(base_style_opts.opts)

        if connect_style_opts:
            connect_style_opts.opts = {
                f"connect{k[:1].upper() + k[1:]}": v
                for k, v in connect_style_opts.opts.items()
            }
            _inner_opts.update(connect_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

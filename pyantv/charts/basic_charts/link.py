from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Link(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.LINK)

    def set_link_style(
        self,
        arrow_size: types.Optional[types.Union[str, types.Numeric]] = None,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {"arrowSize": arrow_size}

        if base_style_opts:
            _inner_opts.update(base_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

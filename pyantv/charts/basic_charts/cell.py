from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Cell(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.CELL)

    def set_cell_style(
        self,
        base_radius_inset_opts: types.Optional[types.BaseChartRadiusInsetStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {}

        if base_radius_inset_opts:
            _inner_opts.update(base_radius_inset_opts.opts)

        self.options.update(style=_inner_opts)

        return self

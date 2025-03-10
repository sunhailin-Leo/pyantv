from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Range(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.RANGE)

    def set_range_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self


class RangeX(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.RANGEX)

    def set_rangex_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self


class RangeY(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.RANGEY)

    def set_rangey_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self

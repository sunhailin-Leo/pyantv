from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Box(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.BOX)

    def set_box_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class BoxPlot(Chart):
    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.BOXPLOT)

    def set_boxplot_style(
        self,
        is_extend: types.Optional[bool] = None,
        point_style_opts: types.Optional[types.BaseChartStyle] = None,
        box_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: dict = {"extend": is_extend}

        if point_style_opts:
            point_style_opts.opts = {
                f"point{k[:1].upper() + k[1:]}": v
                for k, v in point_style_opts.opts.items()
            }
            _inner_opts.update(point_style_opts.opts)

        if box_style_opts:
            box_style_opts.opts = {
                f"box{k[:1].upper() + k[1:]}": v for k, v in box_style_opts.opts.items()
            }
            _inner_opts.update(box_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

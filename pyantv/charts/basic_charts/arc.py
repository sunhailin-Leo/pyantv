from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Arc(Chart):
    """弧形图，用于绘制弧线连接（如弦图中的弧线）。"""

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.ARC)

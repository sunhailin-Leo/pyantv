from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Path(Chart):
    """路径图，用于绘制自定义路径、地图边界等。"""

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.PATH)

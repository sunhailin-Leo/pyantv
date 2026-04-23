from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Line3D(Chart):
    """3D 折线图。

    基于 AntV G2 的 ``line3D`` Mark 类型，需要 WebGL 渲染器
    和 threedlib 扩展库支持。
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.LINE3D)

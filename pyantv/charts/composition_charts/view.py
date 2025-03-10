from pyantv import options as opts
from pyantv import types
from pyantv.charts.chart import Chart
from pyantv.globals import ChartType


class View(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.VIEW)

    def set_view_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

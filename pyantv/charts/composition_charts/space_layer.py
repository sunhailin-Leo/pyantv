from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class SpaceLayer(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.SPACELAYER)

    def set_space_layer_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

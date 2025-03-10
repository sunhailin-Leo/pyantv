from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Vector(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.VECTOR)

    def set_vector_style(
        self,
        arrow_size: types.Optional[types.Union[str, types.Numeric]] = None,
    ):
        self.options.update(style={"arrowSize": arrow_size})

        return self

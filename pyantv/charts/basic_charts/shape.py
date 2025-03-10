from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Shape(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.SHAPE)

    def set_shape_style(
        self,
        x_: types.Optional[types.Union[types.Numeric, str]] = None,
        y_: types.Optional[types.Union[types.Numeric, str]] = None,
        render: types.Optional[types.JSFunc] = None,
    ):
        self.options.update(
            style={
                "x": x_,
                "y": y_,
                "render": render,
            }
        )

        return self

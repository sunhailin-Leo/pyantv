from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class HeatMap(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.HEATMAP)

    def set_heatmap_style(
        self,
        gradient: types.Optional[types.Union[str, types.Sequence]] = None,
        opacity: types.Optional[types.Numeric] = None,
        max_opacity: types.Optional[types.Numeric] = None,
        min_opacity: types.Optional[types.Numeric] = None,
        blur: types.Optional[types.Numeric] = None,
        is_use_gradient_opacity: types.Optional[bool] = None,
    ):
        self.options.update(style={
            "gradient": gradient,
            "opacity": opacity,
            "maxOpacity": max_opacity,
            "minOpacity": min_opacity,
            "blur": blur,
            "useGradientOpacity": is_use_gradient_opacity,
        })

        return self

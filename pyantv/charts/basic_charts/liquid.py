from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Liquid(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.LIQUID)

    def set_liquid_style(
        self,
        outline_border: types.Optional[types.Numeric] = None,
        outline_distance: types.Optional[types.Numeric] = None,
        outline_stroke: types.Optional[str] = None,
        wave_length: types.Optional[types.Numeric] = None,
        background_fill: types.Optional[str] = None,
        text_fill: types.Optional[str] = None,
        text_font_size: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            style={
                "outlineBorder": outline_border,
                "outlineDistance": outline_distance,
                "outlineStroke": outline_stroke,
                "waveLength": wave_length,
                "backgroundFill": background_fill,
                "textFill": text_fill,
                "textFontSize": text_font_size,
            }
        )

        return self

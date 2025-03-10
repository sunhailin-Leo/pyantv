from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Text(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.TEXT)

    def set_text_style(
        self,
        font_size: types.Optional[types.JSFunc] = None,
        font_family: types.Optional[types.JSFunc] = None,
        font_weight: types.Optional[types.JSFunc] = None,
        line_height: types.Optional[types.JSFunc] = None,
        text_align: types.Optional[types.JSFunc] = None,
        text_baseline: types.Optional[types.JSFunc] = None,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style={
            "fontSize": font_size,
            "fontFamily": font_family,
            "fontWeight": font_weight,
            "lineHeight": line_height,
            "textAlign": text_align,
            "textBaseline": text_baseline,
        })

        return self

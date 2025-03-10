from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Wordcloud(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.WORDCLOUD)

    def set_wordcloud_layout(
        self,
        padding: types.Optional[types.Numeric] = None,
        rotate: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
        random: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
        sprial: types.Optional[str] = None,
        image_mask: types.Optional[types.JSFunc] = None,
        font_size: types.Optional[types.Union[types.Numeric, types.JSFunc]] = None,
    ):
        self.options.update(
            layout={
                "padding": padding,
                "rotate": rotate,
                "random": random,
                "sprial": sprial,
                "imageMask": image_mask,
                "fontSize": font_size,
            }
        )
        return self

    def set_wordcloud_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self

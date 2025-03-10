from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Pack(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.PACK)

    def set_pack_layout(
        self,
        sort: types.Optional[types.JSFunc] = None,
        padding: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            layout={
                "sort": sort,
                "padding": padding,
            }
        )
        return self

    def set_pack_style(
        self,
        label_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {}

        if label_style_opts:
            label_style_opts.opts = {
                f"label{k[:1].upper() + k[1:]}": v
                for k, v in label_style_opts.opts.items()
            }
            _inner_opts.update(label_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

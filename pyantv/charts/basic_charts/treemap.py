from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class TreeMap(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.TREEMAP)

    def set_treemap_layout(
        self,
        title: types.Optional[str] = None,
        padding: types.Optional[types.Numeric] = None,
        padding_inner: types.Optional[types.Numeric] = None,
        sort_: types.Optional[types.JSFunc] = None,
        layer: types.Optional[types.JSFunc] = None,
        path: types.Optional[types.JSFunc] = None,
        tile: types.Optional[types.JSFunc] = None,
    ):
        self.options.update(
            layout={
                "title": title,
                "padding": padding,
                "paddingInner": padding_inner,
                "sort": sort_,
                "layer": layer,
                "path": path,
                "tile": tile,
            }
        )
        return self

    def set_treemap_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
        label_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {}

        if base_style_opts:
            _inner_opts.update(base_style_opts.opts)

        if label_style_opts:
            label_style_opts.opts = {
                f"label{k[:1].upper() + k[1:]}": v
                for k, v in label_style_opts.opts.items()
            }
            _inner_opts.update(label_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

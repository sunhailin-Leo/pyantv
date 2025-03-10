from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Tree(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.TREE)

    def set_tree_layout(
        self,
        node_size: types.Optional[types.Numeric] = None,
        sort_by: types.Optional[types.JSFunc] = None,
        separation: types.Optional[types.JSFunc] = None,
    ):
        self.options.update(
            layout={
                "nodeSize": node_size,
                "sortBy": sort_by,
                "separation": separation,
            }
        )
        return self

    def set_tree_style(
        self,
        node_style_opts: types.Optional[types.BaseChartStyle] = None,
        link_style_opts: types.Optional[types.BaseChartStyle] = None,
        label_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        _inner_opts: types.Optional[dict] = {}

        if label_style_opts:
            label_style_opts.opts = {
                f"label{k[:1].upper() + k[1:]}": v
                for k, v in label_style_opts.opts.items()
            }
            _inner_opts.update(label_style_opts.opts)

        if node_style_opts:
            node_style_opts.opts = {
                f"node{k[:1].upper() + k[1:]}": v
                for k, v in node_style_opts.opts.items()
            }
            _inner_opts.update(node_style_opts.opts)

        if link_style_opts:
            link_style_opts.opts = {
                f"link{k[:1].upper() + k[1:]}": v
                for k, v in link_style_opts.opts.items()
            }
            _inner_opts.update(link_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

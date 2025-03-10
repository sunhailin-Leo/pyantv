from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class ForceGraph(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.FORCEGRAPH)

    def set_force_graph_layout(
        self,
        is_joint: types.Optional[bool] = None,
        node_strength: types.Optional[types.JSFunc] = None,
        link_strength: types.Optional[types.JSFunc] = None,
    ):
        self.options.update(
            layout={
                "joint": is_joint,
                "nodeStrength": node_strength,
                "linkStrength": link_strength,
            }
        )
        return self

    def set_force_graph_style(
        self,
        base_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        self.options.update(style=base_style_opts)

        return self

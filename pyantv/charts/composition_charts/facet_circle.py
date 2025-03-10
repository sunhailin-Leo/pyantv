from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class FacetCircle(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.FACETCIRCLE)

    def set_facet_circle_encode(
        self,
        position: types.Optional[types.JSFunc] = None,
    ):
        self.options.update(
            encode={
                "position": position,
            }
        )

        return self

    def set_facet_circle_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class FacetRect(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.FACETRECT)

    def set_facet_rect_encode(
        self,
        x_field_name: types.Optional[types.Union[str, types.Sequence[str]]] = None,
        y_field_name: types.Optional[types.Union[str, types.Sequence[str]]] = None,
    ):
        self.options.update(
            encode={
                "x": x_field_name,
                "y": y_field_name,
            }
        )

        return self

    def set_facet_rect_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

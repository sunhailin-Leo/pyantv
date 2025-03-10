from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Chord(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.CHORD)

    def set_chord_style(
        self,
        y_: types.Optional[types.Numeric] = None,
        id_: types.Optional[types.JSFunc] = None,
        source: types.Optional[types.JSFunc] = None,
        target: types.Optional[types.JSFunc] = None,
        source_weight: types.Optional[types.JSFunc] = None,
        target_weight: types.Optional[types.JSFunc] = None,
        sort_by: types.Optional[types.JSFunc] = None,
        node_width_ratio: types.Optional[types.Numeric] = None,
        node_padding_ratio: types.Optional[types.Numeric] = None,
    ):
        self.options.update(
            style={
                "y": y_,
                "id": id_,
                "source": source,
                "target": target,
                "sourceWeight": source_weight,
                "targetWeight": target_weight,
                "sortBy": sort_by,
                "nodeWidthRatio": node_width_ratio,
                "nodePaddingRatio": node_padding_ratio,
            },
        )

        return self

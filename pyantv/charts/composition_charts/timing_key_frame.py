from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class TimingKeyFrame(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.TIMINGKEYFRAME)

    def set_timing_key_frame_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

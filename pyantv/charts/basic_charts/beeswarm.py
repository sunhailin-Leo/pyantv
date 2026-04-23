from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Beeswarm(Chart):
    """蜂群图 Mark 类。

    用于展示一维数据分布，通过力模拟避免点重叠。
    基于 G2 的 beeswarm mark 实现，使用 d3-force
    力模拟算法对数据点进行布局。

    Examples:
        >>> from pyantv import Beeswarm
        >>> beeswarm = (
        ...     Beeswarm()
        ...     .set_data(data=[
        ...         {"value": 1, "category": "A"},
        ...         {"value": 2, "category": "A"},
        ...         {"value": 3, "category": "B"},
        ...     ])
        ...     .set_encode(x_field_name="value", y_field_name="category")
        ... )
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.BEESWARM)

from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class WaterFall(Chart):
    """瀑布图高级封装类。

    基于 G2 的 interval mark + stackY transform + diffX transform
    组合实现。构造时自动预置瀑布图所需的 transform 配置，
    用户只需设置数据和编码即可得到标准瀑布图。

    瀑布图常用于展示数据的累积变化过程，例如收支明细、
    利润分解等场景。

    Examples:
        >>> from pyantv import WaterFall
        >>> waterfall = (
        ...     WaterFall()
        ...     .set_data(data=[
        ...         {"type": "日用品", "money": 120},
        ...         {"type": "伙食费", "money": 900},
        ...         {"type": "交通费", "money": 200},
        ...         {"type": "水电费", "money": 300},
        ...         {"type": "房租", "money": 1200},
        ...     ])
        ...     .set_encode(x_field_name="type", y_field_name="money")
        ... )
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.INTERVAL)
        self.options.update(transform=[
            {"type": "stackY"},
            {"type": "diffX"},
        ])

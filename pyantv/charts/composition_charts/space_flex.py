from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class SpaceFlex(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.SPACEFLEX)

    def set_space_flex_children(
        self,
        children: types.Optional[types.Sequence[Chart]] = None,
    ):
        self.options.update(
            {
                "children": children,
            }
        )

        return self

    def add_child(self, chart: Chart):
        """添加子图表。

        :param chart: 子图表对象。
        :returns: 当前对象自身，支持链式调用。
        """
        if not hasattr(self, "_children"):
            self._children = []
        self._children.append(chart)
        children = self.options.get("children", [])
        children.append(chart.get_options())
        self.options.update(children=children)
        return self

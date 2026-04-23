from pyantv import options as opts
from pyantv import types
from pyantv.charts.chart import Chart
from pyantv.globals import ChartType


class View(Chart):

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.VIEW)

    def set_view_children(
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

    def link_tooltip(self, shared: bool = True):
        """启用子视图间的 tooltip 联动。

        当鼠标悬停在一个子图表上时，其他子图表也会显示相同
        数据维度的 tooltip，实现多图联动分析。

        :param shared: 是否共享 tooltip，默认 ``True``。
        :returns: 当前对象自身，支持链式调用。

        Examples:
            >>> view = View()
            >>> view.add_child(line_chart).add_child(bar_chart)
            >>> view.link_tooltip()
        """
        interaction = self.options.get("interaction", {})
        if isinstance(interaction, bool):
            interaction = {}
        interaction["tooltip"] = {"shared": shared}
        self.options.update(interaction=interaction)
        return self

    def link_brush(
        self,
        brush_type: str = "rect",
        shared: bool = True,
    ):
        """启用子视图间的框选联动。

        在一个子图表中框选数据范围时，其他子图表会同步高亮
        或过滤相应范围的数据。

        :param brush_type: 框选类型，可选 ``"rect"``、``"x"``、``"y"``。
        :param shared: 是否共享框选状态，默认 ``True``。
        :returns: 当前对象自身，支持链式调用。

        Examples:
            >>> view = View()
            >>> view.add_child(scatter1).add_child(scatter2)
            >>> view.link_brush(brush_type="rect")
        """
        valid_types = ("rect", "x", "y")
        if brush_type not in valid_types:
            raise ValueError(
                "brush_type must be one of {}, got '{}'".format(
                    valid_types, brush_type
                )
            )
        interaction = self.options.get("interaction", {})
        if isinstance(interaction, bool):
            interaction = {}
        interaction["brushHighlight"] = {
            "series": shared,
            "type": brush_type,
        }
        self.options.update(interaction=interaction)
        return self

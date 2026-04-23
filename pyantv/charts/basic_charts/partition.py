from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Partition(Chart):
    """分区图 Mark 类。

    用于展示层级数据的矩形分区可视化，类似旭日图的矩形版本。
    基于 G2 的 partition composite mark 实现，子节点从父节点
    的起始位置开始布局，通过宽度比例展示父子关系。

    Examples:
        >>> from pyantv import Partition
        >>> partition = (
        ...     Partition()
        ...     .set_data(data=[
        ...         {"name": "root", "children": [
        ...             {"name": "A", "value": 10},
        ...             {"name": "B", "value": 20},
        ...         ]}
        ...     ])
        ...     .set_encode(value_field="value")
        ...     .set_partition_layout(fill_parent=True)
        ... )
    """

    def __init__(
        self,
        init_opts: types.Init = opts.InitOpts(),
        render_opts: types.RenderInit = opts.RenderOpts(),
    ):
        super().__init__(init_opts=init_opts, render_opts=render_opts)
        self.options.update(type=ChartType.PARTITION)

    def set_partition_layout(
        self,
        fill_parent: types.Optional[bool] = None,
        sort_: types.Optional[types.JSFunc] = None,
    ):
        """设置分区图布局参数。

        Args:
            fill_parent: 子节点是否填满父节点宽度，默认 True。
            sort_: 节点排序函数。

        Returns:
            图表对象自身，支持链式调用。
        """
        self.options.update(
            layout={
                "fillParent": fill_parent,
                "sort": sort_,
            }
        )
        return self

    def set_partition_style(
        self,
        label_style_opts: types.Optional[types.BaseChartStyle] = None,
    ):
        """设置分区图样式。

        Args:
            label_style_opts: 标签样式配置。

        Returns:
            图表对象自身，支持链式调用。
        """
        _inner_opts: types.Optional[dict] = {}

        if label_style_opts:
            label_style_opts.opts = {
                f"label{k[:1].upper() + k[1:]}": v
                for k, v in label_style_opts.opts.items()
            }
            _inner_opts.update(label_style_opts.opts)

        self.options.update(style=_inner_opts)

        return self

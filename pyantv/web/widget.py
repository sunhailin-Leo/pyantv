"""ipywidgets 交互式图表组件。

提供 ChartWidget 类，让 pyantv 图表可以在 Jupyter Lab 中
作为交互式 Widget 使用，支持参数动态更新。
"""
from typing import Any


def render_widget(
    chart: Any,
    width: str = "100%",
    height: str = "500px",
):
    """在 Jupyter Lab 中以 Widget 形式渲染图表。

    需要安装 ipywidgets（pip install ipywidgets）。

    :param chart: pyantv 图表对象。
    :param width: Widget 宽度，默认 "100%"。
    :param height: Widget 高度，默认 "500px"。
    :returns: ipywidgets.HTML Widget 对象。
    :raises ImportError: 当 ipywidgets 未安装时。
    """
    try:
        import ipywidgets as widgets
    except ImportError:
        raise ImportError(
            "ipywidgets is required for render_widget(). "
            "Install it with: pip install ipywidgets"
        )

    html_content = chart.render_embed()
    widget = widgets.HTML(
        value=html_content,
        layout=widgets.Layout(width=width, height=height),
    )
    return widget


class ChartWidget:
    """交互式图表 Widget 包装器。

    支持动态更新图表数据和配置。
    """

    def __init__(self, chart: Any, width: str = "100%", height: str = "500px"):
        """初始化 ChartWidget。

        :param chart: pyantv 图表对象。
        :param width: Widget 宽度。
        :param height: Widget 高度。
        """
        self._chart = chart
        self._width = width
        self._height = height
        self._widget = None

    def show(self):
        """显示 Widget。

        :returns: ipywidgets.HTML Widget 对象。
        """
        self._widget = render_widget(
            self._chart, width=self._width, height=self._height
        )
        return self._widget

    def update(self, **kwargs):
        """更新图表配置并刷新 Widget。

        :param kwargs: 要更新的配置项。
        """
        if kwargs.get("data") is not None:
            self._chart.set_data(data=kwargs.pop("data"))
        self._chart.options.update(**kwargs)
        if self._widget is not None:
            self._widget.value = self._chart.render_embed()

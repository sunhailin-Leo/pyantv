"""Plotly Dash 集成辅助函数。

提供 ``to_dash()`` 函数，让 pyantv 图表可以嵌入 Plotly Dash 应用。

使用示例
--------

.. code-block:: python

    import dash
    from pyantv import Line
    from pyantv.web import to_dash

    line = (
        Line()
        .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
        .set_encode(x_field_name="x", y_field_name="y")
    )

    app = dash.Dash(__name__)
    app.layout = dash.html.Div([to_dash(line, height="400px")])
"""

from typing import Any, Optional


def to_dash(
    chart: Any,
    width: Optional[str] = None,
    height: Optional[str] = None,
    style: Optional[dict] = None,
) -> Any:
    """将 pyantv 图表渲染为 Dash ``html.Iframe`` 组件。

    通过 iframe ``srcDoc`` 沙盒执行图表 HTML（含 AntV G2 CDN ``<script>`` 与初始化
    脚本），绕过 Dash / React 对内联脚本的剥离。该方案与 Streamlit
    ``components.html()`` 及 Notebook ``build_iframe_html`` 的 srcdoc 嵌入一致。

    需要安装 Dash：``pip install dash`` 或 ``pip install pyantv[dash]``。

    :param chart: pyantv 图表对象（Line、Interval 等，需可实现 ``render_embed()``）。
    :param width: iframe 宽度（CSS 字符串，如 ``"100%"`` / ``"900px"``），默认 None
        表示不显式设置（交由浏览器 / 布局决定）。优先级高于 ``style`` 中的同名键。
    :param height: iframe 高度（CSS 字符串，如 ``"500px"``），默认 None。优先级高于
        ``style`` 中的同名键。
    :param style: 额外的 iframe 行内样式字典，会与 ``width`` / ``height`` 合并为一个
        新字典（不原地修改用户传入的 dict）；后者优先级更高（覆盖同名字段）。
    :returns: ``dash.html.Iframe`` 组件对象，可直接放入 ``dash.html.Div([...])`` 布局。
    :raises ImportError: 当未安装 ``dash`` 时。

    .. note::

        图表隔离在 iframe 沙盒中，跨组件的 Dash 回调无法直接读取图表交互事件
        （如点击 / 筛选）。该限制不在本函数解决，需要跨组件交互时请在应用层
        自行处理。

    Examples:
        >>> import dash
        >>> from pyantv import Line
        >>> from pyantv.web import to_dash
        >>> line = (
        ...     Line()
        ...     .set_data(data=[{"x": 1, "y": 2}])
        ...     .set_encode(x_field_name="x", y_field_name="y")
        ... )
        >>> app = dash.Dash(__name__)
        >>> app.layout = dash.html.Div([to_dash(line, height="400px")])
    """
    try:
        import dash
    except ImportError:
        raise ImportError(
            "Dash is required for to_dash(). "
            "Install it with: pip install dash"
        )

    html_content = chart.render_embed()

    merged_style = dict(style or {})
    if width is not None:
        merged_style["width"] = width
    if height is not None:
        merged_style["height"] = height

    return dash.html.Iframe(srcDoc=html_content, style=merged_style or None)

"""Streamlit 集成辅助函数。

提供 ``st_pyantv()`` 组件，让 pyantv 图表可以嵌入 Streamlit 应用。

使用示例::

    import streamlit as st
    from pyantv import Line
    from pyantv.web import st_pyantv

    line = (
        Line()
        .set_data(data=[{"x": 1, "y": 2}, {"x": 2, "y": 5}])
        .set_encode(x_field_name="x", y_field_name="y")
    )
    st_pyantv(line, height=400)
"""

from typing import Any, Optional


def st_pyantv(
    chart: Any,
    height: int = 500,
    width: Optional[int] = None,
    key: Optional[str] = None,
):
    """在 Streamlit 应用中渲染 pyantv 图表。

    通过 ``streamlit.components.v1.html()`` 将图表嵌入页面。
    需要安装 Streamlit（``pip install streamlit``）。

    :param chart: pyantv 图表对象（Line、Interval 等）。
    :param height: 图表高度（像素），默认 500。
    :param width: 图表宽度（像素），默认 None 表示自适应。
    :param key: Streamlit 组件唯一标识。
    :returns: Streamlit 组件返回值。
    :raises ImportError: 当 Streamlit 未安装时。
    """
    try:
        import streamlit.components.v1 as components
    except ImportError:
        raise ImportError(
            "Streamlit is required for st_pyantv(). "
            "Install it with: pip install streamlit"
        )

    html_content = chart.render_embed()
    return components.html(
        html_content,
        height=height,
        width=width,
        scrolling=False,
    )

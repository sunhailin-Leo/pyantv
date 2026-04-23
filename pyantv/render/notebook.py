"""Notebook 渲染引擎。

提供 Jupyter Notebook / JupyterLab / Google Colab / VS Code Notebook
中的内联渲染支持，使用 iframe srcdoc 方式避免 CSS/JS 污染。
"""

import html as _html_mod
import uuid

from ..types import Optional

# ---------------------------------------------------------------------------
# 全局 Notebook 渲染配置
# ---------------------------------------------------------------------------
_NOTEBOOK_CONFIG = {
    "width": "100%",
    "height": "400px",
    "theme": "default",
}


def notebook_config(
    width: str = "100%",
    height: str = "400px",
    theme: str = "default",
) -> None:
    """配置 Notebook 渲染的全局参数。

    :param width: iframe 宽度，默认 "100%"。
    :param height: iframe 高度，默认 "400px"。
    :param theme: 图表主题，默认 "default"。
    """
    _NOTEBOOK_CONFIG["width"] = width
    _NOTEBOOK_CONFIG["height"] = height
    _NOTEBOOK_CONFIG["theme"] = theme


def is_notebook() -> bool:
    """检测当前是否运行在 Jupyter Notebook 环境中。

    支持检测 Jupyter Notebook / JupyterLab / Google Colab / VS Code Notebook。

    :returns: 如果在 Notebook 环境中返回 True。
    """
    try:
        from IPython import get_ipython

        shell = get_ipython()
        if shell is None:
            return False
        shell_class = type(shell).__name__
        if shell_class == "ZMQInteractiveShell":
            return True
        if shell_class == "TerminalInteractiveShell":
            return False
        # Google Colab
        if "google.colab" in str(type(shell)):
            return True
        return False
    except (ImportError, NameError):
        return False


def build_iframe_html(
    chart_options_json: str,
    js_links: list,
    css_links: list,
    chart_id: Optional[str] = None,
    width: Optional[str] = None,
    height: Optional[str] = None,
    render_options_json: Optional[str] = None,
) -> str:
    """构建 iframe srcdoc HTML 字符串。

    生成一个 self-contained 的 HTML 页面，通过 iframe srcdoc 嵌入，
    避免 CSS/JS 污染宿主 Notebook 页面。

    :param chart_options_json: 图表配置 JSON 字符串。
    :param js_links: JS 资源链接列表。
    :param css_links: CSS 资源链接列表。
    :param chart_id: 图表容器 ID，默认自动生成。
    :param width: iframe 宽度，默认使用全局配置。
    :param height: iframe 高度，默认使用全局配置。
    :param render_options_json: 渲染配置 JSON 字符串。
    :returns: 完整的 iframe HTML 字符串。
    """
    chart_id = chart_id or uuid.uuid4().hex
    iframe_width = width or _NOTEBOOK_CONFIG["width"]
    iframe_height = height or _NOTEBOOK_CONFIG["height"]
    theme = _NOTEBOOK_CONFIG["theme"]

    # 构建 script 标签
    script_tags = "\n".join(
        '<script src="{}"></script>'.format(link) for link in js_links
    )
    css_tags = "\n".join(
        '<link rel="stylesheet" href="{}"/>'.format(link) for link in css_links
    )

    # 构建 theme 配置
    theme_line = ""
    if theme and theme != "default":
        theme_line = 'chart.theme("{}");'.format(theme)

    # 构建 render options
    render_opts_line = ""
    if render_options_json:
        render_opts_line = "Object.assign(renderOpts, {});".format(render_options_json)

    # 内部 HTML 页面
    inner_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    {css_tags}
    {script_tags}
    <style>
        body {{ margin: 0; padding: 0; overflow: hidden; }}
        #{chart_id} {{ width: 100%; height: 100%; }}
    </style>
</head>
<body>
    <div id="{chart_id}"></div>
    <script>
        var renderOpts = {{container: "{chart_id}"}};
        {render_opts_line}
        var chart = new G2.Chart(renderOpts);
        {theme_line}
        chart.options({chart_options});
        chart.render();
    </script>
</body>
</html>""".format(
        css_tags=css_tags,
        script_tags=script_tags,
        chart_id=chart_id,
        chart_options=chart_options_json,
        render_opts_line=render_opts_line,
        theme_line=theme_line,
    )

    # 转义内部 HTML 用于 srcdoc 属性
    escaped_html = _html_mod.escape(inner_html)

    return (
        '<iframe srcdoc="{srcdoc}" '
        'width="{width}" height="{height}" '
        'style="border: none;" '
        'sandbox="allow-scripts allow-same-origin">'
        "</iframe>"
    ).format(
        srcdoc=escaped_html,
        width=iframe_width,
        height=iframe_height,
    )

"""Web 框架集成辅助函数。

提供 Flask / Django / Sanic 等 Web 框架的图表渲染集成。
核心思路：通过 ``render_embed()`` 获取 HTML 字符串，再包装为框架的 Response。

使用示例
--------

Flask::

    from flask import Flask
    from pyantv import Line
    from pyantv.web import make_response

    app = Flask(__name__)

    @app.route("/chart")
    def chart_view():
        line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
        return make_response(line)

Django::

    from django.http import HttpResponse
    from pyantv import Line
    from pyantv.web import render_chart_to_html

    def chart_view(request):
        line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
        return HttpResponse(render_chart_to_html(line))

Sanic::

    from sanic import Sanic
    from sanic.response import html
    from pyantv import Line
    from pyantv.web import render_chart_to_html

    app = Sanic("ChartApp")

    @app.route("/chart")
    async def chart_view(request):
        line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
        return html(render_chart_to_html(line))
"""

from typing import Any, Optional


def render_chart_to_html(
    chart: Any,
    template_name: str = "simple_chart.html",
) -> str:
    """将图表渲染为完整的 HTML 字符串。

    等价于 ``chart.render_embed()``，但提供更语义化的函数名，
    适合在 Web 框架的视图函数中使用。

    :param chart: pyantv 图表对象（Line、Interval 等）。
    :param template_name: Jinja2 模板名称，默认 ``simple_chart.html``。
    :returns: 完整的 HTML 字符串。
    """
    return chart.render_embed(template_name=template_name)


def make_response(
    chart: Any,
    template_name: str = "simple_chart.html",
    status: int = 200,
    headers: Optional[dict] = None,
) -> Any:
    """将图表渲染为 Flask Response 对象。

    需要安装 Flask。如果未安装 Flask，会抛出 ImportError。

    :param chart: pyantv 图表对象。
    :param template_name: Jinja2 模板名称。
    :param status: HTTP 状态码，默认 200。
    :param headers: 额外的 HTTP 响应头。
    :returns: Flask Response 对象。
    """
    try:
        from flask import Response
    except ImportError:
        raise ImportError(
            "Flask is required for make_response(). "
            "Install it with: pip install flask"
        )

    html_content = render_chart_to_html(chart, template_name=template_name)
    response_headers = {"Content-Type": "text/html; charset=utf-8"}
    if headers:
        response_headers.update(headers)

    return Response(
        html_content,
        status=status,
        headers=response_headers,
    )

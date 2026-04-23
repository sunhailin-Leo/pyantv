"""图表导出功能。

提供将图表导出为 PNG 图片和 SVG 矢量图的能力，基于 Playwright 浏览器自动化。

使用示例::

    from pyantv import Line
    from pyantv.render.export import export_png, export_svg

    line = Line().set_data(data=[...]).set_encode(x_field_name="x", y_field_name="y")
    export_png(line, "chart.png", width=1200, height=800)
    export_svg(line, "chart.svg", width=1200, height=800)

或通过 Chart 实例方法::

    line.save_as_image("chart.png", width=1200, height=800)
    line.save_as_svg("chart.svg", width=1200, height=800)
"""

import os
import tempfile
from typing import Any


def export_png(
    chart: Any,
    path: str,
    width: int = 1200,
    height: int = 800,
):
    """将图表导出为 PNG 图片。

    需要安装 Playwright（``pip install playwright``）并执行
    ``playwright install chromium`` 安装浏览器。

    :param chart: pyantv 图表对象。
    :param path: 输出 PNG 文件路径。
    :param width: 视口宽度（像素）。
    :param height: 视口高度（像素）。
    :raises ImportError: 当 Playwright 未安装时。
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError(
            "Playwright is required for export_png(). "
            "Install it with: pip install playwright && "
            "playwright install chromium"
        )

    html_content = chart.render_embed()

    temp_dir = tempfile.mkdtemp()
    temp_html = os.path.join(temp_dir, "chart_export.html")
    try:
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(
                viewport={"width": width, "height": height}
            )
            page.goto(f"file://{temp_html}")
            page.wait_for_timeout(2000)
            page.screenshot(path=path, full_page=False)
            browser.close()
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)


def export_svg(
    chart: Any,
    path: str,
    width: int = 1200,
    height: int = 800,
):
    """将图表导出为 SVG 矢量图。

    需要安装 Playwright（``pip install playwright``）并执行
    ``playwright install chromium`` 安装浏览器。

    :param chart: pyantv 图表对象。
    :param path: 输出 SVG 文件路径。
    :param width: 视口宽度（像素）。
    :param height: 视口高度（像素）。
    :raises ImportError: 当 Playwright 未安装时。
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError(
            "Playwright is required for export_svg(). "
            "Install it with: pip install playwright && "
            "playwright install chromium"
        )

    html_content = chart.render_embed()

    temp_dir = tempfile.mkdtemp()
    temp_html = os.path.join(temp_dir, "chart_export.html")
    try:
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(
                viewport={"width": width, "height": height}
            )
            page.goto(f"file://{temp_html}")
            page.wait_for_timeout(2000)

            # 尝试获取 SVG 元素
            svg_content = page.evaluate(
                "() => {"
                " const svg = document.querySelector('svg');"
                " return svg ? svg.outerHTML : null;"
                " }"
            )

            if svg_content:
                # 写入 SVG 文件
                with open(path, "w", encoding="utf-8") as f:
                    f.write(svg_content)
            else:
                # 如果没有找到 SVG 元素（可能是 Canvas 渲染），则回退到 PNG
                import warnings
                warnings.warn(
                    "No SVG element found. "
                    "The chart may use Canvas renderer. "
                    "Falling back to PNG export.",
                    UserWarning,
                )
                # 将路径改为 PNG
                png_path = path.rsplit(".", 1)[0] + ".png"
                page.screenshot(path=png_path, full_page=False)
                browser.close()
                raise ValueError(
                    "No SVG element found. "
                    "The chart may use Canvas renderer."
                    " PNG saved to {} instead.".format(
                        png_path
                    )
                )

            browser.close()
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)
